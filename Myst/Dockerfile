# myst-client

FROM jrei/systemd-ubuntu

# fixes timezone
ENV TZ=${timezone}
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# below are the 3 lines that fix domain resolution errors during build
RUN mkdir -p /var/lib/resolvconf && \
    :> /var/lib/resolvconf/linkified && \
    echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-set-selections

# runs myst installer script
COPY myst-installer.sh tmp/installer.sh
RUN chmod +x /tmp/installer.sh && \
    /tmp/installer.sh

# install python and pip dependencies
RUN apt-get install python3 python3-pip dnsutils iputils-ping iproute2 net-tools iptables locales screen speedtest-cli -y

# makes folder in root's home for project files
RUN mkdir ~/dockerdata

# copies mysterium config files -- for some reason the install script doesnt copy them
RUN mkdir /usr/bin/config/
COPY myst-data/config/* /usr/bin/config/

# install dependencies for your script
COPY python-scripts/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt