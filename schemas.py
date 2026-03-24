from pydantic import BaseModel
from typing import Optional

class TeamCreate(BaseModel):
    name: str
    city: str
    coach: Optional[str] = None
    wins: int = 0
    losses: int = 0

class TeamResponse(BaseModel):
    id: int
    name: str
    city: str
    coach: Optional[str]
    wins: int
    losses: int

    class Config:
        from_attributes = True


class PlayerCreate(BaseModel):
    name: str
    surname: str
    avg_pts: float = 0.0
    avg_assists: float = 0.0
    avg_reb: float = 0.0
    team_id: Optional[int] = None

class PlayerResponse(BaseModel):
    id: int
    name: str
    surname: str
    avg_pts: float
    avg_assists: float
    avg_reb: float
    team_id: Optional[int]

    class Config:
        from_attributes = True