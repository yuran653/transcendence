FROM postgres:12.19-bookworm

COPY ./postgres/conf/postgresql.conf /etc/postgresql/postgresql.conf

# RUN chown postgres:postgres /etc/postgresql/postgresql.conf

# USER postgres

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]
