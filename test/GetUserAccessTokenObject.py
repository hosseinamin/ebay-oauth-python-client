# -*- coding: utf-8 -*-
"""
Copyright 2019 eBay Inc.
 
Licensed under the Apache License, Version 2.0 (the "License");
You may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,

WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and
limitations under the License.

"""
from __future__ import print_function
import os, sys
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))
from ebayoauthclient import eBayOAuthClient
import unittest
import TestUtil

app_scopes = ["https://api.ebay.com/oauth/api_scope", "https://api.ebay.com/oauth/api_scope/sell.inventory", "https://api.ebay.com/oauth/api_scope/sell.marketing", "https://api.ebay.com/oauth/api_scope/sell.account", "https://api.ebay.com/oauth/api_scope/sell.fulfillment"]

class TestGetUserAccessTokenObject(unittest.TestCase):

    def _initoauthclient(self, scopes):
        return eBayOAuthClient(client_id=os.environ['CLIENT_ID'],
                               client_secret=os.environ['CLIENT_SECRET'],
                               dev_id=os.environ['DEV_ID'],
                               redirect_uri=os.environ['REDIRECT_URI'],
                               scopes=scopes, env=os.environ.get('API_ENV', 'SANDBOX'))
        
    def test_generate_authorization_url(self):
        client = self._initoauthclient(app_scopes)
        signin_url = client.generate_user_authorization_url()
        self.assertIsNotNone(signin_url)
        print('\n *** test_get_signin_url ***: \n', signin_url)

    def test_exchange_authorization_code(self):
        client = self._initoauthclient(app_scopes)
        signin_url = client.generate_user_authorization_url()
        code = TestUtil.get_authorization_code_for_user(signin_url, os.environ['LOGIN_USERNAME'], os.environ['LOGIN_PASSWORD'])
        user_token = client.exchange_code_for_access_token(code)
        self.assertIsNotNone(user_token['access_token'])
        self.assertTrue(len(user_token['access_token']) > 0)
        print('\n *** test_get_user_access_token ***:\n', user_token)

    def test_exchange_refresh_for_access_token(self):
        client = self._initoauthclient(app_scopes)
        signin_url = client.generate_user_authorization_url()
        code = TestUtil.get_authorization_code_for_user(signin_url, os.environ['LOGIN_USERNAME'], os.environ['LOGIN_PASSWORD'])
        user_token = oauth2api_inst.exchange_code_for_access_token(code)
        self.assertIsNotNone(user_token['refresh_token'])
        self.assertTrue(len(user_token['refresh_token']) > 0)

        user_token = client.get_access_token(user_token['refresh_token'])
        self.assertIsNotNone(user_token['access_token'])
        self.assertTrue(len(user_token['access_token']) > 0)

        print('\n *** test_refresh_user_access_token ***:\n', user_token)

if __name__ == '__main__':
    unittest.main()
