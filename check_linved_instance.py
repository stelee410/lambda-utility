from typing import Union
import fire
import os
import requests
from alert import alert

SERVER_URL = 'https://cloud.lambdalabs.com/'
API_GET_INSTANCES = SERVER_URL + 'api/v1/instances'
from typing import List, Dict, Union
import os
import requests

def main(api_key: Union[str, None] = None, receiver:Union[str, None] = None, proxy=None) -> None:
    # Get the API key from the environment variable
    if api_key is None and 'LAMBDA_API_KEY' in os.environ:
        api_key = os.environ['LAMBDA_API_KEY']
    if not api_key:
        raise ValueError('API key is missing or empty')
    # Get the list of instances from the API
    resp = requests.get(API_GET_INSTANCES, headers={'Authorization': 'Basic '+api_key}).json()
    if not 'data' in resp:
        raise ValueError('response does not contain data, this might be due to an invalid API key')
    instances = resp['data']
    if not instances:
        print('No instance found.')
        return
    else:
        print('Found {} instances.'.format(len(instances)))
        if receiver:
            message = 'Found {} instances running on lambda'.format(len(instances))
            if proxy:
                hostname, port_s = proxy.split(':')
                port = int(port_s)
                proxy_object = {'hostname': hostname, 'port': port}
            else:
                proxy_object = None
            alert(receiver, message, proxy_object)

if __name__ == '__main__':
    fire.Fire(main)
