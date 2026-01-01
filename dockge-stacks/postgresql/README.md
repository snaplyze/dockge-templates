# PostgreSQL

The most advanced open-source database

## Quick Start

```bash
cd /opt/stacks/postgresql
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `POSTGRES_USER`: Superuser
- `POSTGRES_PASSWORD`: Superuser password

## Ports

- `5432`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/lib/postgresql/data` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Database

---

*Converted from Portainer template to Dockge format*