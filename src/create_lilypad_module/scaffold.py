#!/usr/bin/env python3

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
import importlib.resources as resources


def initialize_git_repo(target_dir: Path) -> None:
    """
    Initializes a Git repository in the specified directory.

    Args:
        target_dir (Path): Path to the directory where the Git repository will be initialized.

    Raises:
        SystemExit: If the Git initialization process fails.
    """
    try:
        os.chdir(target_dir)
        subprocess.run(["git", "init"], check=True)
        print(f"Initialized empty Git repository in {target_dir}")
    except subprocess.CalledProcessError as error:
        print(f"Error: Failed to initialize Git repository. {error}")
        sys.exit(1)


def get_github_username_from_remote(repo_path: Path) -> str:
    """
    Extracts the GitHub username from the remote URL of a Git repository.

    Args:
        repo_path (Path): Path to the local Git repository.

    Returns:
        str: The GitHub username extracted from the remote URL.

    Raises:
        SystemExit: If the specified path is not a valid Git repository or the username cannot be determined.
    """
    try:
        if not (repo_path / ".git").is_dir():
            raise ValueError(
                f"The directory {repo_path} is not a valid Git repository."
            )

        os.chdir(repo_path)

        remote_url = subprocess.check_output(
            ["git", "remote", "get-url", "origin"], text=True, stderr=subprocess.DEVNULL
        ).strip()

        match = re.search(r"github\.com[:/](.*?)/", remote_url)
        if match:
            return match.group(1)
        else:
            raise ValueError("GitHub username not found in the remote URL.")

    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)


def copy_templates(target_dir: Path) -> None:
    """
    Copies template files from the `templates` directory to the specified target directory.

    Args:
        target_dir (Path): Path to the target directory where template files will be copied.

    Raises:
        OSError: If an error occurs during the file or directory copying process.
    """
    try:
        with resources.path("create_lilypad_module", "templates") as templates_dir:
            for item in templates_dir.iterdir():
                target_path = target_dir / item.name
                if item.is_file():
                    shutil.copy(item, target_path)
                elif item.is_dir():
                    shutil.copytree(item, target_path)
    except OSError as error:
        print(f"Error copying templates: {error}")
        sys.exit(1)


def generate_module_config(github_repo: str, output_file: Path) -> None:
    """
    Generates a configuration file for the Lilypad module.

    Args:
        github_repo (str): The GitHub repository URL for the module.
        output_file (Path): Path to the output configuration JSON file.

    Raises:
        OSError: If an error occurs while writing the configuration file.
    """
    config = {
        "machine": {"gpu": 0, "cpu": 1000, "ram": 4000},
        "job": {
            "APIVersion": "V1beta1",
            "Metadata": {"CreatedAt": "0001-01-01T00:00:00Z", "Requester": {}},
            "Spec": {
                "Deal": {"Concurrency": 1},
                "Docker": {
                    "Entrypoint": ["python", "/workspace/run_inference.py"],
                    "WorkingDirectory": "/workspace",
                    "EnvironmentVariables": ["INPUT_TEXT={{ js .input }}"],
                    "Image": f"{github_repo}:latest",
                },
                "Engine": "Docker",
                "Network": {"Type": "None"},
                "Outputs": [{"Name": "outputs", "Path": "/outputs"}],
                "PublisherSpec": {"Type": "ipfs"},
                "Resources": {"CPU": "1", "Memory": "4000"},
                "Timeout": 600,
                "Wasm": {"EntryModule": {}},
            },
        },
    }

    try:
        with open(output_file, "w") as json_file:
            json.dump(config, json_file, indent=4)
        print(f"Module configuration generated at {output_file}")
    except OSError as error:
        print(f"Error writing configuration file: {error}")
        sys.exit(1)


def scaffold_project(project_name: str) -> None:
    """
    Scaffolds a new Lilypad module project in the specified directory.

    Args:
        project_name (str): Name of the new project.

    Raises:
        SystemExit: If the target directory already exists or if critical steps fail.
    """
    target_dir = Path.cwd() / project_name

    if target_dir.exists():
        print(f"Error: Directory '{project_name}' already exists.")
        sys.exit(1)

    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        print(f"Scaffolding project: {project_name}")

        copy_templates(target_dir)
        initialize_git_repo(target_dir)

        github_username = get_github_username_from_remote(target_dir)
        if github_username:
            github_repo = f"github.com/{github_username}/{project_name}"
            generate_module_config(
                github_repo=github_repo, output_file=target_dir / "lilypad_module.json"
            )
        else:
            print("Error: GitHub username could not be determined. Exiting.")
            sys.exit(1)
    except Exception as error:
        print(f"Error scaffolding project: {error}")
        sys.exit(1)


def main() -> None:
    """
    Entry point for the script. Parses command-line arguments and initiates project scaffolding.
    """
    parser = argparse.ArgumentParser(description="Scaffold a new Lilypad module.")
    parser.add_argument(
        "project_name",
        type=str,
        nargs="?",
        help="Name of the new project.",
    )
    args = parser.parse_args()
    project_name = args.project_name

    if not project_name:
        project_name = input(
            "Enter the name of your new project (default: lilypad-module): "
        ).strip()
        if not project_name:
            project_name = "lilypad-module"

    scaffold_project(project_name)


if __name__ == "__main__":
    main()
