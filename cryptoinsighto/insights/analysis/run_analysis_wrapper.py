from functools import wraps
import time
import logging


# A wrapper for the analysis functions
# The purpose of this wrapper is to
# 1. load the input data for the functions
# 2. log the compute function
# 3. forward the results (for now it just prints it)
def run_analysis(analysis_name):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            print(f"Running analysis: {analysis_name}")
            result = func(*args, **kwargs)
            # TODO: actual forwarding of the result to a queue
            print(f"Function {analysis_name} produced the result {result}")

            print(f"Function {analysis_name} completed")
            return result

        return wrapper

    return decorator
