from pydantic import BaseModel, Field, field_validator
from typing import List


class PointsetFieldModel(BaseModel):
    pointSetFieldId: str
    attribute: str
    numPoints: int
    minVal: float = Field(ge=-50450.34, le=3072481.0)
    maxVal: float = Field(ge=0.0, le=9.1156998E8)


class PointsetModel(BaseModel):
    pointSetId: str
    geoName: str
    mapDataSetName: str
    interpreter: str
    minX: float
    minY: float
    maxX: float
    maxY: float
    numPoints: int
    updateUser: str
    pointsetFields: List[PointsetFieldModel]

    @field_validator('minX')
    @classmethod
    def check_min_x(cls, v: float):
        min_x_values = [456030.03, 457297.38, 458501.34]
        if v not in min_x_values:
            raise ValueError(f'Invalid minX value: {v}, expected values: {min_x_values}')
        return v

    @field_validator('minY')
    @classmethod
    def check_min_y(cls, v: float):
        min_y_values = [6786009.0, 6787241.5, 6788410.5]
        if v not in min_y_values:
            raise ValueError(f'Invalid minY value: {v}, expected values: {min_y_values}')
        return v

    @field_validator('maxX')
    @classmethod
    def check_max_x(cls, v: float):
        max_x_values = [456118.78, 457386.1, 458754.78]
        if v not in max_x_values:
            raise ValueError(f'Invalid maxX value: {v}, expected values: {max_x_values}')
        return v

    @field_validator('maxY')
    @classmethod
    def check_max_y(cls, v: float):
        max_y_values = [6786098.0, 6787330.5, 6788663.5]
        if v not in max_y_values:
            raise ValueError(f'Invalid maxY value: {v}, expected values: {max_y_values}')
        return v

    @field_validator('numPoints')
    @classmethod
    def check_num_points(cls, v: int):
        num_points_values = [13, 195, 449]
        if v not in num_points_values:
            raise ValueError(f'Invalid numPoints value: {v}, expected values: {num_points_values}')
        return v


class ResponseTileGenModel(BaseModel):
    status: str
    message: str
    pointsets: List[PointsetModel]

    @field_validator('pointsets')
    @classmethod
    def check_pointsets_size(cls, v: List[PointsetModel]):
        if v.__len__() != 2:
            raise ValueError(f'Invalid pointsets size value: {v.__len__()}, expected value: 2')
        return v
