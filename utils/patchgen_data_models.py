from pydantic import BaseModel, Field, field_validator
from typing import List, Optional


class ExecutionTimeModel(BaseModel):
    read: str = Field(pattern=r"\d{2}:\d{2}:\d{2}\.\d{3}")
    calc: str = Field(pattern=r"\d{2}:\d{2}:\d{2}\.\d{3}")
    total: str = Field(pattern=r"\d{2}:\d{2}:\d{2}\.\d{3}")
    write: str = Field(pattern=r"\d{2}:\d{2}:\d{2}\.\d{3}")


class PointsetFieldModel(BaseModel):
    pointSetFieldId: str = Field(pattern=r"\d+")
    attribute: str = Field(pattern=r"\w+")
    numPoints: int
    minVal: float = Field(ge=0.0, le=1.0)
    maxVal: float

    @field_validator('maxVal')
    @classmethod
    def check_min_y(cls, v: float):
        max_val = [147018.0, 0.0, 2149.0, 546.0, 1.0, 1081.0, 1484.0, 386.0]
        if v not in max_val:
            raise ValueError(f'Invalid minY value: {v}, expected values: {max_val}')
        return v


class PatchesDataModel(BaseModel):
    pointSetId: str = Field(pattern=r"\d+")
    geoName: str = Field(pattern=r"\w+")
    mapDataSetName: str = Field(pattern=r"\w+")
    interpreter: str = "LGC"
    minX: float = 455966.72
    minY: float = 6785898.0
    maxX: float = 459641.9
    maxY: float = 6789573.0
    numPoints: int = 147018
    remark: Optional[str] = None
    updateUser: str = Field(pattern=r"[\w\.]+")
    pointsetFields: List[PointsetFieldModel]


class PointsetModel(BaseModel):
    patches: PatchesDataModel


class DetailsModel(BaseModel):
    pointSet: PointsetModel
    executionTime: ExecutionTimeModel


class ResponsePatchGenModel(BaseModel):
    status: str = "OK"
    message: str
    details: DetailsModel
