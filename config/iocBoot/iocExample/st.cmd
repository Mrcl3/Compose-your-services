#!/pandaIoc
epicsEnvSet( "STREAM_PROTOCOL_PATH", "protocols" )
dbLoadDatabase( "/dbd/pandaIoc.dbd", 0, 0 )
pandaIoc_registerRecordDeviceDriver( pdbbase )

## Load record instances
dbLoadTemplate "databases/user.substitutions"


iocInit()

dbl > log/ioc.dbl
