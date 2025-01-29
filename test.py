# x = 5

# def AbobaFunc(inp):
#     result = f"aboba function result is: {inp}"
#     print(result)
# AbobaFunc("input")
# print(x, "aboba", type(x), sep = ":")
# print("Hello, VS Code!")
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("here")
        if args:
            print(args[0])
        print(f"function name = {func.__name__}, *args = {args}, **kwargs = {kwargs}")
        out = func(*args, **kwargs)
        print(out.upper())
        print("Что-то делаем после вызова функции.")
        return "wrapper res"
    return wrapper

@my_decorator
def say_hello(last_name, name):
    return f"Hello {name} {last_name}"

print(say_hello("filia", "filia2"))


def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1


gen = natural_numbers()

for _ in range(5):
    print(next(gen))

squares = (x**2 for x in range(11))
print(next(squares))
