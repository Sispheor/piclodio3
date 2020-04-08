# BUILD
# docker build --force-rm=true -t piclodio-back .

# RUN
# docker run -it --rm \
# -v /home/nico/Desktop/piclodio_db:/code/back/db.sqlite3 \
# -v /dev/snd:/dev/snd \
# -p 8000:8000 \
# piclodio-back

FROM python:3.7

# Set environment variables
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /

# Install dependencies
RUN apt-get update && apt-get install -y \
    libasound2-dev sqlite3 mplayer psmisc\
    && rm -rf /var/lib/apt/lists/*
RUN pip install -r /requirements.txt

# Set work directory
RUN mkdir /code
WORKDIR /code

# Copy project code
COPY . /code/

EXPOSE 8000

ENTRYPOINT /code/entrypoint.sh
