# Compose your services 
These services are  deployed using docker-compose (compose file format 3.7), which is a tool for defining and running multi-container Docker application. This application requires docker engine version 18.06.0+. 

This example contains most essential blocks (containers) for proper operation of the certain experimental setup:

* Control System Studio (Phoebus)
* Example IOC
* Redis database
* Archiver appliance
* Zookeeper
* Kafka
* Alarm server
* Alarm logger
* Elasticsearch 
* Kibana
* Save and Restore service (jmasar + postgresql)


## Prerequisites 

### Docker installation


To install Docker on your PC, follow instructions at Docker website [Get Docker for linux](https://docs.docker.com/install/linux/docker-ce/debian/) or simply check docker-installation directory.  

To install Docker Compose on your PC, follow instructions at Docker website [Get Docker Compose](https://docs.docker.com/compose/install/).

Docker compose is included in the latest version of Docker Engine.
### Howto

Go to the documentation to see how to start this example.

```
usage: startup.py [-h] [--start] [--stop] [--ioc] [--archiver] [--log [LOG]]

This script allows to build/stop all the containers. This script will work
properly if the subsystem name matches the alarm server configuration file

optional arguments:
  -h, --help   show this help message and exit
  --start      Start the containers
  --stop       Stop the containers
  --ioc        Start the IOC
  --archiver   Start the archiver
  --log [LOG]  Specify the service name (not the container name)

All is well that ends well.
```





