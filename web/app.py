from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

def create_app():
    app = Flask(__name__)
    app.secret_key = "supersecretkey"

    def get_db_connection():
        conn = sqlite3.connect('data/database.db')
        conn.row_factory = sqlite3.Row
        return conn

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/users')
    def users():
        conn = get_db_connection()
        users = conn.execute('SELECT * FROM users').fetchall()
        conn.close()
        return render_template('users.html', users=users)

    @app.route('/user/<int:id>')
    def user(id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()
        conn.close()
        if user is None:
            return 'User not found'
        return render_template('user.html', user=user)

    @app.route('/user/edit/<int:id>', methods=('GET', 'POST'))
    def edit_user(id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()
        
        if request.method == 'POST':
            xp = request.form['xp']
            balance = request.form['balance']
            conn.execute('UPDATE users SET xp = ?, balance = ? WHERE id = ?', (xp, balance, id))
            conn.commit()
            conn.close()
            flash('User updated successfully!')
            return redirect(url_for('user', id=id))

        conn.close()
        return render_template('edit_user.html', user=user)

    return app
    
