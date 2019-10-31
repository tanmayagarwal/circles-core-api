#official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /root/Downloads/git-2.7.2/git-repo/circles-core-api/


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk --update --upgrade add gcc musl-dev  jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf 	 

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /root/Downloads/git-2.7.2/git-repo/circles-core-api/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /root/Downloads/git-2.7.2/git-repo/circles-core-api/entrypoint.sh
# copy project
COPY . /root/Downloads/git-2.7.2/git-repo/circles-core-api/

ENTRYPOINT ["/root/Downloads/git-2.7.2/git-repo/circles-core-api/entrypoint.sh"]
