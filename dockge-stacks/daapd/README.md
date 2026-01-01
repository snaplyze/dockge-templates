# Daapd

DAAP (iTunes) media server with support for AirPlay devices, Apple Remote (and compatibles), MPD and internet radio.

## Quick Start

```bash
cd /opt/stacks/daapd
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/music` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Music

---

*Converted from Portainer template to Dockge format*