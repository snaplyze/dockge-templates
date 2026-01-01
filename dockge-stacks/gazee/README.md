# Gazee

A WebApp Comic Reader for your favorite digital comics. Reach and read your comic library from any web connected device with a modern web browser.

## Quick Start

```bash
cd /opt/stacks/gazee
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/comics` in container
- `./data/*`: Mapped to `/mylar` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Web, Books, Tools

---

*Converted from Portainer template to Dockge format*