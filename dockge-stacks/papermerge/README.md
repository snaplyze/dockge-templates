# Papermerge

[Papermerge](https://www.papermerge.com/) is an open source document management system (DMS) primarily designed for archiving and retrieving your digital documents. Instead of having piles of paper documents all over your desk, office or drawers - you can quickly scan them and configure your scanner to directly upload to Papermerge DMS.'

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/papermerge/configmkdir -p /volume1/docker/papermerge/data

## Quick Start

```bash
cd /opt/stacks/papermerge
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