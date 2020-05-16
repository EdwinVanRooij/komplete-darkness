from core.exception_engine import ExceptionEngine


def main():
    """Main program flow."""
    print("Starting...")
    raise IndexError("Some index thing")


if __name__ == "__main__":
    # Wrap the entire program execution by the exception engine.
    # This will prevent the program from crashing, and instead providing useful exception feedback to the user.
    ExceptionEngine.wrap(main)
