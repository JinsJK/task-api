FROM node:20.14.0-alpine AS builder
WORKDIR /app
COPY . .
RUN npm install && npm run build

FROM nginx:1.25.3-alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
