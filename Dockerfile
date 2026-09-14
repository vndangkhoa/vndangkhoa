FROM nginx:alpine

LABEL maintainer="Khoa Vo <vonguyendangkhoa@gmail.com>"
LABEL org.opencontainers.image.title="vndangkhoa profile"
LABEL org.opencontainers.image.description="Personal Profile & Portfolio for Khoa Vo (@vndangkhoa)"
LABEL org.opencontainers.image.url="https://github.com/vndangkhoa/vndangkhoa"
LABEL org.opencontainers.image.source="https://github.com/vndangkhoa/vndangkhoa"

COPY index.html /usr/share/nginx/html/index.html
COPY assets /usr/share/nginx/html/assets
COPY donation.jpg /usr/share/nginx/html/donation.jpg
COPY llms.txt /usr/share/nginx/html/llms.txt
COPY AGENTS.md /usr/share/nginx/html/AGENTS.md

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
