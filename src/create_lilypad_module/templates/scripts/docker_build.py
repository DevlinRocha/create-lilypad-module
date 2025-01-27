import subprocess
from ..config.constants import DOCKER_REPO


def docker_build():
    command = [
        "docker",
        "buildx",
        "build",
        "--platform",
        "linux/amd64",
        "-t",
        f"{DOCKER_REPO}:latest",
        "--push",
        ".",
    ]

    try:
        result = subprocess.run(command, check=True, text=True)
        print("Lilypad module executed successfully.")
        return result
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    docker_build()
