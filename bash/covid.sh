#!/bin/bash

# this script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)

POSITIVE=$(echo $DATA | jq '.[0].positive')
CUR_HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalizedCurrently')
CUR_INICU=$(echo $DATA | jq '.[0].inIcuCurrently')
DEATHS=$(echo $DATA | jq '.[0].death')

TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $CUR_HOSPITALIZED people currently hospitalized, $CUR_INICU in ICU and $DEATHS deaths."


