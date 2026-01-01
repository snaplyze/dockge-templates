# Mylar

An automated Comic Book downloader (cbr/cbz) for use with SABnzbd, NZBGet and torrents.

## Quick Start

```bash
cd /opt/stacks/mylar
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8090:8090`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/downloads` in container
- `./data/*`: Mapped to `/comics` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Downloaders, Books

---

*Converted from Portainer template to Dockge format*