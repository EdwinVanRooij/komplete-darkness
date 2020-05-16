from core.exception_engine import ExceptionEngine


def setup():
    """Main setup program flow."""
    print("Starting...")


if __name__ == "__main__":
    # Wrap the entire program execution by the exception engine.
    # This will prevent the program from crashing, and instead providing useful exception feedback to the user.
    ExceptionEngine.wrap(setup)
