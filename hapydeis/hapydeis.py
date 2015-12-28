#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from urlparse import urljoin
from os import path as ospath


class DeisLevel0Exception(Exception):
    pass


class DeisLevel0Client(object):
    def __init__(self, endpoint, version='v1', base_path='', token=None, s=requests.Session()):
        self.version = version
        self.endpoint = endpoint
        self.base_path = base_path
        self.path = urljoin(urljoin(self.endpoint, self.version + '/'), self.base_path)
        self.token = token
        self.s = s

    def authenticate(self, user, pwd):
        resp = self.auth.login.create(username=user, password=pwd)
        self.token = resp['token']
        return resp

    def _do_request(self, method, **args):
        headers = {}
        if self.token:
            headers = {'Authorization': "token {0}".format(self.token)}

        _do = getattr(self.s, method, 'get')
        response = _do(self.path, headers=headers, json=args)
        if response.status_code > 299:
            raise DeisLevel0Exception(response.text)
        return (response.text and response.json()) or '{}'

    def get(self):
        return self._do_request('get')

    def create(self, **args):
        return self._do_request('post', **args)

    def __getattr__(self, name):
        return DeisLevel0Client(
            self.endpoint,
            self.version,
            ospath.join(self.base_path, name) + '/',
            self.token,
            self.s
        )
