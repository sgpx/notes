FROM python:3.12
EXPOSE 3001
WORKDIR /root
COPY ./backend /root/backend
WORKDIR /root/backend
RUN pip3 install -r requirements.txt
ENTRYPOINT ["gunicorn","app:app","-w","2","--error-logfile","/dev/stdout","--access-logfile","/dev/stdout","-t","180","--bind","0.0.0.0:3001"]
