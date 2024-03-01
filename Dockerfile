FROM python:3.9.13-slim

COPY requirements.txt .
COPY app /app
COPY entrypoint.sh .

ENTRYPOINT [ "/bin/bash","entrypoint.sh" ]
