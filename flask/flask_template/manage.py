from flask_migrate import MigrateCommand
from flask_script import Manager

from APPS import create_app

pro_env='default'

app = create_app(pro_env)


manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()