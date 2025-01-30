import argparse
import platform
import subprocess
from config.constants import DOCKER_REPO


def docker_build():
    parser = argparse.ArgumentParser(
        description="Build and publish the Lilypad module Docker image."
    )

    parser.add_argument(
        "--push",
        action="store_true",
        help="Push the Docker image to Docker Hub.",
    )

    args = parser.parse_args()

    push = args.push

    machine_arch = platform.machine()
    if machine_arch in ["arm64", "aarch64"]:
        os_arch = "arm64"
    elif machine_arch in ["x86_64", "amd64"]:
        os_arch = "amd64"
    else:
        os_arch = "unsupported_arch"

    if not push and os_arch == "unsupported_arch":
        print(
            "❌ Error: You are building a local Docker image for an unsupported architecture."
        )
        print(
            "⛔️ Instead, consider using `--push` to push a Docker image for a supported architecture to Docker Hub."
        )
        print("👉 python -m scripts.docker_build --push")
        return

    command = (
        [
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
        if push
        else [
            "docker",
            "buildx",
            "build",
            "--platform",
            f"linux/{machine_arch}",
            "-t",
            f"{DOCKER_REPO}:latest",
            ".",
        ]
    )

    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        (
            print("✅ Docker image built and published to Docker Hub successfully.")
            if push
            else print("✅ Docker image built successfully.")
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    docker_build()
