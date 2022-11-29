from pydantic import BaseModel


class DistrictCapitalsScheme(BaseModel):
    COV_DIST_1: int
    NAMECAP: str
    DISTRICT: str
    POPCAP: int
    POINT_X: float
    POINT_Y: float
    xcoord: float
    ycoord: float
