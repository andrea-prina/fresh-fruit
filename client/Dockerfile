FROM node:14.16.0-alpine3.13

RUN npm install -g http-server

RUN addgroup app && adduser -S -G app app

USER app

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

RUN npm run build

EXPOSE 8080

CMD ["http-server", "dist"]