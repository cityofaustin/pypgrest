import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypgrest",
    version="0.0.3",
    author="City of Austin",
    author_email="transportation.data@austintexas.gov",
    description="A python client for interacting with PostgREST APIs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cityofaustin/py-postgrest",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta", 
    ),
)

