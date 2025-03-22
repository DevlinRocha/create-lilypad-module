# Getting Started with Create Lilypad Module

This project was bootstrapped with [Create Lilypad Module](https://github.com/DevlinRocha/create-lilypad-module).

## Prerequisites

To build and run a module on Lilypad Network, you'll need to have the [Lilypad CLI](https://docs.lilypad.tech/lilypad/lilypad-testnet/install-run-requirements) and [Docker](https://www.docker.com/) installed on your machine, as well as [GitHub](https://github.com/) and [Docker Hub](https://hub.docker.com/) accounts.

## Getting Started

> `create-lilypad-module` preconfigures Ollama models for the [`/v1/chat/completions` API endpoint](https://github.com/ollama/ollama/blob/main/docs/openai.md). If the model you're using is intended to use a different endpoint:
> 1. Update the `curl` request in the [`/src/run_model`](src/run_model) file to point to the desired endpoint.
> 2. If the new endpoint requires a different request format, modify the `request` argument specified in this `README` below and the `request` function in the [scripts/run](scripts/run) file.

Get a module up and running on Lilypad Network with 3 simple commands!

From the project directory run the following:

1. `scripts/configure` configures the module.
2. `scripts/build` builds and pushes the Docker image to Docker Hub. Depending on the size of the model you are using, expect this to take a while.
    - Update "Image" field in [`lilypad_module.json.tmpl`](lilypad_module.json.tmpl).
    - Commit and push your changes to a public GitHub repository.
3. `scripts/run` runs the module.
    - Enter a request to the module and wait for the response back.

You've just built and ran a module on Lilypad Network! 🎉

Once the Docker image has been pushed to Docker Hub, you can run the module on Lilypad Network from any machine that has the Lilypad CLI installed:

> When using the CLI, make sure that you Base64 encode your request (this is handled automatically when using `scripts/run`):

```sh
export WEB3_PRIVATE_KEY=WEB3_PRIVATE_KEY

lilypad run github.com/GITHUB_USERNAME/MODULE_REPO:TAG \
-i request="$(echo -n '{
  "model": "MODEL_NAME:MODEL_VERSION",
  "messages": [{
    "role": "system",
    "content": "you are a helpful AI assistant"
  },
  {
  "role": "user",
  "content": "what order do frogs belong to?"
  }],
  "temperature": 0.6
}' | base64 -w 0)"
```

| Field      | Description                                                                 | Type     |
| -----------| --------------------------------------------------------------------------- | -------- |
| `model`    | Model ID used to generate the response (e.g. deepseek-r1:7b). **Required**. | `string` |
| `messages` | A list of messages comprising the conversation so far. **Required**.        | `array`  |

### Optional Fields and Default Values

- [Create chat completion](https://platform.openai.com/docs/api-reference/chat/create)

| Field               | Description | Default |
| ------------------- | ----------- | ------- |
| `frequency_penalty` | Number between `-2.0` and `2.0`. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. | `0` |
| `max_tokens`        | The maximum number of tokens that can be generated in the chat completion. | |
| `presence_penalty`  | Number between `-2.0` and `2.0`. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. | `0` |
| `response_format`   | An object specifying the format that the model must output. [Learn more](https://platform.openai.com/docs/api-reference/chat/create#chat-create-response_format). | |
| `seed`              | Makes a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result. Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend. | |
| `stop`              | Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence. | `null` |
| `temperature`       | What sampling temperature to use, between `0` and `2`. Higher values like `0.8` will make the output more random, while lower values like `0.2` will make it more focused and deterministic. We recommend altering this or `top_p` but not both. | `1` |
| `top_p`             | An alternative to sampling with `temperature`, called nucleus sampling, where the model considers the results of the tokens with `top_p` probability mass. So `0.1` means only the tokens comprising the top 10% probability mass are considered. We recommend altering this or `temperature` but not both. | `1` |
| `tools`             | A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported. [Learn more](https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools). | |

## Available Scripts

In the project directory, you can run:

### [`scripts/configure`](scripts/configure)

Configures the module.
Sets the following values in the [`.env` file](.env)

```
MODEL_NAME
MODEL_VERSION
DOCKER_HUB_USERNAME
DOCKER_IMAGE
GITHUB_REPO
```

### [`scripts/build [--major] [--minor] [--patch] [--local]`](scripts/build)

Builds the Docker image and pushes it to Docker Hub.

#### `--major`, `--minor`, and `--patch` Flags

Increments the specified version before building the Docker image.

#### `--local` Flag

Loads the built Docker image into the local Docker daemon.

### [`scripts/run [--local]`](scripts/run)

Runs the module.

#### `--local` Flag

Runs the local Docker image (requires the image be built locally).

## Learn More

To learn more about Lilypad, check out the [Lilypad documentation](https://docs.lilypad.tech/lilypad).
