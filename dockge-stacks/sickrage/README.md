# SickRage

Automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

## Quick Start

```bash
cd /opt/stacks/sickrage
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PGID`: PGID
- `PUID`: PUID
- `TZ`: TZ

## Ports

- `8081`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/downloads` in container
- `./data/*`: Mapped to `/tv` in container
- `./data/*`: Mapped to `/blackhole` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Downloaders, Mediaappvideo

---

*Converted from Portainer template to Dockge format*