FROM node:16-alpine

WORKDIR /code
COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile

ENV NODE_ENV development
ENV NEXT_TELEMETRY_DISABLED 1

CMD ["yarn", "dev"]