ARG MESSAGE
FROM python:3.7-alpine 
WORKDIR /app 
COPY requirements.txt main.py /app/
RUN apk add --no-cache curl && pip3 install --no-cache-dir -r requirements.txt  
COPY templates/index.html /app/templates/
ENV FLASK_ENV=${MESSAGE}

HEALTHCHECK --interval=3s --start-period=5s \
    CMD curl -f "http://localhost/health" || exit 1
ENTRYPOINT ["python3"] 
CMD ["main.py"]