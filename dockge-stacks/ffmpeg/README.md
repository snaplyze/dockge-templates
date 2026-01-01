# Ffmpeg

This container needs special attention. Please check https://hub.docker.com/r/linuxserver/ffmpeg for details.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/ffmpeg/config

## Quick Start

```bash
cd /opt/stacks/ffmpeg
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ

## Ports

- `80:80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Mediaserver

---

*Converted from Portainer template to Dockge format*