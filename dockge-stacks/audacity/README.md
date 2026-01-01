# Audacity

[Audacity](https://www.audacityteam.org/) is an easy-to-use, multi-track audio editor and recorder. Developed by a group of volunteers as open source.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/audacity/config

## Quick Start

```bash
cd /opt/stacks/audacity
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ

## Ports

- `3000:3000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*