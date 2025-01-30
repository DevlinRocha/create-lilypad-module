import argparse
import platform
import subprocess
import sys
from config.constants import DOCKER_REPO


def docker_build():
    if not DOCKER_REPO:
        print(
            "❌ Error: DOCKER_REPO is not set in config/constants.py.",
            file=sys.stderr,
            flush=True,
        )
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="Build and publish the Lilypad module Docker image."
    )

    parser.add_argument(
        "--push",
        action="store_true",
        help="Push the Docker image to Docker Hub.",
    )

    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Build the Docker image without using cache.",
    )

    args = parser.parse_args()

    push = args.push
    no_cache = args.no_cache

    arch_map = {
        "arm64": "arm64",
        "aarch64": "arm64",
        "x86_64": "amd64",
        "amd64": "amd64",
    }

    os_arch = arch_map.get(platform.machine(), "unsupported_arch")

    if not push and os_arch == "unsupported_arch":
        print(
            "❌ Error: Unsupported local architecture detected.",
            file=sys.stderr,
            flush=True,
        )
        print(
            "⛔️ Use `--push` to push the Docker image to Docker Hub instead of building locally."
        )
        print("👉 python -m scripts.docker_build --push")
        sys.exit(1)

    command = [
        "docker",
        "buildx",
        "build",
        "--platform",
        f"linux/{'amd64' if push else os_arch}",
        "-t",
        f"{DOCKER_REPO}:latest",
        "--push" if push else "--load",
        *(["--no-cache"] if push or no_cache else []),
        ".",
    ]

    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        if push:
            print("✅ Docker image built and published to Docker Hub successfully.")
        else:
            print("✅ Docker image built successfully.")
        return result
    except subprocess.CalledProcessError as error:
        print(
            f"❌ An error occurred: {error}",
            file=sys.stderr,
            flush=True,
        )
        sys.exit(1)


if __name__ == "__main__":
    docker_build()
