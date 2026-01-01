# FreshRSS

A free, self-hostable rss aggregator.

## Quick Start

```bash
cd /opt/stacks/freshrss
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Feedreader

---

*Converted from Portainer template to Dockge format*