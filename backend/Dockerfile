FROM python:3.7-alpine 
WORKDIR /app 
RUN apk add --no-cache curl gcc python3-dev musl-dev linux-headers
COPY requirements.txt main.py healthcheck.py /app/
RUN pip3 install -r requirements.txt 
ENV FLASK_ENV=TEST
HEALTHCHECK --interval=3s --start-period=5s \
    CMD python3 healthcheck.py
ENTRYPOINT ["python3"]
CMD ["main.py"]
