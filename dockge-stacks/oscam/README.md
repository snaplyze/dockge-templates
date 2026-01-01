# OScam

OScam is a softcam, software to be used to decrypt digital television channels on a settopbox (receiver), as an alternative for a conditional access module (CAM). The main features of OSCam are next to its softcam capabilities, that it is able to function as a cardserver.

## Quick Start

```bash
cd /opt/stacks/oscam
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8888:8888`: Service port
- `10000:10000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Other

---

*Converted from Portainer template to Dockge format*