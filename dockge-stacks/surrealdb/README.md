# SurrealDB

SurrealDB is an end-to-end cloud native database for web, mobile, serverless, jamstack, backend, and traditional applications.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://surrealdb.com/Official Docker Documentation: https://hub.docker.com/r/surrealdb/surrealdb

## Quick Start

```bash
cd /opt/stacks/surrealdb
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `SDB_USERNAME`: SDB_USERNAME
- `SDB_PASSWORD`: SDB_PASSWORD

## Ports

- `8020:8000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tool

---

*Converted from Portainer template to Dockge format*