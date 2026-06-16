
from langchain_google_genai import ChatGoogleGenerativeAI
from core.config import settings

llm = ChatGoogleGenerativeAI(
    google_api_key=settings.GOOGLE_GENAI_API_KEY,
    model=settings.GOOGLE_GENAI_MODEL,
    temperature=0
)