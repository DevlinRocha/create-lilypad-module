#!/usr/bin/env python3

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from importlib.resources import files


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
    except subprocess.CalledProcessError as error:
        print(f"Error: Failed to initialize Git repository. {error}")
        sys.exit(1)


def copy_templates(target_dir: Path) -> None:
    """
    Copies template files from the `templates` directory to the specified target directory.

    Args:
        target_dir (Path): Path to the target directory where template files will be copied.

    Raises:
        OSError: If an error occurs during the file or directory copying process.
    """
    templates_dir = Path(__file__).resolve().parent / "templates"

    if not templates_dir.is_dir():
        print(f"Error: Templates directory not found at {templates_dir}")
        sys.exit(1)
    try:
        shutil.copytree(
            templates_dir,
            target_dir,
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
    except OSError as error:
        print(f"Error copying templates: {error}")
        sys.exit(1)


def generate_module_config(output_file: Path) -> None:
    """
    Generates a configuration file for the Lilypad module.

    Args:
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
                    "Entrypoint": ["python", "/workspace/src/run_inference.py"],
                    "WorkingDirectory": "/workspace",
                    "EnvironmentVariables": ["INPUT_TEXT={{ js .input }}"],
                    "Image": "",
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
        print(
            f"\nCreating a new Lilypad module in: {Path(__file__).resolve().parent}/{project_name}\n"
        )

        copy_templates(target_dir)
        initialize_git_repo(target_dir)

        generate_module_config(
            output_file=target_dir / "lilypad_module.json.tmpl",
        )

        print(f"\n✅ Success! Created {project_name} at ~/{project_name}")
        print("\nOpen the project by typing:")
        print(f"\n\t\033[38;2;20;199;195mcd\033[0m {project_name}")
        print(f"\nGLHF!")
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
