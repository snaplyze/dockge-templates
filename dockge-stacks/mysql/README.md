# MySQL

The most popular open-source database

## Quick Start

```bash
cd /opt/stacks/mysql
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `MYSQL_ROOT_PASSWORD`: Root password
- `MYSQL_ROOT_HOST`: MYSQL_ROOT_HOST

## Ports

- `3306`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/lib/mysql` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Database

---

*Converted from Portainer template to Dockge format*