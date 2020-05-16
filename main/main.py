from core.communication_engine import CommunicationEngine
from core.exception_engine import ExceptionEngine
from core.settings_engine import SettingsEngine
from core.keyboard_engine import KeyboardEngine


def main():
    """Main program flow."""
    print("Starting...")
    CommunicationEngine.greet_main()

    config = None
    try:
        config = SettingsEngine.get_config()
    except FileNotFoundError:
        CommunicationEngine.quit("Config file not found. Make sure to run the setup first!")

    keyboard_engine = KeyboardEngine(config)
    keyboard_engine.start()

    keyboard_engine.turn_off()
    CommunicationEngine.success_main()


if __name__ == "__main__":
    # Wrap the entire program execution by the exception engine.
    # This will prevent the program from crashing, and instead providing useful exception feedback to the user.
    ExceptionEngine.wrap(main)
