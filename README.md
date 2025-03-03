# Create Lilypad Module

Create Lilypad Module is an officially supported way to create Lilypad modules. It offers a modern Docker build setup with minimal configuration.

If something doesn’t work, please [file an issue](https://github.com/DevlinRocha/create-lilypad-module/issues/new).

If you have questions or need help, please ask in [GitHub Discussions](https://github.com/DevlinRocha/create-lilypad-module/discussions).

## Quick Start

```sh
create-lilypad-module project_name
cd project_name
scripts/configure
scripts/build
scripts/run
```

> If you've previously installed `create-lilypad-module` globally via `npm install -g create-lilypad-module`, we recommend you uninstall the package using `npm uninstall -g create-lilypad-module` to ensure that `npx` always uses the latest version.

Output:

```
project_name
├── scripts
│   ├── build
│   ├── configure
│   └── run
├── src
│   └── run_model
├── .dockerignore
├── .env
├── .gitignore
├── Dockerfile
├── lilypad_module.json.tmpl
├── README.md
```
