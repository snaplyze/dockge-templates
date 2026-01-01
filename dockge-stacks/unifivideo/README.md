# UniFi Video

UniFi Video is a powerful and flexible, integrated IP video management surveillance system designed to work with Ubiquiti’s UniFi Video Camera product line. UniFi Video has an intuitive, configurable, and feature‑packed user interface with advanced features such as motion detection, auto‑discovery, user‑level security, storage management, reporting, and mobile device support.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://github.com/pducharme/UniFi-Video-ControllerOfficial Docker Documentation: https://github.com/pducharme/UniFi-Video-Controller

## Quick Start

```bash
cd /opt/stacks/unifivideo
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `UMASK`: UMASK
- `CONTEXT_PATH`: CONTEXT_PATH

## Ports

- `1935:1935`: Service port
- `7444:7444`: Service port
- `7447:7447`: Service port
- `6666:6666`: Service port
- `7442:7442`: Service port
- `7080:7080`: Service port
- `7443:7443`: Service port
- `7445:7445`: Service port
- `7446:7446`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/recordings` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Cctv

---

*Converted from Portainer template to Dockge format*