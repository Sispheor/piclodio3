# BUILD
# docker build --force-rm=true -t piclodio-front .

# RUN
# docker run -it --rm \
# -p 80:80 \
# piclodio-front

### Stage 1: build ###

FROM node:12.16.1-alpine as builder

# Set working directory
RUN mkdir /app
WORKDIR /app

# Copy app dependencies.
COPY package.json package-lock.json /app/

# Install app dependencies
RUN npm install

# Copy app files
COPY . /app

# Build app
RUN npm run build

### Stage 2: delivery ###

FROM nginx:1.16.1-alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy output directory from builder to nginx image
COPY --from=builder /app/dist/piclodio3-front /usr/share/nginx/html

# Copy nginx configuration file
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
