#encode:utf-8
import werobot
token_id = "mazhongyi14789"
robot = werobot.WeRoBot(token=token_id)

def hello(message):
    return 'Hello World!'
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
