import os
import pandas as pd
from functions.functions import Functions
from config import Configurations

config = Configurations().get_config()


class Dataframes:

    def merge_to_csv(self, _get, new_df, key):

        df_appended = pd.concat([_get, pd.DataFrame([new_df.__dict__])], ignore_index=True)
        df_appended.to_csv(os.getcwd() + '/files/' + config[key]['aws_key'], sep=',', encoding='utf-8', index=False)

    def to_csv(self, df_appended, key):
        df_appended.to_csv(os.getcwd() + '/files/' + config[key]['aws_key'], sep=',', encoding='utf-8', index=False)

        # Functions().get_s3_pubs().to_csv(os.getcwd() + '/files/' + config['pub']['aws_key'], sep=',', encoding='utf-8',
        #                                  index=False)
