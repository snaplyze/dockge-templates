# pgAdmin

PGAdmin is a web-based GUI tool used to interact with the Postgres database sessions, both locally and remote servers as well. You can use PGAdmin to perform any sort of database administration required for a Postgres database.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://www.pgadmin.org/Official Docker Documentation: https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.htmlPre-installation script must be RAN before you install: wget -qO- https://raw.githubusercontent.com/pi-hosted/pi-hosted/master/tools/install_pgadmin.sh | bash

## Quick Start

```bash
cd /opt/stacks/pgadmin
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `PGADMIN_DEFAULT_EMAIL`: PGADMIN_DEFAULT_EMAIL
- `PGADMIN_DEFAULT_PASSWORD`: PGADMIN_DEFAULT_PASSWORD
- `TZ`: TZ

## Ports

- `5050:80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/lib/pgadmin` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*