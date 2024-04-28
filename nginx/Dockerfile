FROM nginx
COPY ./foobar/ /foobar
RUN rm -rf /usr/share/nginx/html
RUN mv /foobar /usr/share/nginx/html
EXPOSE 80
