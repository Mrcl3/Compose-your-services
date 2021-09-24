import config
import settings
import argparse

parser=argparse.ArgumentParser(
    description='''This script allows to build/stop all the containers.
This script will work properly if the subsystem name matches the alarm server configuration file''',
    epilog="""All is well that ends well.""")
parser.add_argument("--start", help="Start the containers", action="store_true")
parser.add_argument("--stop", help="Stop the containers", action="store_true")
parser.add_argument("--ioc", help="Start the IOC", action="store_true")
parser.add_argument("--archiver", help="Start the archiver", action="store_true")
parser.add_argument("--log", nargs='?', help="Specify the service name (not the container name)", default="check_string_for_empty")

args=parser.parse_args()

if args.start:
    settings.create_files()
    settings.startup()
if args.stop:
    settings.stop()
if args.ioc:
    settings.create_files()
    settings.ioc()
if args.archiver:
    settings.archiver()
if args.log:
    settings.logs(args.log)










