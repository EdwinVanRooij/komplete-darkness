from core.communication_engine import CommunicationEngine
from core.exception_engine import ExceptionEngine
from core.settings_engine import SettingsEngine


def setup():
    """Main setup program flow."""
    # Greet the user.
    CommunicationEngine.greet()

    # Make the user choose their device name.
    device_name = CommunicationEngine.get_device_name()

    # Retrieve the config settings for that specific device.
    config = SettingsEngine.get_config_by_device_name(device_name)

    # Write those config settings to a file.
    SettingsEngine.write_config(config)

    # All went well, quit the program.
    CommunicationEngine.success()
    input("Press enter to quit...")
    exit(0)


if __name__ == "__main__":
    # Wrap the entire program execution by the exception engine.
    # This will prevent the program from crashing, and instead providing useful exception feedback to the user.
    ExceptionEngine.wrap(setup)
