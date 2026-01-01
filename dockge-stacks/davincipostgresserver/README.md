# DaVinci Postgres Server

DaVinci Resolve Postgresql Server, Davinci requires a specific version of postgres db, this container will install the version needed

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://raw.githubusercontent.com/pi-hosted/pi-hosted/master/docs/davinci.mdOfficial Docker Documentation: https://raw.githubusercontent.com/pi-hosted/pi-hosted/master/docs/davinci.md

## Quick Start

```bash
cd /opt/stacks/davincipostgresserver
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `POSTGRES_DB`: POSTGRES_DB
- `POSTGRES_USER`: POSTGRES_USER
- `POSTGRES_PASSWORD`: POSTGRES_PASSWORD
- `TZ`: TZ

## Ports

- `5432:5432`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/lib/postgresql/data` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Tool

---

*Converted from Portainer template to Dockge format*