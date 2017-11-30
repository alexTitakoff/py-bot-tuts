#!/usr/bin/python3

import test_module

test_var = 'lalalla'

def init():
    print('test_main start')
    import test_module


init()

# Вызвали функцию из модуля
modules_test = test_module
modules_test.init(test_var)
