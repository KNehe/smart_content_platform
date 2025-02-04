from django.urls import path
from .views import (
    UserRegistrationView,
    GenerateContentView,
    SummarizeContentView,
    UserContentView,
    RecommendationView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("api/register/", UserRegistrationView.as_view(), name="user-registration"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/generate-content/", GenerateContentView.as_view(), name="generate-content"
    ),
    path(
        "api/summarize-content/",
        SummarizeContentView.as_view(),
        name="summarize-content",
    ),
    path("api/user-content/", UserContentView.as_view(), name="user-content"),
    path(
        "api/recommendations/<int:content_id>/",
        RecommendationView.as_view(),
        name="recommendations",
    ),
]
