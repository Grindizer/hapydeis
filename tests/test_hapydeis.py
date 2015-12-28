#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from click.testing import CliRunner
import pytest

from json import dumps
from hapydeis.__main__ import main
from hapydeis.hapydeis import DeisLevel0Client, DeisLevel0Exception
import httpretty

apps_list = {u'count': 4,
             u'next': None,
             u'previous': None,
             u'results': [{u'created': u'2015-12-17T16:28:27UTC',
               u'id': u'alfred',
               u'owner': u'admin',
               u'structure': {u'cmd': 1},
               u'updated': u'2015-12-17T17:33:04UTC',
               u'url': u'alfred.alpha.devops.hdmtech.net',
               u'uuid': u'2ca27703-c327-4f60-a2d6-d2de8053f235'},
              {u'created': u'2015-12-21T14:30:35UTC',
               u'id': u'doorman',
               u'owner': u'admin',
               u'structure': {u'cmd': 1},
               u'updated': u'2015-12-21T15:25:12UTC',
               u'url': u'doorman.alpha.devops.hdmtech.net',
               u'uuid': u'eaf3cab4-e0f7-46a1-a1b5-3f62ab25c915'},
              {u'created': u'2015-12-21T16:53:04UTC',
               u'id': u'rover',
               u'owner': u'admin',
               u'structure': {u'cmd': 1},
               u'updated': u'2015-12-21T17:27:40UTC',
               u'url': u'rover.alpha.devops.hdmtech.net',
               u'uuid': u'b1bf128c-f389-49a5-a353-06302b3552f0'},
              {u'created': u'2015-12-18T23:32:01UTC',
               u'id': u'seekui',
               u'owner': u'admin',
               u'structure': {u'cmd': 4},
               u'updated': u'2015-12-23T21:41:08UTC',
               u'url': u'seekui.alpha.devops.hdmtech.net',
               u'uuid': u'3810f798-5713-4a39-95d7-3742a84111da'}]}


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == 'Hapydeis main command line invoked.\n'
    assert result.exit_code == 0

@httpretty.activate
def test_hapydeis_auth_failed():
    httpretty.register_uri(httpretty.POST,
                           "http://deis/v1/auth/login/",
                           status=400,
                           body='{"non_field_errors": ["Unable to log in with provided credentials."]}')
    client = DeisLevel0Client('http://deis')
    with pytest.raises(DeisLevel0Exception) as excp:
        client.authenticate('nn', 'bb')

@httpretty.activate
def test_hapydeis_auth_success():
    httpretty.register_uri(httpretty.POST,
                           "http://deis/v1/auth/login/",
                           status=200,
                           body='{"token": "toto"}')
    client = DeisLevel0Client('http://deis')
    res = client.authenticate('cc', 'vv')
    assert 'token' in res

@httpretty.activate
def test_hapydeis_apps_list():
    httpretty.register_uri(httpretty.GET,
                           "http://deis/v1/apps/",
                           status=200,
                           body=dumps(apps_list))
    client = DeisLevel0Client('http://deis')
    res = client.apps.get()
    assert res == apps_list







