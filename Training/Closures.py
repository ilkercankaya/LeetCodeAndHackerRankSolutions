# below is an enclosure function
def Counter(x):
    message = "I am a closure"
    x += 10

    def _increment():
        nonlocal x
        x += 1
        print(x, message)

    return _increment


counter = Counter(0)
counter()
counter()
counter()


# below is an enclosure function
def make_printer(msg):
    def printer():
        print(msg)

    return printer


printer = make_printer('Foo!')
printer()


# below is a nested function
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    innerFunction()
