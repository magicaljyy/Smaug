#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
import logging
from logging import Formatter, FileHandler
from forms import *
import os
from model.shared import db
from flask_restful import Api

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

# Import views
from views import basic
from views.items import ItemAPI, ItemListAPI, ItemActionAPI

# Add routes
app.add_url_rule('/', 'home', view_func=basic.home, methods=['GET', 'POST'])

app.add_url_rule('/about', 'about', view_func=basic.about)

app.add_url_rule('/login', 'login', view_func=basic.login, methods=['GET', 'POST'])

app.add_url_rule('/register', 'register', view_func=basic.register)

app.add_url_rule('/forgot', 'forgot', view_func=basic.forgot)

app.add_url_rule('/testdb', 'testdb', view_func=basic.testdb)

app.add_url_rule('/logout', 'logout', view_func=basic.logout)

# Add api routes
api = Api(app)
api.add_resource(ItemAPI, '/items/<item_id>')
api.add_resource(ItemListAPI, '/items')
api.add_resource(ItemActionAPI, '/items/<item_id>/buy')

@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404
    
# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
