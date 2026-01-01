# NZBGet

NZBGet is a usenet downloader, written in C++ and designed with performance in mind to achieve maximum download speed by using very little system resources. It supports all platforms including Windows, Mac, Linux and works on all devices including PC, NAS, WLAN routers and media players.

## Quick Start

```bash
cd /opt/stacks/nzbget
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `6789:6789`: Service port

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