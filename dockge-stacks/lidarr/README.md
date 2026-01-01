# Lidarr

Lidarr is a music collection manager for Usenet and BitTorrent users.

## Quick Start

```bash
cd /opt/stacks/lidarr
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8686:8686`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/downloads` in container
- `./data/*`: Mapped to `/music` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Downloaders, Music

---

*Converted from Portainer template to Dockge format*