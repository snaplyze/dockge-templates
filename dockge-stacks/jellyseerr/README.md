# Jellyseerr

Jellyseer is a free and open source software application for managing requests for your media library.

## Quick Start

```bash
cd /opt/stacks/jellyseerr
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `5055:5055`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/app/config` in container

## Source

Template maintainer:  https://github.com/Qballjos/portainer_templates/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*