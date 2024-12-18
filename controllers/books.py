from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import Book
from database import db

books_bp = Blueprint('books', __name__, url_prefix='/books')

@books_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        autor = request.form['autor']
        book = Book(nome, autor)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books.index'))
    books = Book.query.all()
    return render_template('books/index.html', books=books)
