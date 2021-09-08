#!/usr/bin/python3
​
from urllib import request
import sys
import json
​
url = 'https://api.demo.sensorfactory.io/sensors/instances/a805eb0f-5aec-4864-a8c0-c30e0d47d60a/metrics?token=bda47654-4167-4cc1-9f9e-779c8dd17379'
def http_request(url):
    perf = str(' |')
    sta = str('OK:')
​
    try:
        # Try to reach the endpoint given by the url
        result = (request.urlopen(url)).read()
    except:
        # If something is wrong return an error message
        print('error')
        sys.exit(3) 
    else:
        # if everithing work fine return the content of the endpoint 
        result = result.decode('utf-8')
        result = json.loads(result)
        for i in result['metrics']:
            if isinstance((i['value']),int) or isinstance((i['value']),float):
                sta = sta +' '+i['channel']+'('+str(i['value'])+'),'
                perf = perf +" '"+i['channel']+"'="+str(i['value'])+","
            else:
                sta = sta +' '+i['channel']+'('+str(i['value'])+'),'
                perf = perf
        print(sta[:-1]+perf[:-1])
        sys.exit(0)  
​
​
​
http_request(url)




