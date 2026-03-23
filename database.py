from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

engine = create_engine('sqlite:///database.db')
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)