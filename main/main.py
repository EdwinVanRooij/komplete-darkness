from core.communication_engine import CommunicationEngine
from core.exception_engine import ExceptionEngine
from core.settings_engine import SettingsEngine, CONFIG_FILEPATH


def main():
    """Main program flow."""
    print("Starting...")
    CommunicationEngine.greet()

    try:
        config = SettingsEngine.get_config(CONFIG_FILEPATH)
    except FileNotFoundError:
        CommunicationEngine.quit("Settings file not found. Make sure to run the setup first!")


if __name__ == "__main__":
    # Wrap the entire program execution by the exception engine.
    # This will prevent the program from crashing, and instead providing useful exception feedback to the user.
    ExceptionEngine.wrap(main)
