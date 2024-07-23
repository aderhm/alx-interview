#!/usr/bin/python3
"""
Module: UTF-8 Validator
"""


def validUTF8(data):
    """Checks if a given data set represents a valid UTF-8 encoding.
    """
    byte_data = [i & 0xFF for i in data]
    try:
        byte_data = bytes(byte_data)
        byte_data.decode('utf-8')
    except UnicodeDecodeError:
        return False
    return True
