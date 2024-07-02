#!/bin/bash

cd myproject
PYTHONPATH=. uwsgi --ini ../uwsgi.ini
