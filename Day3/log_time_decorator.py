
import time


def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        total = (end - start) * 1000

        print(f"The Function took {total:.2f} ms")
        with open("execution_log.txt", 'a') as file:
            file.write(f"{func.__name__} took {total} ms\n")
        return result
    return wrapper

  