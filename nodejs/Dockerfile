FROM node:14

WORKDIR /app

ARG DEFAULT_PORT=80

COPY package.json .

RUN npm install

COPY . .

ENV PORT $DEFAULT_PORT

EXPOSE $PORT

# VOLUME [ "/app/node_modules" ]

VOLUME ["/app/temp"]

CMD [ "npm", "start" ]