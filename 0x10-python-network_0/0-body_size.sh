#!/bin/bash
# This script will print the size of the body of the response
curl -s "$1" | wc -c