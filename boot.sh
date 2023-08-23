#!/bin/bash

set -e

# flyway  -configFiles="flyway/conf/flyway.conf" \
#      -url="jdbc:mysql://$DB_HOST:$DB_PORT/purchase_automation?allowPublicKeyRetrieval=true" \
#      -user="$DB_USER" \
#      -password="$DB_PASS" \
#      migrate

source venv/bin/activate
exec gunicorn -b 0.0.0.0:5000 -k gevent init_app:application --max-requests=1000 --timeout=300 --workers=5 --access-logfile='-' --access-logformat='%(h)s %(u)s [%(t)s] %(m)s "%(U)s" "%(q)s" %(H)s %(s)s %(B)s "%(f)s" "%(a)s" %(M)s msecs'