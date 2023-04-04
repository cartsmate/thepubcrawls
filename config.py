import os
import json
from configparser import ConfigParser


class Configurations:

    def get_config(self):
        directory_path = os.getcwd()
        constants = ConfigParser()
        constants.read(directory_path + "/constants.ini")
        config = dict()

        config['aws_key_pub'] = constants.get("Aws_keys", "PUB")
        config['aws_key_review'] = constants.get("Aws_keys", "REVIEW")
        config['aws_key_station'] = constants.get("Aws_keys", "STATION")
        config['aws_key_area'] = constants.get("Aws_keys", "AREA")

        config['aws_prefix_pub'] = constants.get("Aws_prefixs", "PUB")
        config['aws_prefix_review'] = constants.get("Aws_prefixs", "REVIEW")
        config['aws_prefix_station'] = constants.get("Aws_prefixs", "STATION")
        config['aws_prefix_area'] = constants.get("Aws_prefixs", "AREA")

        config['model_pub'] = constants.get("Models", "PUB")
        config['model_review'] = constants.get("Models", "REVIEW")
        config['model_station'] = constants.get("Models", "STATION")
        config['model_area'] = constants.get("Models", "AREA")

        config['column_photo'] = constants.get("Columns", "PHOTO")
        config['column_all'] = constants.get("Columns", "ALL")
        config['column_pub'] = constants.get("Columns", "PUB")
        config['column_review'] = constants.get("Columns", "REVIEW")
        config['column_score'] = constants.get("Columns", "SCORE")
        config['column_required'] = constants.get("Columns", "REQUIRED")

        config['visible_pub'] = constants.get("Visibles", "PUB")
        config['visible_review'] = constants.get("Visibles", "REVIEW")

        config['control_date'] = constants.get("Controls", "DATE")
        config['control_input'] = constants.get("Controls", "INPUT")
        config['control_dropdown'] = constants.get("Controls", "DROPDOWN")
        config['control_slider'] = constants.get("Controls", "SLIDER")

        config['colour_all'] = constants.get("Colours", "ALL")
        config['colour_new'] = constants.get("Colours", "NEW")
        config['colour_reviewed'] = constants.get("Colours", "REVIEWED")
        config['colour_black'] = constants.get("Colours", "BLACK")
        config['colour_red'] = constants.get("Colours", "RED")
        config['colour_primary'] = constants.get("Colours", "PRIMARY")

        # with open(os.getcwd() + '/config.json') as file:  # Opening JSON file
        #     config_file = json.load(file)  # returns JSON object as a dictionary
        #     config['google_key'] = config_file['configs']['local_key']
        #     config['access_id'] = config_file['configs']['access_id']
        #     config['access_key'] = config_file['configs']['access_key']
        #     config['bucket_name'] = config_file['configs']['bucket_name']
        #     config['source'] = config_file['configs']['source']
        # else:
        config['google_key'] = os.getenv("HEROKU_GOOGLE_API")
        config['access_id'] = os.environ.get("ACCESS_ID")
        config['access_key'] = os.environ.get("ACCESS_KEY")
        config['bucket_name'] = os.environ.get("BUCKET_NAME")
        return config
