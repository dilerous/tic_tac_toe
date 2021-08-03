import redis
import logging
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


tick_tac_logger = get_logger('tick_tac')


class Redisdb:
    def __init__(self, **kwargs):
        tick_tac_logger.debug("__init__ method of Redisdb")
        self.db = redis.Redis(charset="utf-8", decode_responses=True)
        self.playerone_id = kwargs.get('playerone_id')
        self.playertwo_id = kwargs.get('playertwo_id')
        self.game_id = kwargs.get('game_id')
        self.state = kwargs.get('board_state')
        print(self.db)

    def delete_key(self, key):
        self.db.delete(key)
        return True

    def set_key(self, key, value):
        tick_tac_logger.debug("set_key method of Redisdb")
        self.db.mset({key: value})
        return True

    def get_key(self, key):
        self.db.get(key)
        return self.db.get(key)

    def create_list(self, list_values):
        tick_tac_logger.debug("create_list method of Redisdb")
        for item in reversed(list_values):
            self.db.lpush('board_state', str(item))
        return True

    def update_list(self, index, value):
        tick_tac_logger.debug("update_list method of Redisdb")
        self.db.lset('board_state', index, value)
        return True

    def get_list(self, value):
        tick_tac_logger.debug("get_list method of Redisdb")
        return self.db.lrange(value, 0, -1)
