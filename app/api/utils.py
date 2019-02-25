# coding:utf-8
import hashlib
import random
import string

from flask import jsonify


def random_string_generator(size=7, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_key(url):
    key = random_string_generator()
    return key


def respond201(url):
    ''' 
    response for 'Created' 
    '''
    response = jsonify()
    response.status_code = 201
    response.headers['location'] = url
    return response


def respond404():
    ''' 
    response for 'Not found' 
    '''
    response = jsonify()
    response.status_code = 404
    return response
    

def respond422():
    ''' response for 'Unprocessable Entity' '''
    response = jsonify()
    response.status_code = 422
    return response
