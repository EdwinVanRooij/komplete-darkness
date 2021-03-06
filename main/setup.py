from core.communication_engine import CommunicationEngine
from core.exception_engine import ExceptionEngine
from core.settings_engine import SettingsEngine, DEVICE_CONFIG_MAP


def setup():
    """Main setup program flow."""
    # Greet the user.
    CommunicationEngine.greet_setup()

    # Make the user choose their device name.
    device_name = CommunicationEngine.get_device_name()

    # Retrieve the config settings for that specific device.
    config = DEVICE_CONFIG_MAP[device_name]

    # Write those config settings to a file.
    SettingsEngine.write_config(config)

    # All went well, quit the program.
    CommunicationEngine.success_setup()


if __name__ == "__main__":
    # Wrap the entire program execution by the exception engine.
    # This will prevent the program from crashing, and instead providing useful exception feedback to the user.
    ExceptionEngine.wrap(setup)
