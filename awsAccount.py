# Date:   03/08/2015
# Author: Long Chen
# Description: A class to get aws access key and secret of an AWS account

import os
import configparser


class awsAccount:
    _aws_access_key_id = None 
    _aws_secret_access_key = None

    def __init__(self, account):
        base_path = os.path.dirname(os.path.realpath(__file__))
        CRED = base_path + '/conf/awscred'
        Config = configparser.ConfigParser()
        # Read configuration file
        Config.read(CRED)
        dict = {}
        # Read account profile section in the file
        options = Config.options(account)
        # Read configuration optons in the account section
        for option in options:
           try:
                dict[option] = Config.get(account, option)
                if dict[option] == -1:
                    print("skip: %s" % option)
           except:
                print("exception on %s!" % option)
                dict[option] = None
        # Store the access key data to the class
        self._aws_access_key_id = dict['aws_access_key_id']
        self._aws_secret_access_key = dict['aws_secret_access_key']
