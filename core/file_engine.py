import os
import json

from json import JSONDecodeError


class FileEngine:
    """Deals with all file related functionality."""

    @staticmethod
    def get_all_potential_song_files(json_filenames):
        """Returns a list of all json filenames that may potentially be song files, out of the given
        json filenames."""
        song_files = []

        for json_file in json_filenames:
            with open(json_file) as json_content:
                try:
                    data = json.load(json_content)
                    if KEY_COLOR_PALETTE in data \
                            or KEY_TOTAL_NUMBER_OF_NOTES in data \
                            or KEY_NOTES_PER_COLOR in data:
                        # Detected that one or more of the settings keys are present, so this is probably meant to be
                        # a settings file.
                        song_files.append(json_file)
                except JSONDecodeError:
                    FileEngine.on_incorrect_json(json_file)

        return song_files

    @staticmethod
    def get_all_potential_ni_files(json_filenames):
        """Returns a list of all json filenames that may potentially be NI files, out of the given
        json filenames."""
        ni_files = []

        for json_file in json_filenames:
            with open(json_file) as json_content:
                try:
                    data = json.load(json_content)
                    if KEY_NATIVE_INSTRUMENTS_CODE in data \
                            or KEY_INSTRUMENT_ADDRESS in data \
                            or KEY_NUMBER_OF_KEYS in data \
                            or KEY_OFFSET in data:
                        # Detected that one or more of the settings keys are present, so this is probably meant to be
                        # a NI file.
                        ni_files.append(json_file)
                except JSONDecodeError:
                    FileEngine.on_incorrect_json(json_file)

        return ni_files

    @staticmethod
    def get_all_potential_settings_files(json_filenames):
        """Returns a list of all json filenames that may potentially be settings files, out of the given
        json filenames."""
        settings_files = []

        for json_file in json_filenames:
            with open(json_file) as json_content:
                try:
                    data = json.load(json_content)
                    if KEY_BRIDGE_IP in data \
                            or KEY_DEVICE_INPUT_NAME in data \
                            or KEY_LIGHTS in data \
                            or KEY_SEQUENCES in data \
                            or KEY_BRIGHTNESS_MIN in data \
                            or KEY_BRIGHTNESS_MAX in data:
                        # Detected that one or more of the settings keys are present, so this is probably meant to be
                        # a settings file.
                        settings_files.append(json_file)
                except JSONDecodeError:
                    FileEngine.on_incorrect_json(json_file)

        return settings_files

    @staticmethod
    def get_all_json_files_in_directory(directory, recursively=True):
        """Gets all json files in a given directory, returning the filepath.
        Recursively defines whether or not to look in further subdirectories, will
        go one level deep if set to True."""
        filepaths = []

        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if filepath.endswith(".json"):
                # We found a json file, add it.
                filepaths.append(filepath)

            elif os.path.isdir(filepath):
                if recursively is True:
                    # We found a subdirectory, and we should look through it. Call this method again, but don't
                    # look through any more subdirectories.
                    filepaths.extend(FileEngine.get_all_json_files_in_directory(filepath, False))

        return filepaths

    @staticmethod
    def on_incorrect_json(filepath):
        from core import CommunicationEngine
        # Import it locally, because otherwise we'd get a recursive dependency loop.

        CommunicationEngine.quit(f"Could not read {filepath} as a JSON file. Make sure the file is "
                                 f"written in correct JSON format.")
