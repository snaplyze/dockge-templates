# Minecraft Server

This docker image provides a Minecraft Server that will automatically download the latest stable version at startup. You can also run/upgrade to any specific version or the latest snapshot. See the Versions section below for more information.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://www.minecraft.net/en-usOfficial Docker Documentation: https://github.com/itzg/docker-minecraft-server#using-docker-compose

## Quick Start

```bash
cd /opt/stacks/minecraft
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `EULA`: EULA

## Ports

- `25565:25565`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools, Games

---

*Converted from Portainer template to Dockge format*