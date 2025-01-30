# Getting Started with Create Lilypad Module

This project was bootstrapped with [Create Lilypad Module](https://github.com/DevlinRocha/create-lilypad-module).

## Configuration

Additional configuration is required to run the Lilypad module.

> [config/constants.py](./config/constants.py)

```python
MODULE_REPO = ""
TARGET_COMMIT = ""
DOCKER_REPO = ""
WEB3_DEVELOPMENT_KEY = ""
```

### `MODULE_REPO`

The URL for the GitHub repository storing the module code.

### `TARGET_COMMIT`

The git commit hash that will be used to run the module.

Use `git log` to find and set this easily.

### `DOCKER_REPO`

The URL for the Docker Hub repository storing the container image of the module code.

### `WEB3_DEVELOPMENT_KEY`

> 🚨 **DO NOT SHARE THIS KEY** 🚨

The private key for the wallet that will be used to run the job.

A new burner wallet is highly recommended to use for development.
The wallet must have enough LP to fund the job.

- [Funding your wallet](https://docs.lilypad.tech/lilypad/lilypad-testnet/quick-start/funding-your-wallet-from-faucet)

## Available Scripts

In the project directory, you can run:

### [`python -m scripts.download_models`](./scripts/download_models.py)

A basic outline for downloading a model is provided, but the structure of the script and the methods for downloading and saving the model can differ between models and libraries. It’s important to tailor the process to the specific requirements of the model you're working with.

### [`python -m scripts.docker_build`](./scripts/docker_build.py)

Builds and publishes a Docker image for the module to use.

#### `--push` Flag

Running the script with `--push` passed in pushes the Docker image to Docker Hub.

#### `--no-cache` Flag

Running the script with `--no-cache` pased in builds the Docker image without using cache. Useful if you are having issues with your local Docker image. This flag is automatically applied when using `--push`.

### [`python -m scripts.run_module`](./scripts/run_module.py)

This script is provided for convenience to speed up development. It is equivalent to running the Lilypad module with the provided input and private key. Depending on how your module works, you may need to change the default behavior of this script.

#### `--local` Flag

Running the script with `--local` passed in runs the Lilypad module Docker image locally instead of on Lilypad's Network.

## Learn More

Learn how to build a [Lilypad job module](https://docs.lilypad.tech/lilypad/developer-resources/build-a-job-module).

To learn more about Lilypad, check out the [Lilypad documentation](https://docs.lilypad.tech/lilypad).
