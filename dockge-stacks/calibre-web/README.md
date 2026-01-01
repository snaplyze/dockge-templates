# Calibre Web

Calibre Web is a web app providing a clean interface for browsing, reading and downloading eBooks using an existing Calibre database.

## Important Note

Configuration /config - Where Calibre-web should store it's database/books - Path to your calibre library metadata.db file

## Quick Start

```bash
cd /opt/stacks/calibre-web
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8083:8083`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/books` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Cloud, Books

---

*Converted from Portainer template to Dockge format*