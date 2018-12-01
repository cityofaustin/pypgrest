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

# see postgrest docs for support query params
>>> params = {
        "select" : "name,tortilla,cost",
        "tortilla" : "is.corn",
        "limit" : 100
    }

>>> data = pgrest.select(params)

[{ "name" : "al pastor", "tortilla" : "corn", "cost" : "$2.00" }, ... ]

# you can inspect the `Requests` response object like so
>>> pgrest.res.status_code
200
```

## License

As a work of the City of Austin, this project is in the public domain within the United States.

Additionally, we waive copyright and related rights of the work worldwide through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
