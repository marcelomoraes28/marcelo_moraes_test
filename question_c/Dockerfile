FROM python:3.6.6
LABEL maintainer 'Marcelo Moraes <marcelomoraesjr28 at gmail.com>'
RUN mkdir src
COPY README.md setup.py pytest.ini __init__.py /src/
COPY cache /src/cache
COPY tests /src/tests
RUN ls -l /src/tests
RUN pip3 install -e /src/.[test]

WORKDIR /src

