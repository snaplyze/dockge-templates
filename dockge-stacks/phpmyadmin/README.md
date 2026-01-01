# Phpmyadmin

[Phpmyadmin](https://github.com/phpmyadmin/phpmyadmin/) is a free software tool written in PHP, intended to handle the administration of MySQL over the Web. phpMyAdmin supports a wide range of operations on MySQL and MariaDB.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/phpmyadmin/config

## Quick Start

```bash
cd /opt/stacks/phpmyadmin
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `PMA_ARBITRARY`: PMA_ARBITRARY
- `PMA_ABSOLUTE_URI`: PMA_ABSOLUTE_URI

## Ports

- `80:80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Databaseserver

---

*Converted from Portainer template to Dockge format*