from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models import Emprestimo, User, Book
from database import db
from datetime import datetime

emprestimo_bp = Blueprint(
    name="emprestimo", 
    import_name=__name__,
    url_prefix='/emprestimos'
)


@emprestimo_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        user_id = request.form['user_id']
        book_id = request.form['book_id']
        data_devolucao = datetime.strptime(request.form['data_devolucao'], "%Y-%m-%d")
        emprestimo = Emprestimo(user_id, book_id, data_devolucao)
        db.session.add(emprestimo)
        db.session.commit()
        return redirect(url_for('emprestimo.index'))
    emprestimos = Emprestimo.query.all()
    users = User.query.all()
    books = Book.query.all()
    return render_template('emprestimos/index.html', emprestimos=emprestimos, users=users, books=books)
