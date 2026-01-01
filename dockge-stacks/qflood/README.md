# qFlood

A docker image with qBittorrent and the Flood UI, also optional WireGuard VPN support. See the official documentation for WireGuard VPN support at https://hotio.dev/containers/qflood/

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://hotio.dev/containers/qflood/Official Docker Documentation: https://hotio.dev/containers/qflood/The default qBittorrent username is admin and the default password is adminadmin.

## Quick Start

```bash
cd /opt/stacks/qflood
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `UMASK`: UMASK
- `TZ`: TZ
- `FLOOD_AUTH`: FLOOD_AUTH

## Ports

- `3000:3000`: Service port
- `8080:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/app/qBittorrent/downloads` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Downloaders

---

*Converted from Portainer template to Dockge format*