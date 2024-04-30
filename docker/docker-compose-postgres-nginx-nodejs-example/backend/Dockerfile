FROM node:20
WORKDIR /app
COPY ./index.js /app/
COPY ./package.json /app/
RUN npm i
ENTRYPOINT [ "node","index.js" ]
EXPOSE 3990