FROM python:3.7-alpine as builder
WORKDIR /app 
RUN apk update && \
    apk add --no-cache gcc python3-dev musl-dev linux-headers

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.7-alpine 

WORKDIR /app
RUN addgroup -S appgroup && adduser -S app -G appgroup
RUN chwn -R app:appgroup /app
USER app
COPY --chown=app:appgroup --from=builder /app/wheels /wheels
COPY --chown=app:appgroup --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY --chown=app:appgroup main.py healthcheck.py /app/

ENV FLASK_ENV=TEST
HEALTHCHECK --interval=3s --start-period=5s \
    CMD python3 healthcheck.py
ENTRYPOINT ["python3"]
CMD ["main.py"]
