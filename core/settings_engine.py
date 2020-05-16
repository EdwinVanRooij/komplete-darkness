import json

from core.classes import Config
from core.const import *

import os.path
from os import path


class SettingsEngine:
    """This engine will handle all settings-related tasks. For example, it can read a settings file for a song, and
    return a class instance for it."""

    @staticmethod
    def get_config():
        with open(CONFIG_FILEPATH) as json_file:
            data = json.load(json_file)
            settings = Config(
                data[KEY_MODE],
                data[KEY_INSTRUMENT_CODE],
                data[KEY_INSTRUMENT_ADDRESS],
                data[KEY_NUMBER_OF_KEYS],
                data[KEY_OFFSET]
            )
            return settings

    @staticmethod
    def write_config(config):
        """Saves a value to the cache."""
        SettingsEngine.create_if_not_exists()

        with open(CONFIG_FILEPATH) as f:
            data = json.load(f)
            data[KEY_MODE] = config.mode
            data[KEY_INSTRUMENT_CODE] = config.instrument_code
            data[KEY_INSTRUMENT_ADDRESS] = config.instrument_address
            data[KEY_NUMBER_OF_KEYS] = config.number_of_keys
            data[KEY_OFFSET] = config.offset
            json.dump(data, open(CONFIG_FILEPATH, "w+"), indent=4)

    @staticmethod
    def create_if_not_exists():
        """Creates a cache file if it doesn't exist yet."""
        if not path.exists(CONFIG_FILEPATH):
            with open(CONFIG_FILEPATH, 'w+') as file:
                file.write("{}")
