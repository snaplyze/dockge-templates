# Plex Requests

Simple automated way for users to request new content for Plex.

## Quick Start

```bash
cd /opt/stacks/plexrequests
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `URL_BASE`: URL_BASE

## Ports

- `3000:3000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Downloaders, Video, Tools

---

*Converted from Portainer template to Dockge format*