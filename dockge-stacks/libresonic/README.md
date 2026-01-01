# libresonic

Libresonic is a free, web-based media streamer, providing ubiqutious access to your music. Use it to share your music with friends, or to listen to your own music while at work. You can stream to multiple players simultaneously, for instance to one player in your kitchen and another in your living room. /music = Location of music. /media = Location of other media. /podcasts = Location of podcasts. /playlists = Location for playlists storage. CONTEXT_PATH is for setting url-base in reverse proxy setups - (optional) Default user/pass is admin/admin

## Quick Start

```bash
cd /opt/stacks/libresonic
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `CONTEXT_PATH`: CONTEXT_PATH
- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ

## Ports

- `4040`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/music` in container
- `./data/*`: Mapped to `/playlists` in container
- `./data/*`: Mapped to `/podcasts` in container
- `./data/*`: Mapped to `/media` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/dnburgess/self-hosted-template/

---

*Converted from Portainer template to Dockge format*