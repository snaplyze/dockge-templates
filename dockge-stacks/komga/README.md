# Komga

Koomga Manga, Comic and E-Book Server

## Quick Start

```bash
cd /opt/stacks/komga
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8080:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/books` in container
- `./data/*`: Mapped to `/comics` in container
- `./data/*`: Mapped to `/manga` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Libraryserver

---

*Converted from Portainer template to Dockge format*