ARG MESSAGE
FROM python:3.7-alpine 
WORKDIR /app 
COPY requirements.txt main.py /app/
RUN pip3 install --no-cache-dir -r requirements.txt 
COPY templates/index.html /app/templates/
ENV FLASK_ENV=${MESSAGE}
ENTRYPOINT ["python3"] 
CMD ["main.py"]