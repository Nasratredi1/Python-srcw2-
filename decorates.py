def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the Function.")
    return wrapper
        

@announce
def hello():
    print ("Hello, world!")

hello()

# decorate take a function and add capability to it.