# Pypgrest

A Python client for interacting with PostgREST APIs.

## Installation

```
$ pip install pypgrest
```

## Quick start

```python
>>> from pypgrest import Postgrest

>>> client = Postgrest("https://api.tacos.com", token="secretsalsa")

# See postgrest docs for supported query params
>>> params = {
        "select" : "name,tortilla,cost",
        "tortilla" : "is.corn",
        "limit" : 100,
        "order": "name"
    }

# Supported methods are select, insert, update, upsert, and delete
>>> client.select(resource="menu", params=params, pagination=True, headers=None)
# [{ "name" : "al pastor", "tortilla" : "corn", "cost" : "2.01" }, ... ]

>>> payload = [{ "id" : 23, "cost" : "2.25" }, { "id" : 26, "cost" : "1.25" }]

>>> pgrest.upsert(payload)
# [{ "id" : 23, "cost" : "2.25", "name" : "al pastor", ... }, ... ]

# You can inspect the response object at `self.res`:
>>> client.res.status_code
# 201
```

## Headers

The client is initialized with `Content-Type=application/json` and (if you supply a token) `Authorization` headers. You can supply additional headers on construction, or per request.

```python
>>> client = Postgrest(
    "https://api.tacos.com",
    token="secretsalsa", 
    headers={"Prefer": "return=representation"}
)

>>> client.headers
# {"Content-Type": 'application/json', 'Authorization': 'Bearer secretsalsa', 'Prefer': 'return=representation'}

>>> client.insert(
    resource="menu",
    data={"id": 5, "name": "barbacoa"},
    headers={"Prefer": "return=headers-only"}
)

```

## Limits and pagination

By default, the client will paginate requests until all records have been retrieved. You can supply a `limit` param to limit the number of results returned by `select`. 

You can disable pagination with `pagination=False`, in which case the record limit will be capped by your API's [`max-rows`](https://postgrest.org/en/v8.0/configuration.html#max-rows) setting. 

## Development

We use Github Actions to publish to PyPI. The workflows are defined in .github/workflows.

Any commit/merge to the dev branch will trigger a PyPI publication to the knackpy-dev package. Any *release* on the master branch will trigger publication to the knackpy package on PyPI. Note that PyPI publications will fail if don’t bump the version number in setup.py.


## License

As a work of the City of Austin, this project is in the public domain within the United States.

Additionally, we waive copyright and related rights of the work worldwide through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
