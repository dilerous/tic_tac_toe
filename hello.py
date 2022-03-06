from flask import Flask, render_template
from flask_sse import sse
from flask import request
import logging
from os import getenv
import main


app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')


def get_logger(name):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
                '%(asctime)s %(name)-6s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(getenv("LOG_LEVEL", "INFO"))
    return logger


tick_tac_logger = get_logger('tick_tac')


class User():
    def __init__(self):
        self.first_name = 'Brad'
        self.last_name = 'Soper'


class Flask_sse_message():
    def __init__(self, data, type=None, id=None, retry=None):
        self.data = data
        pass

    def to_string(self, data):
        string_data = str(data)
        return string_data

    def to_dict(self, lst):
        res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
        return res_dct
        pass


class Flask_sse_ServerSentEventsBlueprint():
    def __init__(self):
        pass

    def messages(self, channel='sse'):
        pass

    def publish(self, data, type=None, id=None, retry=None, channel='sse'):
        pass

    def redis(self):
        pass

    def stream(self):
        pass


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello_world():
    name = 'Brad'
    sse.publish({"message": f"Hello! {name}"}, type='greeting')
    return "Message sent!"


@app.route("/game")
def publish_redis():
    name = 'Brad'
    sse.publish({"message": f"Hello! {name}"}, type='greeting')
    return "Message sent!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route("/users/<name>")
def me_api(name):
    user = User()
    if user.first_name == name:
        return {
            "first_name": user.first_name,
            "last_name": user.last_name
        }
    else:
        return f"The name {name} was not found"


@app.route("/players/<player>")
def get_player(player):
    redis = main.Redisdb()
    if player == 'player0':
        playerone = redis.get_key('playerone_id')
        return playerone
    if player == 'player1':
        playertwo = redis.get_key('playertwo_id')
        return playertwo


@app.route("/players")
def get_players():
    redis = main.Redisdb()
    playerone = str(redis.get_key('playerone_id'))
    playertwo = str(redis.get_key('playertwo_id'))
    players = {"player_one": playerone,
               "player_two": playertwo
               }
    return players


@app.route("/state")
def get_state():
    redis = main.Redisdb()
    board_state = str(redis.get_list('board_state'))
    return board_state


def do_the_login():
    x = "Example of the POST"
    return x


def show_the_login_form():
    x = "I'm in the login form"
    return x
