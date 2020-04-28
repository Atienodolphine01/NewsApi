from flask_script import Server,Manager
from app import create_app
from config import Config
app = create_app('production')

manager = Manager(app)

manager.add_command('server',Server)

@manager.command
def test():
    '''
    Runnig automated tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestResult(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()