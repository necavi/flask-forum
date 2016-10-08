from flask_script import Manager
import flask_security.script as sec
from application import app, db

manager = Manager(app)
manager.add_command('create_user', sec.CreateUserCommand())
manager.add_command('create_role', sec.CreateRoleCommand())
manager.add_command('add_role',    sec.AddRoleCommand())
manager.add_command('remove_role', sec.RemoveRoleCommand())


@manager.command
def create_db():
    """Creates database from sqlalchemy schema."""
    db.create_all()


def main():
    manager.run()


if __name__ == '__main__':
    main()
