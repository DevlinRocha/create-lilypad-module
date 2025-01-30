import argparse
import os
import subprocess
from config.constants import (
    DOCKER_REPO,
    MODULE_REPO,
    TARGET_COMMIT,
    WEB3_DEVELOPMENT_KEY,
)


def run_module():
    parser = argparse.ArgumentParser(
        description="Run the Lilypad module with specified input."
    )

    parser.add_argument(
        "input",
        type=str,
        nargs="?",
        default=None,
        help="The input to be processed by the Lilypad module.",
    )

    parser.add_argument(
        "--local",
        action="store_true",
        help="Run the Lilypad module Docker image locally.",
    )

    args = parser.parse_args()

    if args.input is None:
        args.input = input("Please enter your input: ")

    local = args.local

    output_dir = os.path.abspath("./outputs")

    command = (
        [
            "docker",
            "run",
            "-e",
            f"INPUT={args.input}",
            "-v",
            f"{output_dir}:/outputs",
            f"{DOCKER_REPO}:latest",
        ]
        if local
        else [
            "lilypad",
            "run",
            f"{MODULE_REPO}:{TARGET_COMMIT}",
            "--web3-private-key",
            WEB3_DEVELOPMENT_KEY,
            "-i",
            f"input={args.input}",
        ]
    )

    try:
        result = subprocess.run(command, check=True, text=True)
        print("Lilypad module executed successfully.")
        return result
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_module()
