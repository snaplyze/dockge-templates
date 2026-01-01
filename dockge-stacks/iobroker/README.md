# iobroker

IoBroker is a open source IoT platform written in JavaScript that easily connects smarthome components from different manufactures. With the help of plugins (called: adapters) ioBroker is able to communicate with a big variety of IoT hardware and services using different protocols and APIs.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://github.com/buanet/ioBroker.dockerOfficial Docker Documentation: https://github.com/buanet/ioBroker.docker

## Quick Start

```bash
cd /opt/stacks/iobroker
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8081:8081`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/opt/iobroker` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Homeautomation

---

*Converted from Portainer template to Dockge format*