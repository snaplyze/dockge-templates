# PhotoShow

A simple, easy way to turn a photo album into a webgallery.

## Quick Start

```bash
cd /opt/stacks/photoshow
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/Pictures` in container
- `./data/*`: Mapped to `/Thumbs` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Photos

---

*Converted from Portainer template to Dockge format*