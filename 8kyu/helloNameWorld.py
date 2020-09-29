def hello(name=None):
    if name == "" or name is None:
        return "Hello, World!"
    else:
        return f"Hello, {name.lower().capitalize()}!"

print(hello("ALIce"))
print(hello())