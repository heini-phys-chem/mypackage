# .readthedocs.yaml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the version of Python and other tools you might need
# build:
#   os: ubuntu-22.04
#   tools:
#     python: "3.10"

mkdocs:
  configuration: mkdocs.yml

# Optionally declare the Python requirements required to build your docs
python:
    install:
        - method: pip
          path: .
          extra_requirements:
              - docs
