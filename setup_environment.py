###### Funciones de utilidad ######
import os
import configparser


def read_ini(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config


config = read_ini("config.ini")

def set_environment_variables() -> None:
    os.environ["OPENAI_API_KEY"] = str(config["LLM"]["OPENAI_API_KEY"])