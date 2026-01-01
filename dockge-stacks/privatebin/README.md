# PrivateBin

PrivateBin is a minimalist, open source online pastebin where the server has zero knowledge of pasted data!
  

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://privatebin.info/Official Docker Documentation: https://hub.docker.com/r/privatebin/nginx-fpm-alpine

## Quick Start

```bash
cd /opt/stacks/privatebin
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8080:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/srv/data` in container
- `./data/*`: Mapped to `/srv/cfg` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Cloud, Productivity, Tools, Web

---

*Converted from Portainer template to Dockge format*