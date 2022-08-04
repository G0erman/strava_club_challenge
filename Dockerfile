FROM python:3.9

WORKDIR strava_app

COPY . /strava_app

RUN pip install -r requirements.txt

CMD pip freeze
