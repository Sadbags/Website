from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MenuItem(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(255), nullable=True)
	price = db.Column(db.Float, nullable=False)

	def __repr__(self):
		return f'<MenuItem {self.name}>'
