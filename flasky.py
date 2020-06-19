import os
from app import create_app, db
from app.models import User, Role, Article
from flask_migrate import Migrate

# set FLASK_APP=flasky.py
# set FLASK_DEBUG=1
# flask run

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Article=Article)