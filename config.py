import os
import json
from configparser import ConfigParser


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')


class Configurations:

    def get_config(self):
        with open(os.getcwd() + '/config_s.json') as file:  # Opening JSON file
            config = json.load(file)  # returns JSON object as a dictionary
        return config

    def get_config2(self):
        try:
            directory_path = os.getcwd()
            constants = ConfigParser()
            constants.read(directory_path + "/constants.ini")
            config2 = {
                "google_key": constants.get('local', 'MAP'),
                "access_id": constants.get('local', 'ID'),
                "access_key": constants.get('local', 'KEY'),
                "bucket_name": constants.get('local', 'BUCKET')
            }
        except:
            config2 = {
                "google_key": os.getenv("HEROKU_GOOGLE_API"),
                "access_id": os.environ.get("ACCESS_ID"),
                "access_key": os.environ.get("ACCESS_KEY"),
                "bucket_name": os.environ.get("BUCKET_NAME")
            }
        return config2
