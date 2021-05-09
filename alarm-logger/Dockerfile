FROM openjdk:14-jdk

RUN microdnf -y install git wget unzip hostname

ARG SUBSYSTEM
ENV SUBSYSTEM $SUBSYSTEM
WORKDIR /opt

# Wait-for-it
RUN git clone https://github.com/vishnubob/wait-for-it.git &&\
    chmod +x /opt/wait-for-it/wait-for-it.sh &&\
    ln -s /opt/wait-for-it/wait-for-it.sh /bin/wait-for-it

# Phoebus alarm logger
RUN cd /opt && wget https://controlssoftware.sns.ornl.gov/css_phoebus/nightly/alarm-logger.zip &&\
    unzip alarm-logger.zip && rm -f alarm-logger-4.6.6.zip && mv alarm-logger-4.6.6 alarm-logger

COPY create_alarm_template.sh /opt/create_alarm_template.sh
COPY create_alarm_index.sh    /opt/create_alarm_index.sh

RUN chmod +x /opt/create_alarm_template.sh && sed -i -e '/es_host=localhost/d' -e '/es_port=9200/d' /opt/create_alarm_template.sh &&\
    chmod +x /opt/create_alarm_index.sh    && sed -i -e '/es_host=localhost/d' -e '/es_port=9200/d' /opt/create_alarm_index.sh

COPY docker-entrypoint-logger.sh /docker-entrypoint.sh

CMD /bin/bash /docker-entrypoint.sh
