#! /usr/bin/env sh
set -e

export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.6/site-packages:/usr/lib/python3.6/site-packages
export SECRET_KEY=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

exec "$@"
