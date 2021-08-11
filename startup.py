import subprocess
import config
import time

# Creates the settings.ini for Phoebus, alarm server and .env based on the config.py
phoebus = open("config/Phoebus/settings.ini", "w")
phoebus_list = [config.welcome, config.addr_list, config.urls, config.archives, config.use_default_archives, config.mailhost, config.server, config.config_name, config.config_names, config.threshold, config.nag_period, config.retention_count, config.es_host, config.es_port, config.es_index, config.es_max_size, config.es_sniff, config.jmasarurl, config.readtimeout, config.connecttimeout, config.split, config.sort, config.splitsave, config.enableCSVIO]
phoebus.writelines(phoebus_list)
phoebus.close()

alarm = open("config/Alarmconfig/settings.ini", "w")
alarm_list = [config.mailhost, config.port, config.server, config.config_name, config.config_names, config.email_sender, config.threshold, config.nag_period, config.retention_count]
alarm.writelines(alarm_list)
alarm.close()

env = open(".env", "w")
env_list = [ config.PATH, config.HOST, config.SUBSYSTEM]
env.writelines(env_list)
env.close()

# Build all the containers using compose and the chosen filename
# To track the built process remove -d from the argd1

try:
    args1 = "docker-compose -f " + config.FILE + " up -d"
# Configure alarm-server match the name and upload the configuration from the config folder
    args2 = "docker exec -t alarm-server sh -c 'cd alarm-server && ./alarm-server.sh -config " + config.SYS + " -import " + config.CONF + " -settings config/settings.ini'"
# Execute the bash commands ^^
    subprocess.call(args1, shell=True)
    time.sleep(10)
    subprocess.call(args2, shell=True)
except:
# If an exception is raised stop the containers
    print("Unable to start the containers")
    args3 = "docker-compose -f " + config.FILE + " down"
    subprocess.call(args3, shell=True)
    




