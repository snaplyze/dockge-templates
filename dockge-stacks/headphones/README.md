# Headphones

Headphones is an automated music downloader for NZB and Torrent, written in Python. It supports SABnzbd, NZBget, Transmission, µTorrent and Blackhole.

## Quick Start

```bash
cd /opt/stacks/headphones
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8181:8181`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/Downloads` in container
- `./data/*`: Mapped to `/music` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Music

---

*Converted from Portainer template to Dockge format*