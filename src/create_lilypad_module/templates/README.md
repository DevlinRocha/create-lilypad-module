# Getting Started with Create Lilypad Module

This project was bootstrapped with [Create Lilypad Module](https://github.com/DevlinRocha/create-lilypad-module).

## Prerequisites

To build and run a module on Lilypad Network, you'll need to have the [Lilypad CLI](https://docs.lilypad.tech/lilypad/lilypad-testnet/install-run-requirements) and [Docker](https://www.docker.com/) on your machine, as well as [GitHub](https://github.com/) and [Docker Hub](https://hub.docker.com/) accounts.

## Available Scripts

In the project directory, you can run:

### [`scripts/configure`](scripts/configure)

Configure your module.
Set the following values in the [`.env` file](.env)

```
MODEL_NAME
MODEL_VERSION
DOCKER_HUB_USERNAME
DOCKER_IMAGE
DOCKER_TAG
GITHUB_REPO
GITHUB_TAG
```

#### `MODEL_NAME`

The name of the model your module will use.

#### `MODEL_VERSION`

The version of the model your module will use.

#### `DOCKER_HUB_USERNAME`

Your Docker Hub username.

#### `DOCKER_IMAGE`

The name of the Docker image.

#### `DOCKER_TAG`

The tag for the Docker image.

Default: v.0.0.0

#### `GITHUB_REPO`

The GitHub repository URL for the module.

#### `GITHUB_TAG`

The GitHub tag, branch, or commit hash.

Use `git log` to easily find commit hashes.

### [`scripts/build [--local]`](scripts/build)

Builds the Docker image and pushes it to Docker Hub.

#### `--local` Flag

Loads the built Docker image into the local Docker daemon.

### [`scripts/run`](scripts/run)

Run your module.

## Learn More

To learn more about Lilypad, check out the [Lilypad documentation](https://docs.lilypad.tech/lilypad).
