FROM node:20

WORKDIR /app

COPY package.json .
RUN npm cache clean --force
RUN npm install

RUN npm i -g serve

COPY . .

RUN npm run build --verbose

EXPOSE 3000

CMD [ "serve", "-s", "dist" ]
