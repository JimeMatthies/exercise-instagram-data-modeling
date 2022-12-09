import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(280), nullable=False)
    email = Column(String(280), nullable=False)
    password = Column(String(280), nullable=False)

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    media_url = Column(String(280), nullable=False)
    title = Column(String(280), nullable=False)
    description = Column(String(280))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_date = Column(DateTime(0))

class Like(Base):
    __tablename__ = 'like'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment = Column(String(280), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    post = relationship(Post)

class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'))
    following_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    #def to_dict(self):
    #    return {}
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
