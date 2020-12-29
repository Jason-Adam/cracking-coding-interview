#!/usr/bin/env bash

set -e;

pyclean() {
    find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
}

pyclean;
