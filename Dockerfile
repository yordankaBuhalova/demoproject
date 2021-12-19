FROM python:3

# create dir
RUN mkdir /code
# set container working dir
WORKDIR /code
# install req. os packages
RUN apt update
RUN apt install gettext -y

# copy requirements.txt in code dir
COPY code/requirements.txt /code/
# install python packages
RUN pip install -r requirements.txt
