FROM python:3.10-alpine
COPY ./cinema ./cinema
WORKDIR ./cinema
RUN pip install -r requirements.txt
RUN chmod 777 entrypoint.sh
ENTRYPOINT ./entrypoint.sh
