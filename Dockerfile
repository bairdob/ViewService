# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.9-alpine AS builder

COPY . /ViewService

WORKDIR /ViewService

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

EXPOSE 8080/tcp
CMD ["python3", "app.py"]

FROM builder as dev-envs

RUN <<EOF
apk update
apk add git
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
