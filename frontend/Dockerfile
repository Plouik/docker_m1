ARG MESSAGE
FROM python:3.7-alpine 
WORKDIR /app 
RUN addgroup -S appgroup && adduser -S app -G appgroup
COPY --chown=app:appgroup requirements.txt main.py /app/
RUN apk add --no-cache curl && pip3 install --no-cache-dir -r requirements.txt  
COPY --chown=app:appgroup templates/index.html /app/templates/
ENV FLASK_ENV=${MESSAGE}

HEALTHCHECK --interval=3s --start-period=5s \
    CMD curl -f "http://localhost/health" || exit 1
ENTRYPOINT ["python3"] 
CMD ["main.py"]