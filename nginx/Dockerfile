FROM nginx:1.27.0-bookworm

COPY ./nginx/conf/ /etc/nginx/conf.d/

EXPOSE 443

ENTRYPOINT ["nginx"]

CMD ["-g", "daemon off;"]
