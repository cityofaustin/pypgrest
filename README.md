# Pypgrest
A python client for interacting with PostgREST APIs.

## Installation
```
$ pip install pypgrest
```

## Usage
```python
>>> from pypgrest import Postgrest

>>> pgrest = Postgrest("https://api.tacos.com", auth="secretsalsa")

# See postgrest docs for supported query params
>>> params = {
        "select" : "name,tortilla,cost",
        "tortilla" : "is.corn",
        "limit" : 100
    }

# Supported methods are select, insert, update, and upsert
>>> pgrest.select(params=params)
[{ "name" : "al pastor", "tortilla" : "corn", "cost" : "2.01" }, ... ]

>>> payload = [{ "id" : 23, "cost" : "2.25" }, { "id" : 26, "cost" : "1.25" }]

>>> pgrest.upsert(payload)
[{ "id" : 23, "cost" : "2.25", "name" : "al pastor", ... }, ... ]

# You can inspect the `Requests` response object like so:
>>> pgrest.res.status_code
201

# If results are paginated the client will continue to request until the specified
# limit (default 1000) is met.
>>> pgrest.select(params={"limit" : 1000})
```

## License

As a work of the City of Austin, this project is in the public domain within the United States.

Additionally, we waive copyright and related rights of the work worldwide through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
