# Getting Started with Create Lilypad Module

This project was bootstrapped with [Create Lilypad Module](https://github.com/DevlinRocha/create-lilypad-module).

## Prerequisites

To build and run a module on Lilypad Network, you'll need to have the [Lilypad CLI](https://docs.lilypad.tech/lilypad/lilypad-testnet/install-run-requirements) and [Docker](https://www.docker.com/) on your machine, as well as [GitHub](https://github.com/) and [Docker Hub](https://hub.docker.com/) accounts.

## Getting Started

1. In your terminal, run `scripts/configure` and configure your module.
2. In your terminal, run `scripts/build` and wait for the Docker image to be built and pushed to Docker Hub.
3. Update "Image" field in [`lilypad_module.json.tmpl`](lilypad_module.json.tmpl).
4. Create a new GitHub repository, then commit and push your changes.

Your module's ready! 🎉

Once your Docker image has been pushed to Docker Hub, you can run your module on Lilypad Network:

> Run `git log` in your terminal to easily find the latest commit hash to use as the GitHub tag.

```sh
export WEB3_PRIVATE_KEY=WEB3_PRIVATE_KEY

lilypad run github.com/github_username/module_repo:github_tag -i prompt="What animal order do frogs belong to"
```

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
GITHUB_REPO
```

### [`scripts/build [--local]`](scripts/build)

Builds the Docker image and pushes it to Docker Hub.

#### `--local` Flag

Loads the built Docker image into the local Docker daemon.

### [`scripts/run`](scripts/run)

Run your module.

## Learn More

To learn more about Lilypad, check out the [Lilypad documentation](https://docs.lilypad.tech/lilypad).
