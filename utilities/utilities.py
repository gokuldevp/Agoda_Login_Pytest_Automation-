import random
import logging
import datetime
import os
from faker import Faker
import configparser


class ConfigUtil:
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__).replace('utilities\\', '')), 'configs', 'config.properties')
    
    def __init__(self, config_file=config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_agoda_url(self):
        return self.config['DEFAULT']['BASE_URL']

    def get_yopmail_url(self):
        return self.config['DEFAULT']['YOPMAIL_URL']

    def get_timeout(self):
        return self.config['DEFAULT'].getint('TIMEOUT')

config_util = ConfigUtil()

def generate_test_data():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name.lower()}.{last_name.lower()}@yopmail.com"
    return first_name,last_name,email

def get_current_date_time():
    """ Function to return datetime int YYMMDDHHmmSS format """
    current_datetime = str(datetime.datetime.now())[0:19]
    return datetime.datetime.strptime(current_datetime, '%Y-%m-%d %H:%M:%S').strftime('%Y%m%d%H%M%S')

def get_current_date():
    """ Function to return datetime int YYMMDDHHmmSS format """
    current_date = str(datetime.date.today().strftime("%Y_%m_%d"))
    return current_date


def loggen(): 
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__).replace('utilities\\', '')), 'logs', 'automation.log') 
    log_handler = logging.FileHandler(log_file) 
    log_handler.setFormatter( logging.Formatter("%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")) 
    logger = logging.getLogger() 
    logger.addHandler(log_handler) 
    logger.setLevel(logging.INFO) 
    return logger

class ScreeShots:
    def __init__(self, driver):
        self.driver = driver
    def take_screenshots_as_png(self,screenshot_name):
        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__).replace('utilities\\', '')),'Reports\\',datetime.date.today().strftime("%Y_%m_%d"))
        
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
        
        screenshot_name = "" + datetime.datetime.strptime(get_current_date_time(), '%Y%m%d%H%M%S').strftime('%d_%m_%Y_%H_%M_%S') + f"_{screenshot_name}" + ".png"
        screenshot_file = os.path.join(dir_path, screenshot_name)
        
        self.driver.save_screenshot(screenshot_file)

        re_path = screenshot_file.replace(os.path.dirname(os.path.abspath(__file__).replace('utilities\\', '')),"")
        return re_path
