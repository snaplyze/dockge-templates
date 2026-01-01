# Homarr-Secured

Homarr is a simple and lightweight homepage for your server, that helps you easily access all of your services in one place.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://homarr.vercel.app/Official Docker Documentation: https://github.com/ajnart/homarrThis version does not allow for interaction with the docker environment for security purposes.

## Quick Start

```bash
cd /opt/stacks/homarr-secured
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `7575:7575`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/app/data/configs` in container
- `./data/*`: Mapped to `/app/public/icons` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Tools, Web, Other

---

*Converted from Portainer template to Dockge format*