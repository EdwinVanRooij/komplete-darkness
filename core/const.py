from core.classes import Config

CONFIG_FILEPATH = "config.json"

# Config file keys
KEY_MODE = "mode"
KEY_INSTRUMENT_CODE = "instrument_code"
KEY_INSTRUMENT_ADDRESS = "instrument_address"
KEY_NUMBER_OF_KEYS = "number_of_keys"
KEY_OFFSET = "offset"

# All devices, mapped by their name which the user should understand.
NATIVE_INSTRUMENTS = 0x17cc
MODE_MK1 = "MK1"
MODE_MK2 = "MK2"
DEVICE_CONFIG_MAP = {
    "Komplete Kontrol S61 MK2": Config(mode=MODE_MK2, instrument_code=NATIVE_INSTRUMENTS, instrument_address=0x1620,
                                       number_of_keys=61, offset=-36),
    "Komplete Kontrol S88 MK2": Config(mode=MODE_MK2, instrument_code=NATIVE_INSTRUMENTS, instrument_address=0x1630,
                                       number_of_keys=88, offset=-36),
    "Komplete Kontrol S49 MK2": Config(mode=MODE_MK2, instrument_code=NATIVE_INSTRUMENTS, instrument_address=0x1610,
                                       number_of_keys=49, offset=-36),
    "Komplete Kontrol S61 MK1": Config(mode=MODE_MK1, instrument_code=NATIVE_INSTRUMENTS, instrument_address=0x1360,
                                       number_of_keys=61, offset=-36),
    "Komplete Kontrol S88 MK1": Config(mode=MODE_MK1, instrument_code=NATIVE_INSTRUMENTS, instrument_address=0x1410,
                                       number_of_keys=88, offset=-21),
    "Komplete Kontrol S49 MK1": Config(mode=MODE_MK1, instrument_code=NATIVE_INSTRUMENTS, instrument_address=0x1350,
                                       number_of_keys=49, offset=-21),
    "Komplete Kontrol S25 MK1": Config(mode=MODE_MK1, instrument_code=NATIVE_INSTRUMENTS, instrument_address=0x1340,
                                       number_of_keys=25, offset=-21),
}
