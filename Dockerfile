FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3.11-venv && \
    echo "Zainstalowano python3.11-venv" && \
    dpkg -l | grep python3.11-venv

RUN apt-get update && apt-get install -y docker.io

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

USER jenkins
