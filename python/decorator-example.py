def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

def lxyz(func):
    def wrapper(*args, **kwargs):
        print(f"lxyz Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"lxyz {func.__name__} returned: {result}")
        return result
    return wrapper

@log_function
@lxyz
def add(a, b):
    return a + b

result = add(3, 5)
