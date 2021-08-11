#!/bin/sh

set -e 

#Defining colors 
RED='\033[0;31m'
NC='\033[0m'

echo "${RED}Building the DCS${NC}"
docker-compose -f docker-compose-aa.yml up -d || echo -en "n\Docker comepose failed to build the project\n\n"
echo "${RED}Configuring alarm-server${NC}"
sleep 10s
docker exec -t alarm-server sh -c 'cd alarm-server && ./alarm-server.sh -config '$1' -import config/'$2' -settings config/settings.ini' || { echo -en "\nAlarm server failed to start... shutting down\n\n" 1>&2; docker-compose -f docker-compose-aa.yml down;}
echo "${RED}Control System Studio is starting...${NC}"


