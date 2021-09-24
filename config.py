#####
#Edit lines below to create your own configuration, SYS has to be changed only once and has to be present also in the alarm system configuration file
#####
import os
import getpass

#####
#Parameters to be changed
#####
#IOC name
IOCname = "exampleioc"
#st.cmd file path
IOCpath = "/config/iocBoot/iocExample/st.cmd"
# Define a name for the alarm-server, it will appear in the .env file
SYS = "CBM"
# Paths for STS, MTS and LTS Archiver appliance and logs


#############################################
#Path to the folder containing all the files
path = os.getcwd()
PATH = f"LOC={path}\n"
#Hostname for containers
hostname = getpass.getuser()
HOST = f"hostname={hostname}\n"
# Define docker-compose file to be initialized
FILE = "docker-compose-aa.yml"
# Define docker-compose file for logging to be initialized
#FILELOG = "docker-compose-log.yml"

# Define subsystem for the yml file
SUBSYSTEM = "SUBSYSTEM=" + SYS + "\n"
# Define the configuration for the alarm-server 
CONF = "config/example"
#Define the name of the IOC 
IOC = "IOC=" + IOCname +"\n"
#IOCpath for env file
IOCp = "iocpath=" + IOCpath + "\n"
#####
#Phoebus settings configuration
#####

# Site-specific welcome (add the path to the file)
welcome = "org.phoebus.ui/welcome=file:/epics/phoebus/site_welcome.html\n"
# Channel Access addr list
addr_list = "org.phoebus.pv.ca/addr_list=192.168.0.1\n"

# Archived Data (define the address of the archiver appliance)
urls = "org.csstudio.trends.databrowser3/urls=pbraw://0.0.0.0:17665/retrieval/\n"
archives = "org.csstudio.trends.databrowser3/archives=pbraw://0.0.0.0:17665/retrieval/\n"
use_default_archives = "org.csstudio.trends.databrowser3/use_default_archives=false\n"

# Alarm server configuration (email configuration depends on the site settings)
mailhost = "org.phoebus.email/mailhost=smtp.gsi.de\n"
port = "org.phoebus.email/mailport=25\n"
server = "org.phoebus.applications.alarm/server=localhost:29094\n"
email_sender = "org.phoebus.applications.alarm/automated_email_sender=Alarm Notification <m.bajdel@gsi.de>\n"
config_name = "org.phoebus.applications.alarm/config_name=" + SYS + "\n"
config_names = "org.phoebus.applications.alarm/config_names=" + SYS + "\n"
threshold = "org.phoebus.applications.alarm/annunciator_threshold=1\n"
nag_period = "org.phoebus.applications.alarm/nag_period=00:00:15\n"
retention_count = "org.phoebus.applications.alarm/annunciator_retention_count=100\n"

# Elastic node configuration
es_host = "org.phoebus.applications.alarm.logging.ui/es_host=localhost\n"
es_port = "org.phoebus.applications.alarm.logging.ui/es_port=9202\n"
es_index = "org.phoebus.applications.alarm.logging.ui/es_index=alarms\n"
es_max_size = "org.phoebus.applications.alarm.logging.ui/es_max_size=1000\n"
es_sniff = "org.phoebus.applications.alarm.logging.ui/es_sniff=false\n"

#save and restore
#The URL to the save-and-restore service
jmasarurl = "org.phoebus.applications.saveandrestore/jmasar.service.url=http://localhost:8080\n"
# Read timeout (in ms) used by the Jersey client
readtimeout = "org.phoebus.applications.saveandrestore/httpClient.readTimeout=1000\n"

# Connect timeout in (ms) used by the Jersey client
connecttimeout = "org.phoebus.applications.saveandrestore/httpClient.connectTimeout=1000\n"

# Extract snapshots from TreeView to ListView
split = "org.phoebus.applications.saveandrestore/splitSnapshot=false\n"

# Sort snapshots in reverse order of created time. Last item comes first.
sort = "org.phoebus.applications.saveandrestore/sortSnapshotsTimeReversed=false\n"

# In "Create/Add to a saveset" dialog, split savesets from folder and show them in ListView
splitsave = "org.phoebus.applications.saveandrestore/splitSaveset=false\n"

# Specify hierarchy parser class to enable TreeTableView in snapshot
# Hierarchy parser class should be in ui/snapshot/hierarchyparser
# RegexHierarchyParser is provided for convenience. Use , as separator for each regex pattern.
# First matched pattern is used to create its hierarchy.
#treeTableView.enable=false
#treeTableView.hierarchyParser=RegexHierarchyParser
#regexHierarchyParser.regexList=(\\w+)_(\\w+):(\\w+)_(\\w+):(.*),(\\w+)_(\\w+):(\\w+)_(.*),(\\w+)_(\\w+):(.*),(\\w+):(.*)

# Importing/exporting saveset/snapshot to/from CSV (Git SNP/BMS compatible)
enableCSVIO = "org.phoebus.applications.saveandrestore/enableCSVIO=false\n"


