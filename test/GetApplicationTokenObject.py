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

app_scopes = ["https://api.ebay.com/oauth/api_scope", "https://api.ebay.com/oauth/api_scope/buy.item.feed"]
invalid_app_scopes = ["https://api.ebay.com/oauth/api_scope", "https://api.ebay.com/oauth/api_scope/sell.inventory"]

class TestGetApplicationTokenObject(unittest.TestCase):

    def _initoauthclient(self, scopes):
        return eBayOAuthClient(client_id=os.environ['CLIENT_ID'],
                               client_secret=os.environ['CLIENT_SECRET'],
                               dev_id=os.environ['DEV_ID'],
                               redirect_uri=os.environ['REDIRECT_URI'],
                               scopes=scopes, env=os.environ.get("API_ENV", "SANDBOX"))
        
    def test_invalid_oauth_scope(self):
        client = self._initoauthclient(invalid_app_scopes)
        try:
            app_token = client.get_application_token()
            self.assertIsNone(app_token['access_token'])
        except ValueError:
            print('\n *** test_invalid_oauth_scope ***\n')
    

    def test_client_credentials_grant(self):
        client = self._initoauthclient(app_scopes)
        app_token = client.get_application_token()
        self.assertIsNotNone(app_token['access_token'])
        self.assertTrue(len(app_token['access_token']) > 0)
        print('\n *** test_client_credentials_grant_sandbox ***:\n', app_token)



if __name__ == '__main__':
    unittest.main()
