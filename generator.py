#def gen_generator():
#   yield 1

#def gen_value():
#    return 1
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b 

if __name__ == '__main__':
    ret = fib()
    print (next(ret))    #<generator object gen_generator at 0x02645648> <type 'generator'>
    print (next(ret))
    print (next(ret))
    print (next(ret))
    print (next(ret))
    print (next(ret))

