# -*- coding: utf-8 -*-
# This module contains settings for Celery

## Broker settings.
broker_url = 'redis://localhost:6379'

# List of modules to import when the Celery worker starts.
include = ['celery_tasks']

## Using the database to store task state and results.
result_backend = 'redis://localhost:6379'
