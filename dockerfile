# Makes a docker container with myst so I can run the Selenium bother


# Ad-Bot
FROM ubuntu:latest

# COPY Tun.sh /tmp/

ENV TZ=US/Mountain
ENV DISPLAY=:99

RUN apt-get update && \
    apt-get install wget python3 python3-pip sudo iproute2 net-tools iptables locales gnupg speedtest-cli -y && \
    pip install numpy pandas pyvirtualdisplay Display selenium selenium_stealth stealth undetected_chromedriver fake_useragent UserAgent random-user-agent && \ 
    mkdir /opt/myst && \
    wget -O /opt/myst/myst.tar.gz --no-check-certificate --content-disposition https://github.com/mysteriumnetwork/node/releases/download/1.6.3/myst_linux_amd64.tar.gz && \
    cd /opt/myst/ && \
    tar -zxvf /opt/myst/myst.tar.gz && \
    rm /opt/myst/myst.tar.gz && \
    cd / && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \ 
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update && apt-get -y install google-chrome-stable && \
    mkdir /root/Dockerdata/


