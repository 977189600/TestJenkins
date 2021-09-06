#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
@Time:2021/8/23 10:11 下午"
@Author:lydia_liu"
@File:httpclient.py
@function:
"""
import requests
import urllib3
import warnings

class HttpClient:
    """Generic Http Client class"""

    def __init__(self, disable_ssl_verify=False, timeout=60):
        """Initialize method"""

        self.client = requests.session()
        self.disable_ssl_verify = disable_ssl_verify
        self.timeout = timeout
        if self.disable_ssl_verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        warnings.simplefilter('ignore',ResourceWarning)


    def Get(self, url, headers=None, data=None, json=None, params=None, *args, **kwargs):
        """Http get method"""

        if headers is None:
            headers = {}

        if self.disable_ssl_verify:
            response = self.client.get(url, headers=headers, data=data, json=json, params=params
                                       , verify=False, timeout=self.timeout, *args, **kwargs)
        else:
            response = self.client.get(url, headers=headers, data=data, json=json, params=params
                                       , timeout=self.timeout, *args, **kwargs)
        response.encoding = 'utf-8'
        print(f'{response.json()}')

        return response