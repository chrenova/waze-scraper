#!/bin/bash

echo "1"
export WAZE_HOME=~/dev/waze-scraper/
echo $WAZE_HOME

cd $WAZE_HOME
source .venv/bin/activate

python -m waze_scraper
