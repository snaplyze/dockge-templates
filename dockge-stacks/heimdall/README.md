# Heimdall

Heimdall is a way to organise all those links to your most used web sites and web applications in a simple way.

## Quick Start

```bash
cd /opt/stacks/heimdall
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `80`: Service port
- `443`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Tools, Web, Dashboard

---

*Converted from Portainer template to Dockge format*