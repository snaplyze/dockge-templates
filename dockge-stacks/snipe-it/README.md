# Snipe-it

Snipe-it makes asset management easy. It was built by people solving real-world IT and asset management problems, and a solid UX has always been a top priority. Straightforward design and bulk actions mean getting things done faster.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/snipe-it/config

## Quick Start

```bash
cd /opt/stacks/snipe-it
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `APP_URL`: APP_URL
- `MYSQL_PORT_3306_TCP_ADDR`: MYSQL_PORT_3306_TCP_ADDR
- `MYSQL_PORT_3306_TCP_PORT`: MYSQL_PORT_3306_TCP_PORT
- `MYSQL_DATABASE`: MYSQL_DATABASE
- `MYSQL_USER`: MYSQL_USER
- `MYSQL_PASSWORD`: MYSQL_PASSWORD

## Ports

- `8080:80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Managementutilityserver

---

*Converted from Portainer template to Dockge format*