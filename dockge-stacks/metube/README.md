# MeTube

Web GUI for youtube-dl (using the yt-dlp fork) with playlist support. Allows you to download videos from YouTube and dozens of other sites (https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://hub.docker.com/r/alexta69/metubeOfficial Docker Documentation: https://github.com/alexta69/metube

## Quick Start

```bash
cd /opt/stacks/metube
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8081:8081`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/downloads` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Downloader

---

*Converted from Portainer template to Dockge format*