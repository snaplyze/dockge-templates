# Droppy

Droppy is a self-hosted file storage server

## Quick Start

```bash
cd /opt/stacks/droppy
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `GID`: GID
- `UID`: UID
- `TZ`: TZ

## Ports

- `8989`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/files/tvshows` in container
- `./data/*`: Mapped to `/files/movies` in container
- `./data/*`: Mapped to `/files/music` in container
- `./data/*`: Mapped to `/files/photos` in container
- `./data/*`: Mapped to `/files/ebooks` in container
- `./data/*`: Mapped to `/files/documents` in container
- `./data/*`: Mapped to `/files/software` in container
- `./data/*`: Mapped to `/files/downloads` in container
- `./data/*`: Mapped to `/files/blackhole` in container
- `./data/*`: Mapped to `/files/processing` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Tools, Networkweb, Networkother

---

*Converted from Portainer template to Dockge format*