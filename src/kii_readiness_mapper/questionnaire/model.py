from typing import List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field

class QuestionType(str, Enum):
    SINGLE_CHOICE = "single_choice"
    MULTI_CHOICE = "multi_choice"
    YES_NO = "yes_no"
    SCALE = "scale"
    FREE_TEXT = "free_text"

class AnswerOption(BaseModel):
    id: str
    label: str
    value: Union[str, int, float, bool]
    weight: float = 0.0 # Влияние на скоринг
    next_question_id: Optional[str] = None # Ветвление (пока простое)

class Question(BaseModel):
    id: str
    text: str
    type: QuestionType
    options: Optional[List[AnswerOption]] = None
    weight: float = 1.0
    required: bool = True
    help_text: Optional[str] = None

class Section(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    questions: List[Question] = Field(default_factory=list)

class Questionnaire(BaseModel):
    sections: List[Section] = Field(default_factory=list)
