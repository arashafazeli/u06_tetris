#FROM python:3.8
#
#WORKDIR /u06_tetris
#
#RUN apt-get update -y;apt-get install -y python  python3-pip \
#         libxml2 apt-utils sqlite3 build-essential;
#
#RUN pip install --upgrade pip
#
#COPY ./requirements.txt ./
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY ./ ./
#
#ENV PYTHONPATH /u06_tetris


FROM python:3.8

WORKDIR /u06_tetris

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main_modified.py" ]






