#!/epics/ioc/bin/linux-x86_64/epicsIoc

epicsEnvSet( "STREAM_PROTOCOL_PATH", "/protocols" )
dbLoadDatabase( "/epics/ioc/dbd/epicsIoc.dbd", 0, 0 
epicsIoc_registerRecordDeviceDriver( pdbbase )

## Load record instances
dbLoadTemplate "databases/user.substitutions"


iocInit()

dbl > log/ioc.dbl
