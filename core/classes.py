class Config:
    """Holds all config settings."""

    def __init__(self, mode, instrument_code, instrument_address, number_of_keys, offset):
        self.mode = mode
        self.instrument_code = instrument_code
        self.instrument_address = instrument_address
        self.number_of_keys = number_of_keys
        self.offset = offset
