#!/bin/sh

echo "{\"endpoint\": \"$ENDPOINT\"}" > endpoint.json
# python -m SimpleHTTPServer
python cors_server.py
