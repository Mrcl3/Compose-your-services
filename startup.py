import config
import settings
import argparse

parser=argparse.ArgumentParser(
    description='''This script allows to build/stop all the containers.
This script will work properly if the subsystem name matches the alarm server configuration file''',
    epilog="""All is well that ends well.""")
parser.add_argument("--start", help="Start the containers", action="store_true")
parser.add_argument("--stop", help="Stop the containers", action="store_true")

args=parser.parse_args()

if args.start:
    settings.create_files()
    settings.startup()
if args.stop:
    settings.stop()












