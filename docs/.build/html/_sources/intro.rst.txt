Example of a Compose your services
=====================================================
Compose your services is deployed with use of docker-compose (compose file format 3.7), which is a tool for defining and running multi-container Docker application. This application requires docker engine version 18.06.0+. 

This example contains most essential blocks (containers) for proper operation of an experimental setup:

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
--------------

To install Docker on your PC (e.g. Debian), follow instructions at Docker website docker-website_.

    .. _docker-website: https://docs.docker.com/install/linux/docker-ce/debian/
    
To install Docker Compose on your PC, follow instructions at Docker website docker-compose_. 

    .. _docker-compose: https://docs.docker.com/compose/install/

What is the purpose?
------------------------------

This example should serve to show feasibility of using docker and docker-compose for control systems and its practicality. This set of applications has been used in many experimental setups in GSI. There are several advantages of containarizing those applications:

    * user can easily choose which services should be deployed, therefore, it might be useful for small, as well as, bigger experimental setups
    * configuration is very easy, especially if only few services are used



Issues
------------------------------




