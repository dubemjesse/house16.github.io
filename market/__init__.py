from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
import market

db = SQLAlchemy()
db_name = 'market.db'
# migrate = Migrate(app, db)



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db.init_app(app)




from . import routes

# with app.app_context():
#     db.create_all()
#     create_database(app)
