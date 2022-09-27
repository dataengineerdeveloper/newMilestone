from urllib import request
from xmlrpc.client import FastUnmarshaller
import requests
from datetime import datetime

from formatting import format_msg


def send(name, website=None, verbose=False):
    if website != None:
        msg = format_msg(my_name=name)
        #send the message
    else:
        mesg =  format_msg(my_name=name)
    if verbose:
        print(name,website)
    r=requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return "there was an error"
    
response = send ("justin",  verbose = True)
print(response)
if __name__ == "__main__":
    pass

