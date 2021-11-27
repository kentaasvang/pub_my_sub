#!/bin/bash
uwsgi --socket 127.0.0.1:9091 --wsgi-file sub.py --master --processes 2 --threads 2
