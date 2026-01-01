# Plex Media Server

Plex organizes your video, music, and photo collections and streams them to all of your screens.

## Quick Start

```bash
cd /opt/stacks/plex
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PGID`: PGID
- `PUID`: PUID
- `TZ`: TZ
- `VERSION`: VERSION

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/data/tvshows` in container
- `./data/*`: Mapped to `/data/movies` in container
- `./data/*`: Mapped to `/data/music` in container
- `./data/*`: Mapped to `/transcode` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Mediaservervideo, Mediaservermusic, Mediaserverphotos

---

*Converted from Portainer template to Dockge format*