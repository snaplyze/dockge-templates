# Organizr v2

Organizr allows you to setup Tabs that will be loaded all in one webpage. You can then work on your server with ease.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://organizr.app/Official Docker Documentation: https://hub.docker.com/r/organizr/organizr

## Quick Start

```bash
cd /opt/stacks/organizr-v2
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `7171:80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*