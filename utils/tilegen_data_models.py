from pydantic import BaseModel, Field, field_validator
from typing import List


class ExecutionTimeModel(BaseModel):
    read: str = Field(pattern=r"\d{2}:\d{2}:\d{2}\.\d{3}")
    calc: str = Field(pattern=r"\d{2}:\d{2}:\d{2}\.\d{3}")
    total: str = Field(pattern=r"\d{2}:\d{2}:\d{2}\.\d{3}")
    write: str = Field(pattern=r"\d{2}:\d{2}:\d{2}\.\d{3}")


class PointsetFieldModel(BaseModel):
    pointSetFieldId: str = Field(pattern=r"\d+")
    attribute: str = Field(pattern=r"\w+")
    numPoints: int
    minVal: float = Field(ge=-138472.28, le=1004459.4)
    maxVal: float = Field(ge=0.0, le=7.2936202E9)


class PointsetDataModel(BaseModel):
    pointSetId: str = Field(pattern=r"\d+")
    geoName: str = Field(pattern=r"\w+")
    mapDataSetName: str = Field(pattern=r"\w+")
    interpreter: str = "LGC"
    minX: float
    minY: float
    maxX: float
    maxY: float
    numPoints: int
    remark: str = "Autotest"
    updateUser: str = Field(pattern=r"[\w\.]+")
    pointsetFields: List[PointsetFieldModel]

    @field_validator('minX')
    @classmethod
    def check_min_x(cls, v: float):
        min_x_values = [456030.03, 457297.38, 458501.34, 456600.34, 457867.66]
        if v not in min_x_values:
            raise ValueError(f'Invalid minX value: {v}, expected values: {min_x_values}')
        return v

    @field_validator('minY')
    @classmethod
    def check_min_y(cls, v: float):
        min_y_values = [6786009.0, 6787241.0, 6788410.0, 6786561.5, 6787794.0]
        if v not in min_y_values:
            raise ValueError(f'Invalid minY value: {v}, expected values: {min_y_values}')
        return v

    @field_validator('maxX')
    @classmethod
    def check_max_x(cls, v: float):
        max_x_values = [456118.78, 457424.12, 458754.78, 456853.84, 458121.12]
        if v not in max_x_values:
            raise ValueError(f'Invalid maxX value: {v}, expected values: {max_x_values}')
        return v

    @field_validator('maxY')
    @classmethod
    def check_max_y(cls, v: float):
        max_y_values = [6786098.0, 6787368.0, 6788663.0, 6786815.0, 6788047.5]
        if v not in max_y_values:
            raise ValueError(f'Invalid maxY value: {v}, expected values: {max_y_values}')
        return v

    @field_validator('numPoints')
    @classmethod
    def check_num_points(cls, v: int):
        num_points_values = [9, 193, 544, 368, 327]
        if v not in num_points_values:
            raise ValueError(f'Invalid numPoints value: {v}, expected values: {num_points_values}')
        return v


class PointsetModel(BaseModel):
    tiles: PointsetDataModel
    meantrace: PointsetDataModel


class DetailsModel(BaseModel):
    pointSet: PointsetModel
    executionTime: ExecutionTimeModel


class ResponseTileGenModel(BaseModel):
    status: str = "OK"
    message: str
    details: DetailsModel
