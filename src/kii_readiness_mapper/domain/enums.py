from enum import Enum

class Sector(str, Enum):
    HEALTH = "health"
    TRANSPORT = "transport"
    ENERGY = "energy"
    FINANCE = "finance"
    SCIENCE = "science"
    TELECOM = "telecom"
    FUEL = "fuel"
    ATOMIC = "atomic"
    DEFENSE = "defense"
    ROCKET = "rocket"
    MINING = "mining"
    METAL = "metal"
    CHEMICAL = "chemical"
    OTHER = "other"

class SystemType(str, Enum):
    SCADA = "scada"  # АСУ ТП
    IS = "is"        # Информационная система (ИС)
    ITS = "its"      # Информационно-телекоммуникационная сеть (ИТС)
    WEB = "web"      # Веб-сервис / сайт
    OFFICE = "office" # Офисная сеть
    OTHER = "other"

class MeasureType(str, Enum):
    ORG = "org"   # Организационная мера
    TECH = "tech" # Техническая мера

class MaturityLevel(str, Enum):
    NONE = "none"
    INITIAL = "initial"
    DEFINED = "defined"
    MANAGED = "managed"
    OPTIMIZED = "optimized"

class KiiCategory(str, Enum):
    CAT_1 = "1"
    CAT_2 = "2"
    CAT_3 = "3"
    NONE = "none"
    UNKNOWN = "unknown"

class CriticalityLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
