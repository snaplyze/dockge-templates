# Unmanic

Unmanic is a simple tool for optimising your file library. You can use it to convert your files into a single, uniform format, manage file movements based on timestamps, or execute custom commands against a file based on its file size.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://docs.unmanic.app/Official Docker Documentation: https://docs.unmanic.app/docs/installation/docker

## Quick Start

```bash
cd /opt/stacks/unmanic
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8888:8888`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/library` in container
- `./data/*`: Mapped to `/tmp/unmanic` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*