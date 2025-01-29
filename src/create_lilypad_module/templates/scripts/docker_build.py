import subprocess
from config.constants import DOCKER_REPO


def docker_build():
    command = [
        "docker",
        "buildx",
        "build",
        "--platform",
        "linux/amd64,linux/arm64",
        "-t",
        f"{DOCKER_REPO}:latest",
        "--push",
        ".",
    ]

    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Docker image built and published to Docker Hub successfully.")
        return result
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    docker_build()
