from epl import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column,relationship, Mapped
from typing import List

class Club(db.Model):
  __tablename__  = 'club'
  id: Mapped[int] =mapped_column(Integer, primary_key =True)
  name: Mapped[str] =mapped_column(String(50),unique =True,nullable =False)
  staduim :  Mapped[int] =mapped_column (String(50),unique =True,nullable =False)
  year:  Mapped[int] =mapped_column (Integer, nullable =False)
  logo: Mapped[str] =mapped_column (String(225), nullable =False)
  
  players: Mapped[List['Player']] = relationship(back_populates='club')
  
  def __repr__(self):
    return f'<club: {self.name}>'
  
  
class Player(db.Model):
  __tablename__  = 'player'
  id: Mapped[int] =mapped_column(Integer, primary_key =True)
  name: Mapped[str] =mapped_column (String(50),nullable =False)
  position :  Mapped[int] =mapped_column (String(50),nullable =False)
  nationality:  Mapped[int] =mapped_column (String(50),nullable =False)
  img: Mapped[str] =mapped_column (String(225),nullable =False)
  club_id : Mapped[int] = mapped_column(Integer, ForeignKey(Club.id))
  
  club: Mapped[Club] =relationship(back_populates='players')
  
  def __repr__(self):
    return f'<Player: {self.name}>'
  