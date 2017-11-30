#!/usr/bin/python3
#!__VENV_PYTHON__

def hello(msg):
    print('Hello, world!')
    print(msg)

def fib(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b

def init(msg):
    hello(msg)
    for i in range(10):
        print(fib(i))

if __name__ == "__main__":
    hello()
    for i in range(10):
        print(fib(i))