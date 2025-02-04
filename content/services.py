from ollama import chat
import logging

logger = logging.getLogger(__name__)


def generate_content(topic):
    try:
        content_response = chat(
            model="llama3.2",
            messages=[
                {"role": "user", "content": f"Write a detailed blog post about {topic}"}
            ],
        )
        generated_text = content_response["message"]["content"]
        tag_response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": f"Do not add any other text to your response. Extract 5 keyowrds from this text as coma-separated values: {generated_text}",
                }
            ],
        )
        tags = [
            tag.strip() for tag in tag_response["message"]["content"].split(",")[:5]
        ]
        return generated_text, tags
    except Exception as e:
        logger.error(f"Ollama content generation API error: {str(e)}")
        raise Exception("Content generation failed. Please try again.")


def summarize_content(text):
    try:
        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize this text in 3 sentences: {text}",
                }
            ],
        )
        return response.get("message").get("content")
    except Exception as e:
        logger.error(f"Ollama summarization error: {str(e)}")
        raise Exception("Summarization failed. Please try again")
