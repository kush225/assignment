#pull official base image
FROM python:3.7-slim  

#setting up the directory
WORKDIR /server

##installing python-dev
RUN apt-get update -y && \
   apt-get upgrade -y && \
   apt-get dist-upgrade -y && \
   apt-get -y autoremove && \
   apt-get clean
#   && apt-get install python3-dev -y

#COPYING requirements
COPY ./requirements.txt ./requirements.txt

RUN pip3 install --upgrade pip 

#installing dependencies
RUN pip3 install -r ./requirements.txt 

#COPYING server files
COPY ./ ./

#run entrypoint.sh
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]