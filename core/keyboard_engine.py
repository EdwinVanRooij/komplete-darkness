import hid

from core.communication_engine import CommunicationEngine
from core.const import MODE_MK2, MODE_MK1

key_initiate = [0xa0]  # Required to initiate / wake up the keyboard interface.

key_set_light_mk1 = [0x82]  # Means a new light state should be set.
key_set_light_mk2 = [0x81]

near_max_buffer_size = 249  # Leaves one spot open in the buffer.
empty_byte = [0x00]  # Defines an empty byte in a list.
empty_fillers = near_max_buffer_size * empty_byte  # Useful for empty fillers in a buffer.


class KeyboardEngine:
    """Handles all (low-level) operations with the actual USB keyboard(/MIDI controller)."""

    def __init__(self, config):
        self.config = config
        self.mode_key = None
        self.set_mode_key()

        self.device = None
        self.current_state = None  # Holds the current state of all keys.

    def set_mode_key(self):
        if self.config.mode == MODE_MK1:
            self.mode_key = key_set_light_mk1

        elif self.config.mode == MODE_MK2:
            self.mode_key = key_set_light_mk2

        else:
            CommunicationEngine.quit("Unknown mode key, must be MK1 or MK2.")

    def start(self):
        """Starts the engine."""

        # Open the keyboard device interface
        self.device = hid.device()
        self.device.open(0x17cc, 0x1620)
        # self.device.open(self.config.instrument_code, self.config.instrument_address)

        # Initiate / activate the interface.
        self.device.write(key_initiate)

        self.current_state = self.create_empty_buffer()  # Create an empty state
        self.current_state[0] = self.mode_key  # Tell the interface we want to set light states.

    def create_empty_buffer(self):
        """Creates an empty buffer."""
        return empty_byte * self.config.number_of_keys

    def turn_off(self):
        """Turns all keys off."""
        self.current_state = self.mode_key + empty_fillers
        self.update()

    def update(self):
        self.device.write(self.current_state)
