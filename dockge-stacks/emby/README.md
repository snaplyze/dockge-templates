# Emby

Emby organizes video, music, live TV, and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. This container is packaged as a standalone emby Media Server.

## Quick Start

```bash
cd /opt/stacks/emby
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