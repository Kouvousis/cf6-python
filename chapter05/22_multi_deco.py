import time

def log_calls(func):
    """
    A decorator that logs the function call
    """
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__} with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper


def measure_time(func):
    """
    A decorator that measure the execution time for the function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution time of '{func.__name__}': {end_time - start_time}")
        return result
    return wrapper

@log_calls
@measure_time
def say_hello(name):
    time.sleep(1)
    return f"Hello {name}"

def main():
    print(say_hello("Jim"))
    print(say_hello("John"))

if __name__ == "__main__":
    main()
    
