"""
Defines a collection of classes for working with
various APIs.
"""

import requests

from .. import settings

class APIModule(object):
    """
    Abstract class that defines a set of functions for interacting with an API
    """
    def __init__(self, api_key, endpoint_url, api_key_name='api_key'):
        """ All APIs must provide an api key and endpoint """
        self.api_key = api_key
        self.endpoint_url = endpoint_url

        # APIs vary in what they call the api key attribute for requests
        # so we save it as an attribute for the class
        self.api_key_name = api_key_name

    def send_get_request(self, data):
        """
        Sends a get request to the stored api endpoint

        All data to be passed with the request should be supplied
        as a dict passed in as the data parameter.

        Returns the response content and status code.
        """
        data[self.api_key_name] = self.api_key
        response = requests.get(self.endpoint_url, params=data)

        # Response.json() raises an exception on failure, need to guard for that
        return {'content': response.json(), 'status_code': response.status_code}

class CrunchbaseAPI(APIModule):
    """
    Class for interacting with the CrunchbaseAPI
    """
    def __init__(self):
        """ Invoke superclass constructor with crunchbase specific params """
        super(CrunchbaseAPI, self).__init__(settings.CRUNCHBASE_API_KEY, settings.CRUNCHBASE_URL, api_key_name='user_key')

    def get_company_info(self, company_name):
        """
        Queries the crunchbase API for info on the given company

        Right now this just spits back whether or not the company exists.
        Eventually, we can have it give back further information about a
        company that we want to save locally.
        """
        data = {'name': company_name, 'organization_type': 'company'}
        response = self.send_get_request(data)

        if response['status_code'] == 200:
            company_list = response['content']['data']['items']
            if company_list:
                # Grab the first company from the list. This'll be the most
                # likely candidate
                company = company_list[0]
                return {'exists': True, 'name': company['name']}
            else:
                # Assume company doesn't exist
                return {'exists': False}
        else:
            # We encountered an error - we should raise an exception and handle
            # it in the outer scope for error logging, but for now let's
            # just say the company doesn't exist
            return {'exists': False}
