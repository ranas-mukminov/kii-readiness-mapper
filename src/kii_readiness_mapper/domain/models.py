from typing import List, Optional
from pydantic import BaseModel, Field
from .enums import Sector, SystemType, MeasureType, KiiCategory, CriticalityLevel

class ControlMeasure(BaseModel):
    id: str
    type: MeasureType
    title: str
    description: str
    is_implemented: bool = False
    comment: Optional[str] = None

class Gap(BaseModel):
    measure_id: str
    type: MeasureType
    criticality: CriticalityLevel
    description: str
    recommendation: str

class SystemProfile(BaseModel):
    id: str
    name: str
    type: SystemType
    description: Optional[str] = None
    is_critical: bool = False # Влияет ли на критические процессы
    users_count: int = 0
    has_external_access: bool = False
    
    # Результаты оценки (заполняются позже)
    estimated_category: KiiCategory = KiiCategory.UNKNOWN
    gaps: List[Gap] = Field(default_factory=list)

class OrganizationProfile(BaseModel):
    name: str
    sector: Sector
    inn: Optional[str] = None
    systems: List[SystemProfile] = Field(default_factory=list)
    
    # Общие меры (на уровне организации)
    org_measures: List[ControlMeasure] = Field(default_factory=list)

class KiiReadinessResult(BaseModel):
    potential_kii_subject: bool
    subject_confidence: str # low, medium, high
    estimated_category: KiiCategory
    
    subject_score: float = 0.0
    criticality_score: float = 0.0
    org_controls_score: float = 0.0
    tech_controls_score: float = 0.0
    
    summary_text: str
    key_risks: List[str] = Field(default_factory=list)
