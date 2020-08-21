FROM mongo:4.4

# install Python 3
RUN apt update && apt -y upgrade && apt install -y python3-pip
RUN apt install -y python3.7-dev
RUN pip3 install pymongo
RUN apt install -y vim

EXPOSE 27017
