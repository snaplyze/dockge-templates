# NUT Server

The purpose of NUT Server is to monitor a UPS attached device

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://networkupstools.orgOfficial Docker Documentation: https://hub.docker.com/r/instantlinux/nut-upsd

## Quick Start

```bash
cd /opt/stacks/nutserver
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `SERIAL`: SERIAL
- `NAME`: NAME
- `VENDOR ID`: VENDOR ID
- `API_PASSWORD`: API_PASSWORD
- `DESCRIPTION`: DESCRIPTION

## Ports

- `3493:3493`: Service port

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*