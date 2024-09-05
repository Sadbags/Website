from flask import Flask, render_template
from config import Config
from database import db
from models import db, MenuItem

app = Flask(__name__)

db_name = 'restaurant_menu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    items = MenuItem.query.all()
    return render_template('menu.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)