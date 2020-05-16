from core.const import DEVICE_CONFIG_MAP


class CommunicationEngine:
    """Handles all communication with the user, through the command-line interface.
    Deals with user input as well as program output."""

    def __init__(self):
        pass

    @staticmethod
    def quit(exit_message):
        print(exit_message)
        input("Press enter to quit...")
        exit(-1)

    @staticmethod
    def greet_setup():
        print("Welcome to setup!")

    @staticmethod
    def greet_main():
        print("Welcome to KompleteDarkness!")

    @staticmethod
    def success_setup():
        print("Setup was successful! You may now run the main program.")
        input("Press enter to quit...")

    @staticmethod
    def success_main():
        print("Main was successful! The lights should be off. If they're not, please submit an issue at "
              "https://github.com/EdwinVanRooij/komplete-darkness/issues.")
        input("Press enter to quit...")

    @staticmethod
    def get_device_name():
        names = list(DEVICE_CONFIG_MAP.keys())

        print("Which Native Instruments file will you use? Pick a number and press enter.")
        return CommunicationEngine.get_answer_from_string_options(names)

    @staticmethod
    def get_answer_from_string_options(strings):
        CommunicationEngine.print_options(strings)

        keyboard = input(">")
        # noinspection PyBroadException
        try:
            choice_number = int(keyboard)

            if choice_number < 1 or choice_number > len(strings):
                raise IndexError()
            actual_choice = strings[choice_number - 1]
            print(f"Chose \"{actual_choice}\".")
            return actual_choice
        except:
            print("Please choose any of the given options.")
            return CommunicationEngine.get_answer_from_string_options(strings)  # Restart method

    @staticmethod
    def print_options(song_files):
        for number, song_file in enumerate(song_files, start=1):
            print(f"[{number}]: {song_file}")
