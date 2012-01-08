web: python app/manage.py run_gunicorn -b 0.0.0.0:$PORT -w 3 --worker-class=eventlet
worker:   python app/manage.py celeryd -E -B --loglevel=INFO
beat:     python app/manage.py celerybeat -S djcelery.schedulers.DatabaseScheduler --loglevel=INFO
