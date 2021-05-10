Detector Control System for mSTS (tested on Debian and Ubuntu)
===================================
This Detector Control System is deployed with usage of docker-compose (compose file format 3.7), which is a tool for defining and running multi-container Docker application. This application requires docker engine version 18.06.0+. 

DCS contains most essential blocks (containers) for proper operation of the certain experimental setup:

* Control System Studio (Phoebus)
* IOC(s)
* Redis database
* Archiver appliance
* Zookeeper
* Kafka
* Alarm server
* Alarm logger
* Elasticsearch 
* Kibana
* Save and Restore service (jmasar + postgresql)


Prerequisites 
------------

Docker installation
------------

To install Docker on your PC, follow instructions at Docker website [Get Docker for linux](https://docs.docker.com/install/linux/docker-ce/debian/) or simply check docker-installation directory.  

To install Docker Compose on your PC, follow instructions at Docker website [Get Docker Compose](https://docs.docker.com/compose/install/).

Available versions
------------
1. Based on Archive Appliance by Philipp Klaus and Redis database + Save and Restore service (jmasar service + postregsql database)

To run the second version:
```
docker-compose -f docker-compose-aa.yml up <choose-service-to-be-deployed>* 
```
Remember that all the service listed in the depends_on line will be deployed subsequently. 

Before deploying, you may want to carefully check the repositories in which you want to store the db files. 
### Run parameters 
Main repository should be located in the home directory ($HOME should be specified accordingly). 

Main repository can be also placed in any other directory, in which case it is necessary to modify the paths in the docker-compose.yaml file.



Alarm-server 

------------
To import your alarm-server configuration to the alarm-server container.


