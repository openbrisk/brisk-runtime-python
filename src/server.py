#!/usr/bin/env python

import logging
import sys
import imp
import os

from flask import Flask, request, abort, g

app = Flask(__name__)

@app.route('/healthz', methods=['GET'])
def healthz():
    return "", 200, { 'Content-Type': 'text/plain' }

def configure_logging(logLevel):
    global app
    root = logging.getLogger()
    root.setLevel(logLevel)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logLevel)
    ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    app.logger.addHandler(ch)

configure_logging(logging.DEBUG)
app.logger.info("Listening port 8080 ...")
app.run(host='0.0.0.0', port=8080)