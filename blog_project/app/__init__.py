#主要是对整个应用程序做初始化操作
# 主要工作:
# 1.创建flask的应用以及各种的配置
# 2.创建数据库 - sqlalchemy的实例
# 3.通过蓝图去关联其他的业务程序
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

#创建数据库的实例
db = SQLAlchemy()
# 通过一个函数创建app
def create_app():
    app = Flask(__name__)
    # 有关app的各种配置
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost:3306/blog"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SECRET_KEY'] = 'xingchengbian'
    # 使用app初始化db(数据库)
    db.init_app(app)
    # 使用蓝图关联程序
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)
    return app