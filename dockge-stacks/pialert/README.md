# Pi.alert

WIFI / LAN intruder detector

## Quick Start

```bash
cd /opt/stacks/pialert
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `20211:20211`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Network

---

*Converted from Portainer template to Dockge format*