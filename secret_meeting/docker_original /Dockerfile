FROM node:18
WORKDIR /app/
COPY package*.json ./
RUN npm install
COPY server.js ./
USER node 
CMD [ "node", "server.js" ]
