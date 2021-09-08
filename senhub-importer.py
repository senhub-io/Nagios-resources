#!/usr/bin/python3
"""
.SYNOPSIS
    Request SenHub API
.DESCRIPTION
    This sensor use the built in python libraries
    Output: 0 Service OK
            2 Critical
            3 Unknown
.PARAMETER 
    URL : SenHub URL between ''
​
.NOTES       
    1.0
		First version
        support@senhub.io
        13/08/2021
        Alexis
"""
​
from urllib import request
import sys
​
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
        # if everithing work fine check the status of the return string 
        if result[0:2] == 'OK':
            print(result)
            sys.exit(0)  
​
        elif result[0:2] == 'KO':
            print(result)
            sys.exit(2)
​
        else:
            print(result)
            sys.exit(3)
​
        
try:
    http_request(sys.argv[1])
except IndexError:
    # If no url is given return an error
        print('Wrong or no parameter')
        sys.exit(3)
except Exception as e:
        # If something is wrong return an error message
        print(e)
        sys.exit(3) 
