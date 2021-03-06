from flask.ext.admin import Admin
from flask.ext.cache import Cache
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask_assets import Environment

cache = Cache()

assets_env = Environment()

debug_toolbar = DebugToolbarExtension()

admin = Admin(url='/', base_template='base_master.html', template_mode='bootstrap3')
