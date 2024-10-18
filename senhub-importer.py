#!/usr/bin/python3
"""
.SYNOPSIS
    Requests SenHub API
.DESCRIPTION
    This sensor use the built in python libraries
    Output: 0 OK
            1 WARNING
            2 CRITICAL
            3 UNKNOWN
.PARAMETER
    URL : SenHub URL between ''
.NOTES
    1.1
        First version
        support@sensorfactory.eu
        29/09/2021
        Alexis
    1.2
        Check args 
        support@sensorfactory.eu
        19/10/2024
        Yann
"""
from urllib import request
import sys
def http_request(url):
    try:
        # Try to reach the endpoint given by the url
        result = (request.urlopen(url)).read()
        result = result.decode('utf-8')
    except Exception as e:
        # If something is wrong return an error message
        print(e)
        sys.exit(3)
    else:
        # if everything works fine check the status of the return string
        if result.startswith('OK'):
            print(result)
            sys.exit(0)
        elif result.startswith('CRITICAL'):
            print(result)
            sys.exit(2)
        elif result.startswith('UNKNOWN'):
            print(result)
            sys.exit(3)
        elif result.startswith('WARNING'):
            print(result)
            sys.exit(1)
        else:
            print(result)
            sys.exit(3)

try:
    if len(sys.argv) != 2:
        raise IndexError('Exactly one URL parameter is required')
    url = sys.argv[1]
    if not (url.startswith('http://') or url.startswith('https://')):
        raise ValueError('URL must start with http:// or https://')
    if 'senhub.io' not in url:
        raise ValueError('URL must contain senhub.io')
    if 'format=nagios' not in url:
        raise ValueError('URL must contain format=nagios')
    http_request(url)
except IndexError as e:
    # If no url is given or more than one argument is given, return an error
    print(e)
    sys.exit(2)
except ValueError as e:
    # If the URL does not meet the required conditions, return an error
    print(e)
    sys.exit(2)
except Exception as e:
    # If something else goes wrong, return an error message
    print(e)
    sys.exit(2)
