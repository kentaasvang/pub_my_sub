#!/bin/bash
uwsgi --socket 127.0.0.1:9090 --wsgi-file pub.py --master --processes 2 --threads 2
