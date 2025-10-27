FROM nginx:alpine 
COPY nginx.conf /etc/nginx/conf.d/default.conf
HEALTHCHECK --interval=3s --timeout=30s --start-period=5s \
    CMD curl -f "http://localhost:7000/health" || exit 1
