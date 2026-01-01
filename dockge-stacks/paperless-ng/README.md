# Paperless-ng

[Paperless-ng](https://github.com/jonaswinkler/paperless-ng) is an application by Daniel Quinn and contributors that indexes your scanned documents and allows you to easily search for documents and store metadata alongside your documents.'

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/paperless-ng/configmkdir -p /volume1/docker/paperless-ng/data

## Quick Start

```bash
cd /opt/stacks/paperless-ng
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `REDIS_URL`: REDIS_URL

## Ports

- `8000:8000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Familyappserver

---

*Converted from Portainer template to Dockge format*