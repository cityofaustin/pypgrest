import sys
import setuptools


def get_env(args):
    """If args contain `pypi-dev`, the package name will be `pypgrest-dev`. Else the
    package name will be pypgrest."""
    try:
        # test if our custom arg is present and delete it so that setuptools doesn't
        # throw an error
        args.remove("pypi-dev")
        return "dev"
    except ValueError:
        return "prod"


def get_package_name(env):
    if env == "dev":
        return "pypgrest-dev"
    else:
        return "pypgrest"


def build_config(env, readme="README.md"):
    package_name = get_package_name(env)

    with open(readme, "r") as fh:
        long_description = fh.read()

    return {
        "author": "John Clary",
        "author_email": "transportation.data@austintexas.gov",
        "classifiers": [
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: Public Domain",
            "Programming Language :: Python :: 3",
        ],
        "description": "A Python API client for interacting with PostgREST applications.",
        "long_description": long_description,
        "long_description_content_type": "text/markdown",
        "install_requires": ["requests"],
        "keywords": "postgres postgrest api api-client integration python",
        "license": "Public Domain",
        "name": package_name,
        "packages": setuptools.find_packages(),
        "url": "http://github.com/cityofaustin/pypgrest",
        "version": "0.1.0",
    }


if __name__ == "__main__":
    env = get_env(sys.argv)
    config = build_config(env)
    setuptools.setup(**config)
