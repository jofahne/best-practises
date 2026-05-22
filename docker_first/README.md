
# Docker-First Secret And Environment Handling

## Important

The purpose of this repository is to show how to structure your folders when working with secrets and environment variables in a local Docker setup. Before cloning and using this repository, move your production secrets and environment variables outside the repository folder.

## What This Repository Is About

I changed my local development strategy to match the way I actually want to run applications: Docker first.

Instead of putting a `.env` file inside the repository or setting credentials directly in my shell profile, I now keep runtime configuration one level above the repository root on my local machine.

That means:

- secrets live in `.txt` files in a parent-level `secrets` folder
- non-secret environment variables live in a parent-level `.env` file
- `docker compose` loads both into the container at runtime

This keeps the repository clean while making Docker the single entry point for local development.

## Why I Changed The Setup

The main reason is risk reduction.

When coding agents are involved, anything stored inside the repository is easier to expose by accident. That includes `.env` files, temporary notes, copied credentials, and sample configuration that later turns real.

By moving secrets and environment values outside the repository tree, I reduce the chance that they end up in Git, editor context, screenshots, or agent prompts.

The second reason is consistency.

If Docker is the way I run the application locally, then Docker should also be the place where runtime configuration is wired in. That avoids maintaining one setup for local development and another for containerized execution.

The third reason is disk space and long-term maintainability.

After a few years of development, hundreds of projects with different virtual environments start to consume a surprising amount of hard disk space. My Docker-first approach helps because I do not need to keep every full local environment sitting around forever.

The easiest way to describe it is with a house analogy: instead of storing complete houses for every project, I keep the blueprint for how to build each one. Docker is the super-fast 3D printer that can rebuild those houses in the future whenever I need them. That means I keep the instructions in the repository, while the heavy runtime environment gets recreated on demand.

## Directory Layout

Here is the local pattern:

```text
root_local_project_folder/
	.env
	secrets/
		secret1.txt
	repository_folder/		
    docker-compose.yml
		Dockerfile
    .gitignore
    .dockerignore
		app_folder/
      example_app.py
```

In this layout:

- `repository_folder/` is the repository root
- `.env` sits one level above the repository root
- secret text files also sit one level above the repository root

That makes the repository portable while keeping machine-local runtime state outside version control.

## How Docker Compose Uses Them

The Compose file loads the parent-level `.env` file for regular environment variables and mounts the parent-level secret files.

Example pattern:

```yaml
services:
  test-app: #UPDATE
    build:
      context: .
      dockerfile: Dockerfile
    container_name: test-app-container #UPDATE
    env_file:
      - ../.env
    volumes:
      - ./test_app:/app/test_app   # For local development with short iterations, it is best practice to mount the app files. For production deployment, this can be removed.
    
    secrets:
      - secret1 #UPDATE
    restart: no

secrets:
  secret1:
    file: ../secrets/secret1.txt #UPDATE
```

That gives me a clean split:

- `.env` for non-secret runtime values
- Docker secrets file mounts for sensitive values

## Example Setup

Add each secret to a separate `.txt` file inside the parent-level `secrets` folder, and add all non-secret environment variables to the parent-level `.env` file.

Then I start the application from the repository root:

```bash
docker compose --env-file ../.env up --build -d
```

I use the `--env-file` form because it makes variables from the parent-level `.env` file available to Docker Compose while it parses `docker-compose.yml`, not just after the container starts.

Now Docker Compose becomes the only command I need for local startup.

## Why This Fits Agent-Assisted Development Better

This structure is simple, but it solves a real workflow problem.

The repository stays focused on code. Local machine configuration stays outside the codebase. Docker Compose becomes the boundary between the two.

That is a better fit for agent-assisted development because it reduces accidental secret exposure while keeping setup reproducible.

## Practical Rule

Keep repository code inside the repository. Keep secrets and local runtime configuration outside it. Let Docker Compose stitch them together at runtime.

That gives me one development path, fewer accidental leaks, and a cleaner transition from local work to deployment.
