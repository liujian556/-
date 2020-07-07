from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from apps.cms.models import CmsUser
from exts import db
from yqbbs import create_app

app = create_app()

manage = Manager(app)
Migrate(app,db)


manage.add_command('db',MigrateCommand)

@manage.option('-u','--username',dest='username')
@manage.option('-p','--password',dest='password')
@manage.option('-e','--email',dest='email')

def create_cms_user(username,password,email):
    cms_user = CmsUser
    cms_user = cms_user(username=username,_password=password,email=email)

    db.session.add(cms_user)
    db.session.commit()
    print('cms用户添加成功')

if __name__ == '__main__':
    manage.run()