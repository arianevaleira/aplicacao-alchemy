from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from datetime import datetime
from database import db

class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    autor: Mapped[str]

    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor

class Emprestimo(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    book_id: Mapped[int] = mapped_column(ForeignKey('book.id'))
    data_emprestimo: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    data_devolucao: Mapped[datetime]

    user = relationship('User', backref='emprestimos')
    book = relationship('Book', backref='emprestimos')
