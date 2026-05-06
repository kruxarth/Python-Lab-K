def say_hello():
    print("Hello, User!")

say_hello()

def sum_two(p, q):
    return p + q

print("Sum:", sum_two(5, 3))

def exponent(base, exp=2):
    return base ** exp

print("Square:", exponent(4))
print("Cube:", exponent(4, 3))

def add_many(*items):
    result = sum(items)
    return result

print("Sum of multiple values:", add_many(1, 2, 3, 4, 5))

def show_data(**data):
    for k, v in data.items():
        print(k, ":", v)

show_data(name="Alice", age=20, city="Delhi")

square_fn = lambda n: n ** 2
print("Square using lambda:", square_fn(5))

add_fn = lambda m, n: m + n
print("Addition using lambda:", add_fn(3, 7))