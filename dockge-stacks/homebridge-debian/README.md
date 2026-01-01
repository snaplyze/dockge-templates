# Homebridge - Debian

Debian Homebridge allows you to integrate with smart home devices that do not natively support HomeKit. There are over 2,000 Homebridge plugins supporting thousands of different smart accessories.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://homebridge.io/Official Docker Documentation: https://github.com/homebridge/homebridge/wiki/Install-Homebridge-on-DockerBringing HomeKit support where there is none

## Quick Start

```bash
cd /opt/stacks/homebridge-debian
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PGID`: PGID
- `PUID`: PUID
- `HOMEBRIDGE_CONFIG_UI`: HOMEBRIDGE_CONFIG_UI
- `HOMEBRIDGE_CONFIG_UI_PORT`: HOMEBRIDGE_CONFIG_UI_PORT
- `TZ`: TZ

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/homebridge` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Homeautomation

---

*Converted from Portainer template to Dockge format*