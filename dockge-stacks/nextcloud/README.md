# Nextcloud

Where are your photos and documents? With Nextcloud you pick a server of your choice, at home, in a data center or at a provider. And that is where your files will be. Nextcloud runs on that server, protecting your data and giving you access from your desktop or mobile devices.

## Important Note

The database user is nextcloud and the database is nextcloud_db. The host of the database will be located at the bottom of the DB conotainer in portainer.

## Quick Start

```bash
cd /opt/stacks/nextcloud
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `DATABASE_PASSWORD`: DATABASE_PASSWORD
- `MYSQL_ROOT_PASSWORD`: MYSQL_ROOT_PASSWORD
- `PORT`: PORT

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Cloud, Productivity, Tools, Web

---

*Converted from Portainer template to Dockge format*