FROM ubuntu:20.04
RUN ln -s /usr/share/zoneinfo/Asia/Kolkata /etc/localtime

RUN apt update
RUN apt install -y wget xz-utils

WORKDIR /root
RUN wget -v https://nodejs.org/dist/v20.11.0/node-v20.11.0-linux-arm64.tar.xz -O /root/a.tar.xz

RUN mkdir /root/serv/
EXPOSE 3000

RUN echo 'export PATH="$PATH:/root/nodejs/bin"' >> ~/.bashrc
RUN cd /root && tar xf /root/a.tar.xz -C /root/ && mv -v /root/node* /root/nodejs
COPY ./index.js /root/serv/index.js
RUN export PATH="$PATH:/root/nodejs/bin" && cd /root/serv && /root/nodejs/bin/npm init --yes && npm i express cors
ENTRYPOINT ["/root/nodejs/bin/node","/root/serv/index.js"]
