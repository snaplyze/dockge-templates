# Radarr

Radarr - A fork of Sonarr to work with movies à la Couchpotato.

## Quick Start

```bash
cd /opt/stacks/radarr
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `7878:7878`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/downloads` in container
- `./data/*`: Mapped to `/movies` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Downloaders, Video

---

*Converted from Portainer template to Dockge format*