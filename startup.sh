#!/bin/sh

set -e 


#Defining colors 
RED='\033[0;31m'
NC='\033[0m'



echo "${RED}Building the DCS${NC}"
docker-compose -f docker-compose-aa.yml up -d 
echo "${RED}Configuring alarm-server${NC}"
docker exec -t alarm-server sh -c 'cd alarm-server && ./alarm-server.sh -config '$1' -import config/'$2''
echo "${RED}Control System Studio is starting...${NC}"


