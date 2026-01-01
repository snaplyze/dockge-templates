# Kodi Headless

Headless installation of Kodi™ (formerly known as XBMC™), to enable library updates.

## Quick Start

```bash
cd /opt/stacks/kodi-headless
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8080`: Service port
- `9777`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Video

---

*Converted from Portainer template to Dockge format*