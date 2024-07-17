#!/bin/bash

curl -X POST \
  https://gscmu7yix8.execute-api.eu-west-2.amazonaws.com/prod/compare \
  -H 'Content-Type: application/json' \
  -d '{
    "sourceImageKey": "kunmi-nin-1.jpeg",
    "targetImageKey": "kunmi-selfie.jpeg"
  }'
