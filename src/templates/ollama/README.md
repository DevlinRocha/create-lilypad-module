# Getting Started with Create Lilypad Module

This project was bootstrapped with [Create Lilypad Module](https://github.com/DevlinRocha/create-lilypad-module).

## Prerequisites

To build and run a module on Lilypad Network, you'll need to have the [Lilypad CLI](https://docs.lilypad.tech/lilypad/lilypad-testnet/install-run-requirements) and [Docker](https://www.docker.com/) installed on your machine, as well as [GitHub](https://github.com/) and [Docker Hub](https://hub.docker.com/) accounts.

## Getting Started

> `create-lilypad-module` preconfigures Ollama models for the [`/chat` API endpoint](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-chat-completion). If the model you're using is intended to use a different endpoint:
> 1. Update the `curl` request in the [`/src/run_model`](src/run_model) file to point to the desired endpoint.
> 2. If the new endpoint requires a different request format, modify the `request` argument specified in this `README` below and the `request` function in the [scripts/run](scripts/run) file.

Get a module up and running on Lilypad Network with 3 simple commands!

From the project directory run the following:

1. `scripts/configure` configures the module.
2. `scripts/build` builds and pushes the Docker image to Docker Hub. Depending on the size of the model you are using, expect this to take a while.
    - Update "Image" field in [`lilypad_module.json.tmpl`](lilypad_module.json.tmpl).
    - Commit and push your changes to a public GitHub repository.
5. `scripts/run` runs the module.
    - Enter a request to the module and wait for the response back.

You've just built and ran a module on Lilypad Network! 🎉

Once the Docker image has been pushed to Docker Hub, you can run the module on Lilypad Network.

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
  "content": "what is the animal order of the frog?"
  }],
  "stream": false,
  "options": {
    "temperature": 1.0
  }
}' | base64 -w 0)"
```

### Valid Options Parameters and Default Values

- [Ollama Modelfile](https://github.com/ollama/ollama/blob/main/docs/modelfile.md#valid-parameters-and-values)

| Parameter      | Description                                                                                                                                                                                                                                                                                                                                                 | Default |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| mirostat       | Enable Mirostat sampling for controlling perplexity. (0 = disabled, 1 = Mirostat, 2 = Mirostat 2.0)                                                                                                                                                                                                                                                         | `0`     |
| mirostat_eta   | Influences how quickly the algorithm responds to feedback from the generated text. A lower learning rate will result in slower adjustments, while a higher learning rate will make the algorithm more responsive.                                                                                                                                           | `0.1`   |
| mirostat_tau   | Controls the balance between coherence and diversity of the output. A lower value will result in more focused and coherent text.                                                                                                                                                                                                                            | `5`     |
| num_ctx        | Sets the size of the context window used to generate the next token.                                                                                                                                                                                                                                                                                        | `2048`  |
| repeat_last_n  | Sets how far back for the model to look back to prevent repetition. (0 = disabled, -1 = num_ctx)                                                                                                                                                                                                                                                            | `64`    |
| repeat_penalty | Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a lower value (e.g., 0.9) will be more lenient.                                                                                                                                                                                        | `1.1`   |
| temperature    | The temperature of the model. Increasing the temperature will make the model answer more creatively.                                                                                                                                                                                                                                                        | `0.8`   |
| seed           | Sets the random number seed to use for generation. Setting this to a specific number will make the model generate the same text for the same prompt.                                                                                                                                                                                                        | `0`     |
| stop           | Sets the stop sequences to use. When this pattern is encountered the LLM will stop generating text and return. Multiple stop patterns may be set by specifying multiple separate stop parameters in a modelfile.                                                                                                                                            |         |
| num_predict    | Maximum number of tokens to predict when generating text. (-1 = infinite generation)                                                                                                                                                                                                                                                                        | `-1`    |
| top_k          | Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative.                                                                                                                                                                                          | `40`    |
| top_p          | Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text.                                                                                                                                                                                    | `0.9`   |
| min_p          | Alternative to the top_p, and aims to ensure a balance of quality and variety. The parameter p represents the minimum probability for a token to be considered, relative to the probability of the most likely token. For example, with p=0.05 and the most likely token having a probability of 0.9, logits with a value less than 0.045 are filtered out. | `0.0`   |

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

### `--major`, `--minor`, and `--patch` Flags

Increments the specified version before building the Docker image.

#### `--local` Flag

Loads the built Docker image into the local Docker daemon.

### [`scripts/run [--local]`](scripts/run)

Runs the module.

#### `--local` Flag

Runs the local Docker image (requires the image be built locally).

## Learn More

To learn more about Lilypad, check out the [Lilypad documentation](https://docs.lilypad.tech/lilypad).
