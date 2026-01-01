# qBittorrent

The qBittorrent project aims to provide an open-source software alternative to µTorrent. qBittorrent is based on the Qt toolkit and libtorrent-rasterbar library.

## Quick Start

```bash
cd /opt/stacks/qbittorrent
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `6881:6881`: Service port
- `6881:6881`: Service port
- `8080:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/downloads` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Downloaders

---

*Converted from Portainer template to Dockge format*