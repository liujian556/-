from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class CmsUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    _password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50),nullable=False,unique=True)
    join_time =db.Column(db.DateTime,default=datetime.now)


# 对外叫 password  对内叫__password

    @property
    def password(self):
        return self._password

    # 用户输入的密码传入
    def password(self,raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self,raw_password):
        result = check_password_hash(self.password,raw_password)
        return result

# 实例 user = CmsUser()
# user.password = 'text'
