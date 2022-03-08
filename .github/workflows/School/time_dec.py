import time
def time_checker(f):
    def timewrapper(*args, **kwargs):
        start = time.time()
        return_data = f(*args, **kwargs)
        end = time.time()
        print((end - start) * 1000, "ms")
        return return_data
    return timewrapper

@time_checker
def helloer():
    print("Helloer")
    print('I am saying hello.')

@time_checker
def make_joke():
    def joke():
        print('This is funny!!')
        print('You better laugh!!')
    return joke()


helloer()
make_joke()