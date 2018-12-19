#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Zhe Zhang'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'zz',
        'password': 'Pass@word123',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}