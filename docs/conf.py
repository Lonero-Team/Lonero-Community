python:
   version: 3.7
   install:
      - requirements: docs/requirements.txt
      - method: pip
        path: .
        extra_requirements:
            - docs
      - method: setuptools
        path: another/package
   system_packages: true
