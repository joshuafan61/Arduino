#!/bin/bash

API="o.vg88Lst6oLWVJIyOmsoH7SfKhoeEM7Wj"
MSG="$1"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="Message from pi" -d body="$MSG"