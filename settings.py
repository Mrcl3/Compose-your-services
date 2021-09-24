import subprocess
import config
import time
import sys

def create_files():
    #Creates the settings.ini for Phoebus, alarm server and .env based on the config.py
    phoebus = open("config/Phoebus/settings.ini", "w")
    phoebus_list = [config.welcome, config.addr_list, config.urls, config.archives, config.use_default_archives, config.mailhost, config.server, config.config_name, config.config_names, config.threshold, config.nag_period, config.retention_count, config.es_host, config.es_port, config.es_index, config.es_max_size, config.es_sniff, config.jmasarurl, config.readtimeout, config.connecttimeout, config.split, config.sort, config.splitsave, config.enableCSVIO]
    phoebus.writelines(phoebus_list)
    phoebus.close()
    # Alarm server settings
    alarm = open("config/Alarmconfig/settings.ini", "w")
    alarm_list = [config.mailhost, config.port, config.server, config.config_name, config.config_names, config.email_sender, config.threshold, config.nag_period, config.retention_count]
    alarm.writelines(alarm_list)
    alarm.close()
    # .env file
    env = open(".env", "w")
    env_list = [ config.PATH, config.HOST, config.SUBSYSTEM, config.IOC, config.IOCp]
    env.writelines(env_list)
    env.close()

# Build all the containers using compose and the chosen filename
# To track the built process remove -d from the argd1

def startup():
    try:
        args1 = "docker-compose -f " + config.FILE + " build"
        args2 = "docker-compose -f " + config.FILE + " up -d"
        args3 = "docker-compose -f " + config.FILE + " restart alarm-logger"
    # Configure alarm-server match the name and upload the configuration from the config folder
        args4 = "docker exec -t alarm-server sh -c 'cd alarm-server && ./alarm-server.sh -config " + config.SYS + " -import " + config.CONF + " -settings config/settings.ini'"
    # Execute the bash commands ^^
        subprocess.call(args1, shell=True)
        time.sleep(15)
        subprocess.call(args2, shell=True)
        time.sleep(15)
        subprocess.call(args4, shell=True)
        time.sleep(60)
        subprocess.call(args3, shell=True)
    except:
    # If an exception is raised stop the containers
        print("Unable to start the containers")
        args = "docker-compose -f " + config.FILE + " down"
#        args1 = "docker-compose -f " + config.FILELOG + " down"
        subprocess.call(args, shell=True)
#        subprocess.call(args1, shell=True)

def stop():
    try:
        print("Stopping the containers...")
        args = "docker-compose -f " + config.FILE + " down"
#        args1 = "docker-compose -f " + config.FILELOG + " down"
        subprocess.call(args, shell=True)
#        subprocess.call(args1, shell=True)
    except:
        print("Error occured...")
        
def ioc():
    try:
        print("Starting the IOC...")
        args = "docker-compose -f " + config.FILE + " up -d ioc"
        subprocess.call(args, shell=True)
    except:
        print("Error occured...")
        
def archiver():
    try:
        print("Starting the archiver...")
        args = "docker-compose -f " + config.FILE + " up -d archappl"
        subprocess.call(args, shell=True)
    except:
        print("Error occured...")
def logs(arg):
    try:
        print("Checking the logs...")
        args = "docker-compose -f " + config.FILE + " logs --follow " + arg
        print(args)
        subprocess.call(args, shell=True)
    except:
        print("Error occured..")
        
