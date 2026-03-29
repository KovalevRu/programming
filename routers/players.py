from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Player, Team
from schemas import PlayerCreate, PlayerResponse

router = APIRouter(prefix="/players", tags=["players"])

# такая же функция для сессии как в teams
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# получить всех игроков
@router.get("/", response_model=list[PlayerResponse])
def get_players(db: Session = Depends(get_db)):
    return db.query(Player).all()

# получить игрока по айди
@router.get("/{player_id}", response_model=PlayerResponse)
def get_player(player_id: int, db: Session = Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

# создать игрока
@router.post("/", response_model=PlayerResponse)
def create_player(player_data: PlayerCreate, db: Session = Depends(get_db)):
    if player_data.team_id is not None:
        team = db.query(Team).filter(Team.id == player_data.team_id).first()
        if not team:
            raise HTTPException(status_code=404, detail="Team not found")

    player = Player(**player_data.model_dump())
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

@router.patch("/{player_id}", response_model=PlayerResponse)
def update_player(player_id: int, player_data: PlayerCreate, db: Session = Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    for field, value in player_data.model_dump().items():
        setattr(player, field, value)
    db.commit()
    db.refresh(player)
    return player

@router.delete("/{player_id}")
def delete_player(player_id: int, db: Session = Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    db.delete(player)
    db.commit()
    return {"message": "Player deleted"}