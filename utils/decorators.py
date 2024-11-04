import logging


def log_function_status(func):
    """Decorator that prints the name of the function being called."""

    def wrapper(*args, **kwargs):
        logging.info(f"Started: {func.__name__}")
        result = func(*args, **kwargs)  # Call the original function
        logging.info(f"Ended: {func.__name__}")
        return result  # Return the actual output of the function

    return wrapper