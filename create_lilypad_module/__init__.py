#!/usr/bin/env python3

import os
import sys
import subprocess
import json
import re


def initialize_git_repo(target_dir):
    """
    Initializes a Git repository in the target directory.
    """
    try:
        os.chdir(target_dir)
        subprocess.run(["git", "init"], check=True)
        print(f"Initialized empty Git repository in {target_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to initialize Git repository. {e}")
        sys.exit(1)


def get_github_username_from_remote(repo_path):
    """
    Retrieves the GitHub username from the remote URL of a Git repository.
    """
    try:
        if not os.path.isdir(os.path.join(repo_path, ".git")):
            raise ValueError(
                f"The directory {repo_path} is not a valid Git repository."
            )

        os.chdir(repo_path)

        remote_url = (
            subprocess.check_output(
                ["git", "remote", "get-url", "origin"], stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
        )

        match = re.search(r"github\.com[:/](.*?)/", remote_url)
        if match:
            return match.group(1)
        else:
            raise ValueError("GitHub username not found in the remote URL.")
    except Exception as e:
        print(f"Error: {e}")
        return None


def clone_template_repo(template_repo_url, target_dir):
    """
    Clones the template repository into the target directory.
    """
    if os.path.exists(target_dir):
        print(f"Error: Directory '{target_dir}' already exists.")
        sys.exit(1)

    try:
        print(f"Cloning {template_repo_url} into {target_dir}...")
        subprocess.run(["git", "clone", template_repo_url, target_dir], check=True)
        print(f"Template cloned successfully into '{target_dir}'.")

        pyproject_path = os.path.join(target_dir, "pyproject.toml")

        if os.path.exists(pyproject_path):
            os.remove(pyproject_path)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to clone repository. {e}")
        sys.exit(1)


def generate_module_config(github_repo, output_file="lilypad_module.json.tmpl"):
    """
    Generates the module configuration file for Lilypad.
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

    with open(output_file, "w") as json_file:
        json.dump(config, json_file, indent=4)
    print(f"Module configuration generated at {output_file}")


def main():
    """
    Main function to create a Lilypad module project.
    """
    template_repo_url = "https://github.com/DevlinRocha/create-lilypad-module.git"

    print("Welcome to Lilypad Module Creator!")

    project_name = input(
        "Enter the name of your new project (default: lilypad-module): "
    ).strip()

    if not project_name:
        project_name = "lilypad-module"

    target_dir = os.path.join(os.getcwd(), project_name)

    clone_template_repo(template_repo_url, target_dir)
    initialize_git_repo(target_dir)

    github_username = get_github_username_from_remote(target_dir)
    generate_module_config(f"github.com/{github_username}/{project_name}")


if __name__ == "__main__":
    main()
