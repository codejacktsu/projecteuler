import time


def timer(func):
    """decorator: prints process runtime"""

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter() - start_time
        print(f"Finished {func.__name__!r} in {end_time:.4f} secs")
        return result
    return wrapper


class Memoize:
    def __init__(self, function):
        self.cache = {}
        self.function = function

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key in self.cache:
            print("memoized!")
            return self.cache[key]

        value = self.function(*args, **kwargs)
        print("key added: ", key, " ", value)
        self.cache[key] = value
        return value
