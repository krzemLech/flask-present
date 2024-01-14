#!/bin/bash
exec gunicorn --config /app/gunicorn_config.py --access-logfile - run:app