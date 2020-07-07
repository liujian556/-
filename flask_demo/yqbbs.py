from flask import Flask

import config
from apps.cms.views import blue_cms
from apps.front.views import blue_front
from exts import db
from apps.cms.models import CmsUser
def create_app():
    app = Flask(__name__)
    # models
    app.config.from_object(config.ENV_DATABASE.get('database'))
    db.init_app(app)

    # 蓝图
    app.register_blueprint(blue_front)
    app.register_blueprint(blue_cms)


    return app

