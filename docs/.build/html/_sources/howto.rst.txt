Howto
=====================================================

After cloning the repository it's important to set SYS variable located in the config.py.
That variable should be also present in the alarm server configuration file!

    .. code:: bash

	usage: startup.py [-h] [--start] [--stop]

	This script allows to build/stop all the containers. This script will work
	properly if the subsystem name matches the alarm server configuration file

	optional arguments:
  	-h, --help  show this help message and exit
  	--start     Start the containers
  	--stop      Stop the containers

	All is well that ends well.



Remember that all the service listed in the depends_on line will be deployed subsequently. That's why it's important to carefully choose the services you want to deploy.

Before deploying, you may also want to carefully check the repositories in which you want to store the db files. In this case, they will appear in the DCS folder.

The startup procedure may last up to a few minutes. If it is successful, you will see the screen below.

.. image:: Phoebus.png
    :scale: 30%
    :align: center
    :alt: alternate text
    

What's the purpose?
--------------------

