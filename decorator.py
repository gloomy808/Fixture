def decorator_function(func):
    def wrapper():
        print('Start decorate function: {}'.format(func))
        func()
        print('Finish decoration')
    return wrapper

def decorator_with_args(s):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(s)
            func(s)
            return s
        return wrapper
    return actual_decorator

@decorator_function
def hw():
    print('Hello world!')

@decorator_with_args('skillfactory')
def hw2(s):
    print('Hello world!, {}!'.format(s))

if __name__ == '__main__':
    hw()
    hw2()