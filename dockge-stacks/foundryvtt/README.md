# FoundryVTT Server

This docker image provides the FoundryVTT system for hosting your own virtual table top games.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://foundryvtt.com/Official Docker Documentation: https://hub.docker.com/r/felddy/foundryvtt

## Quick Start

```bash
cd /opt/stacks/foundryvtt
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `FOUNDRY_USERNAME`: Foundry Account Name
- `FOUNDRY_PASSWORD`: Foundry Password
- `FOUNDRY_ADMIN_KEY`: Instance Admin Password
- `CONTAINER_PRESERVE_CONFIG`: CONTAINER_PRESERVE_CONFIG

## Ports

- `30000:30000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Games

---

*Converted from Portainer template to Dockge format*