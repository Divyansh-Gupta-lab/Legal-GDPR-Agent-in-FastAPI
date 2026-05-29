import operator
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage
from langchain_core.documents import Document
from langgraph.graph.message import add_messages

from schemas.assessment_schema import QualityAssessment
from schemas.classification_schema import QuestionClassification
from schemas.retry_log_schema import RetryLog

class MainState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    summary: str
    answer: str
    context: list[Document]
    should_abort: bool
    
class ClassificationState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    summary: str
    classification: QuestionClassification | None
    should_abort: bool
    
class RetrievalState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    summary: str
    context: list[Document]
    retrieval_query: str
    context_quality: QualityAssessment | None
    retry_attempt: int
    retries: Annotated[list[RetryLog], operator.add]
    should_abort: bool
    
class AnswerState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    summary: str
    context: list[Document]
    answer: str
    answer_feedback: QualityAssessment | None
    retry_attempt: int
    retries: Annotated[list[RetryLog], operator.add]
    should_abort: bool