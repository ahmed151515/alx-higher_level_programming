#!/bin/bash
# This script will print the size of the body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
