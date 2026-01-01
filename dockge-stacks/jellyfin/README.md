# Jellyfin

Jellyfin is a Free Software Media System that puts you in control of managing and streaming your media. It is an alternative to the proprietary Emby and Plex, to provide media from a dedicated server to end-user devices via multiple apps.

## Quick Start

```bash
cd /opt/stacks/jellyfin
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ

## Ports

- `8096:8096`: Service port
- `8920:8920`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/data/tvshows` in container
- `./data/*`: Mapped to `/data/movies` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Video, Music, Photos

---

*Converted from Portainer template to Dockge format*