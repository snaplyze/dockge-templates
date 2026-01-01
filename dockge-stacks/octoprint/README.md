# OctoPrint

OctoPrint is an open source 3D printer controller application, which provides a web interface for the connected printers.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://octoprint.org/Official Docker Documentation: https://hub.docker.com/r/octoprint/octoprint

## Quick Start

```bash
cd /opt/stacks/octoprint
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `NODE_ENV`: NODE_ENV
- `ENABLE_MJPG_STREAMER`: ENABLE_MJPG_STREAMER

## Ports

- `8051:80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/octoprint` in container
- `./data/*`: Mapped to `/dev` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*