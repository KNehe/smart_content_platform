from rest_framework.views import APIView
from .serializers import UserRegistratoinSerializer, ContentSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from .services import generate_content, summarize_content
from rest_framework.permissions import IsAuthenticated
from .models import Content


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistratoinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenerateContentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            topic = request.data.get("topic")
            if not topic:
                return Response(
                    {"detail": "Topic is required"}, status=status.HTTP_400_BAD_REQUEST
                )
            generated_text, tags = generate_content(topic)
            content = Content.objects.create(
                user=request.user,
                topic=topic,
                generated_text=generated_text,
                tags=tags,
            )
            serializer = ContentSerializer(content)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class SummarizeContentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            text = request.data.get("text")
            if not text:
                return Response(
                    {"detail": "Text is required"}, status=status.HTTP_400_BAD_REQUEST
                )
            summary = summarize_content(text)
            return Response({"summary": summary}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserContentView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContentSerializer

    def get_queryset(self):
        return Content.objects.filter(user=self.request.user).order_by("-created_at")


class RecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, content_id):
        try:
            target_content = Content.objects.get(id=content_id, user=request.user)
            similar_content = Content.objects.filter(
                user=request.user, tags__overlap=target_content.tags
            ).exclude(id=content_id)[:5]
            serializer = ContentSerializer(similar_content, many=True)
            return Response(serializer.data)
        except Content.DoesNotExist:
            return Response(
                {"error": "Content not found"}, status=status.HTTP_404_NOT_FOUND
            )
