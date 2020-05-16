from core.file_engine import FileEngine


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
    def greet():
        print("Welcome to setup!")

    @staticmethod
    def success():
        print("Setup was successful! You may now run the main program.")

    @staticmethod
    def get_device_name():
        names = [
            "Komplete Kontrol S61 MK2",
            "Komplete Kontrol S88 MK2",
            "Komplete Kontrol S49 MK2",
            "Komplete Kontrol S61 MK1",
            "Komplete Kontrol S88 MK1",
            "Komplete Kontrol S49 MK1",
            "Komplete Kontrol S25 MK1",
        ]

        print("Which Native Instruments file will you use? Pick a number and press enter.")
        return CommunicationEngine.get_answer_from_string_options(names)

    @staticmethod
    def get_answer_from_string_options(strings, ):
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
