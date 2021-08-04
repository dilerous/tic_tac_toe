import logging
import requests
from os import getenv


def get_logger(name):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
                '%(asctime)s %(name)-6s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(getenv("LOG_LEVEL", "INFO"))
    return logger


tick_tac_logger = get_logger('tic_taci_toe')


class Client:
    def __init__(self):
        self.url = 'http://127.0.0.1:5000/'
        self.players = None
        self.player0_id = None
        self.player1_id = None
        self.board_state = None

    def get_players(self):
        self.players = requests.get(f"{self.url}/players")
        print(self.players.text)

    def get_player(self, player):
        if player == 'player0':
            self.player0_id = requests.get(f"{self.url}/players/{player}")
            print(self.player0_id.text)
        if player == 'player1':
            self.player1_id = requests.get(f"{self.url}/players/{player}")
            print(self.player1_id.text)

    def get_board_state(self):
        self.board_state = requests.get(f"{self.url}/state")
        print(self.board_state.text)


if __name__ == '__main__':
    client = Client()
    client.get_players()
    client.get_board_state()
    client.get_player('player0')
