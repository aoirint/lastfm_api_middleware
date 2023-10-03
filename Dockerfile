# syntax=docker/dockerfile:1.5
FROM python:3.10

RUN <<EOF
    apt-get update
    apt-get install -y \
        gosu
    apt-get clean
    rm -rf /var/apt/lists/*

    groupadd -o -g 2000 user
    useradd -o -u 2000 -g user -m user
EOF

ADD requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /opt/lastfm_api_middleware
ADD ./lastfm_api_middleware /opt/lastfm_api_middleware/lastfm_api_middleware
ADD ./main.py /opt/lastfm_api_middleware/

CMD [ "gosu", "user", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
