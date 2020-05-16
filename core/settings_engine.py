import json

from core.classes import Config
from core.const import *


class SettingsEngine:
    """This engine will handle all settings-related tasks. For example, it can read a settings file for a song, and
    return a class instance for it."""

    @staticmethod
    def get_config(filepath):
        with open(filepath) as json_file:
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
        # todo; implement
        pass

    @staticmethod
    def get_config_by_device_name(device_name):
        # todo; implement
        pass
