#!/bin/bash
set -x

# Elastic defaults
if [ -z "${ES_HOST}" ]; then
    ES_HOST=$(hostname)
fi
if [ -z "${ES_PORT}" ]; then
    ES_PORT=9200
fi

# Kafka defaults
if [ -z "${KAFKA_HOST}" ]; then
    KAFKA_HOST=$(hostname)
fi
if [ -z "${KAFKA_PORT}" ]; then
    KAFKA_PORT=9092
fi


wait-for-it -t 5 ${KAFKA_HOST}:${KAFKA_PORT}
wait-for-it -t 5 ${ES_HOST}:${ES_PORT}

sleep 5s
echo "Creating ES Template" && cd /opt && es_host=${ES_HOST} es_port=${ES_PORT} sh ./create_alarm_template.sh ${SUBSYSTEM}
sleep 4
echo "Creating ES Index" && cd /opt && es_host=${ES_HOST} es_port=${ES_PORT} sh ./create_alarm_index.sh ${SUBSYSTEM}

# Start Alarm Logger
echo "Starting alarm-server for topic" &&\
    cd /opt/alarm-logger && \
    ./alarm-logger.sh \
        -topics ${SUBSYSTEM}\
        -es_host ${ES_HOST}\
        -es_port ${ES_PORT}\
        -es_sniff  false   \
        -bootstrap.servers ${KAFKA_HOST}:${KAFKA_PORT}\
        -date_span_units M\
        -date_span_value 1\
        -noshell
