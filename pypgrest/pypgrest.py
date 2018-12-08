"""
A Python client for interacting with PostgREST APIs.
"""
from copy import deepcopy

import requests


class Postgrest(object):
    """
    Class to interact with PostgREST.
    """
    def __init__(self, url, auth=None):

        self.auth = auth
        self.url = url

        self.headers = {
            "Content-Type": "application/json",
            "Prefer": "return=representation",  # return entire record json in response
        }

        if self.auth:
            self.headers["Authorization"] = f"Bearer {self.auth}"
        

    def insert(self, data=None):
        self.res = requests.post(self.url, headers=self.headers, json=data)
        self.res.raise_for_status()
        return self.res.json()


    def update(self, params=None, data=None):
        """
        This method is dangerous! It is possible to delete and modify records
        en masse. Read the PostgREST docs.
        """
        self.res = requests.patch(self.url, headers=self.headers, params=params, json=data)
        self.res.raise_for_status()
        return self.res.json()


    def upsert(self, data=None):
        """
        This method is dangerous! It is possible to delete and modify records
        en masse. Read the PostgREST docs.
        """
        headers = deepcopy(self.headers)
        headers["Prefer"] += ", resolution=merge-duplicates"
        self.res = requests.post(self.url, headers=headers, json=data)
        self.res.raise_for_status()
        return self.res.json()


    def delete(self, params=None):
        """
        This method is dangerous! It is possible to delete and modify records
        en masse. Read the PostgREST docs.
        """
        if not params:
            raise Exception("You must supply parameters with delete requests. This is for your own protection.")

        url = f"{self.url}"
        self.res = requests.delete(self.url, params=params, headers=self.headers)
        self.res.raise_for_status()
        return self.res.json()


    def select(self, params=None, increment=1000, pagination=True):
        """Select records from PostgREST DB. See documentation for horizontal
        and vertical filtering at http://postgrest.org/.
        
        Args:
            params (string): PostgREST-compliant request parametrs.

            increment (int, optional): The maximum number of records to
                return request per request. This is applied as a "limit" to
                each API request, until the user-specified limit is reached.
                
                Note that the PosgrREST DB itself will likely have limiting
                configured that cannot be exceeded. For example, our
                instances have a limit of 10000 records per request.

            pagination:
                If the client make multipel requets, returning multiple pages of
                results, buy using the `offest` param
        
        Returns:
            TYPE: List 
        """
        limit = params.setdefault('limit', 1000)

        params['limit'] = increment

        params.setdefault('offset', 0)

        records = []

        while True:
            self.res = requests.get(self.url, params=params, headers=self.headers)

            self.res.raise_for_status()

            records += self.res.json()

            if not self.res.json() or len(records) >= limit or not pagination:
                return records
            else:
                params['offset'] += len(self.res.json())