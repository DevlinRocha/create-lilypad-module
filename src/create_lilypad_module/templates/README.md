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

Once your Docker image has been pushed to Docker Hub, you can run your module on Lilypad Network.

> Make sure that you Base64 encode your input.

```sh
export WEB3_PRIVATE_KEY=WEB3_PRIVATE_KEY

lilypad run github.com/github_username/module_repo:v0.0.0 -i input=$(echo '{"prompt": "Which animal order do frogs belong to?", "system": "You are a helpful AI assistant", "temperature": "0.4"}' | base64 -w 0)
```

### Valid Parameters and Default Values

> \* === Required

| Parameter      | Description                                                                                                                                                                                                                                                                                                                                                 | Default |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| prompt\*       | The content of the message sent from the user to the model.                                                                                                                                                                                                                                                                                                 | `""`    |
| system         | The content of the message sent from the system to the model.                                                                                                                                                                                                                                                                                               | `""`    |
| mirostat       | Enable Mirostat sampling for controlling perplexity. (0 = disabled, 1 = Mirostat, 2 = Mirostat 2.0)                                                                                                                                                                                                                                                         | `0`     |
| mirostat_eta   | Influences how quickly the algorithm responds to feedback from the generated text. A lower learning rate will result in slower adjustments, while a higher learning rate will make the algorithm more responsive.                                                                                                                                           | `0.1`   |
| mirostat_tau   | Controls the balance between coherence and diversity of the output. A lower value will result in more focused and coherent text.                                                                                                                                                                                                                            | `5`     |
| num_ctx        | Sets the size of the context window used to generate the next token.                                                                                                                                                                                                                                                                                        | `2048`  |
| repeat_last_n  | Sets how far back for the model to look back to prevent repetition. (0 = disabled, -1 = num_ctx)                                                                                                                                                                                                                                                            | `64`    |
| repeat_penalty | Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a lower value (e.g., 0.9) will be more lenient.                                                                                                                                                                                        | `1.1`   |
| temperature    | The temperature of the model. Increasing the temperature will make the model answer more creatively.                                                                                                                                                                                                                                                        | `0.8`   |
| seed           | Sets the random number seed to use for generation. Setting this to a specific number will make the model generate the same text for the same prompt.                                                                                                                                                                                                        | `0`     |
| num_predict    | Maximum number of tokens to predict when generating text. (-1 = infinite generation)	                                                                                                                                                                                                                                                                       | `-1`    |
| top_k          | Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative.                                                                                                                                                                                          | `40`    |
| top_p          | Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text.                                                                                                                                                                                    | `0.9`   |
| min_p          | Alternative to the top_p, and aims to ensure a balance of quality and variety. The parameter p represents the minimum probability for a token to be considered, relative to the probability of the most likely token. For example, with p=0.05 and the most likely token having a probability of 0.9, logits with a value less than 0.045 are filtered out. | `0.0`   |

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

### [`scripts/build [--major] [--minor] [--patch] [--local]`](scripts/build)

Builds the Docker image and pushes it to Docker Hub.

### `--major`, `--minor`, and `--patch` Flags

Increment the specified version before building the Docker image.

#### `--local` Flag

Loads the built Docker image into the local Docker daemon.

### [`scripts/run`](scripts/run)

Run your module.

## Learn More

To learn more about Lilypad, check out the [Lilypad documentation](https://docs.lilypad.tech/lilypad).
