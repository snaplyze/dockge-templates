# Pixapop

[Pixapop](https://github.com/bierdok/pixapop) is an open-source single page application to view your photos in the easiest way possible.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/pixapop/configmkdir -p /volume1/docker/pixapop/photos

## Quick Start

```bash
cd /opt/stacks/pixapop
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `APP_USERNAME`: APP_USERNAME
- `APP_PASSWORD`: APP_PASSWORD

## Ports

- `80:80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/photos` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Photos

---

*Converted from Portainer template to Dockge format*