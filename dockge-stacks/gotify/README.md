# Gotify

A simple server for sending and receiving messages

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://gotify.net/Official Docker Documentation: https://gotify.net/docs/installARM7 Image. Documentation is Available here.

## Quick Start

```bash
cd /opt/stacks/gotify
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `TZ`: TZ
- `GOTIFY_DEFAULTUSER_NAME`: GOTIFY_DEFAULTUSER_NAME
- `GOTIFY_DEFAULTUSER_PASS`: GOTIFY_DEFAULTUSER_PASS

## Ports

- `9008:80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/app/data` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*