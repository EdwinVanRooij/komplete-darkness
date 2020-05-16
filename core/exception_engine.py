import sys
import traceback

from core.communication_engine import CommunicationEngine


class ExceptionEngine:

    @staticmethod
    def wrap(method):
        """Wraps execption of a method, catching all exceptions and providing useful information back to the
        user instead of quitting."""
        # noinspection PyBroadException
        try:
            method()
        except Exception:
            # Catch all exceptions, because we always want to show something.
            ex_type, ex_value, ex_traceback = sys.exc_info()
            trace_back = traceback.extract_tb(ex_traceback)  # Extract unformatter stack traces as tuples
            stack_trace = ""

            for trace in trace_back:
                filepath = trace[0]
                line = trace[1]
                type = trace[2]
                function = trace[3]
                stack_trace += f"{filepath}:{line} {type}.{function}\n"

            CommunicationEngine.quit(f"Unexpected error occurred.\n"
                                     f"Error: {ex_type}\n"
                                     f"Message: {ex_value}\n"
                                     f"Trace: {stack_trace}\n")
