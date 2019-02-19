import configparser
import redis

config = configparser.ConfigParser()
config.read('config.ini')
port_ = config['REDIS']['PORT']
host_ = config['REDIS']['HOST']
password_ = config['REDIS']['PASSWORD']


class RedisOperations(object):
    def __init__(self):
        self.r = redis.Redis(host=host_, port=port_, password=password_)

    def save_message(self, username, message):
        try:
            result = self.r.set(username, message)
            if result is True:
                return {"username": username, "message": message}
            else:
                return "Can not save to redis"
        except redis.exceptions.DataError:
            raise

    def get_messages(self):
        result_list = list()
        try:
            result = self.r.keys()
            for keyname in result:
                result_dict = dict()
                value = self.r.get(keyname)
                result_dict['username'] = keyname.decode('utf-8')
                result_dict['message'] = value.decode('utf-8')
                result_list.append(result_dict)
            return result_list
        except redis.exceptions.DataError:
            raise
