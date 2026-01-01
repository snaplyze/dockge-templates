# Gitea

Git with a cup of tea! Painless self-hosted all-in-one software development service, including Git hosting, code review, team collaboration, package registry and CI/CD.

## Important Note

Use SQLite3 for the database unless you have an external one setup.

## Quick Start

```bash
cd /opt/stacks/gitea
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `3000:3000`: Service port
- `222:22`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data` in container
- `./data/*`: Mapped to `/etc/timezone:ro` in container
- `./data/*`: Mapped to `/etc/localtime:ro` in container

## Source

Template maintainer:  https://github.com/Qballjos/portainer_templates/

## Categories

Web, Tools

---

*Converted from Portainer template to Dockge format*