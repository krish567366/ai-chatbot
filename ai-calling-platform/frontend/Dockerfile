# syntax=docker/dockerfile:1
FROM node:20-slim AS base
WORKDIR /usr/src/app
RUN corepack enable && corepack prepare pnpm@9.7.0 --activate
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile
COPY . .
EXPOSE 5173
CMD ["pnpm","dev","--host"]