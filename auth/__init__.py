from flask_login import LoginManager, login_user, logout_user
from flask import Blueprint, render_template, request,url_for, redirect, flash
from models import User
from database import db
from werkzeug.security import check_password_hash

auth_bp = Blueprint(name="auth", 
    import_name=__name__, 
    url_prefix='/auth',
    template_folder='templates')

login_manager = LoginManager()

@login_manager.user_loader #faz o login 
def load_user(user_id):
    return db.get_or_404(User, user_id)

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        user = User(nome, email, senha)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        result = db.session.execute(db.select(User).where(User.email == email)).first()
        
        if result[0] and check_password_hash(result[0].senha, senha):            
            login_user(result[0])
            return redirect(url_for('users.index'))
        else:
            flash('Erro nos dados')       
        
        
    return render_template('auth/login.html')

@auth_bp.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))