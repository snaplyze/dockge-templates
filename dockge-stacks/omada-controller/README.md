# Omada EAP Controller

TP-Link Omada is a software-defined network solution. The EAP Controller is used to manage multiple EAPs. Raspberry Pi 1 and Zero are not supported.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://www.tp-link.com/us/business-networking/omada-sdn-controller/Official Docker Documentation: https://hub.docker.com/r/mbentley/omada-controller

## Quick Start

```bash
cd /opt/stacks/omada-controller
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8088:8088`: Service port
- `8043:8043`: Service port
- `27001:27001`: Service port
- `27002:27002`: Service port
- `29810:29810`: Service port
- `29811:29811`: Service port
- `29812:29812`: Service port
- `29813:29813`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Management, Tools

---

*Converted from Portainer template to Dockge format*