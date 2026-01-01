# Pixel-server

Wireless control of PixelStrips or NeoPixels using a web graphical interface running on a Raspberry Pi.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: http://www.penguintutor.com/projects/pixel-serverOfficial Docker Documentation: https://github.com/Macleykun/pixel-serverPi-Hosted dedicated documentation: pixel-server_setup.mdPre-installation script must be RAN before you install: wget -qO- https://raw.githubusercontent.com/pi-hosted/pi-hosted/master/tools/install_pixel-server.sh | bash

## Quick Start

```bash
cd /opt/stacks/pixel-server
docker compose up -d
```

## Ports

- `85:80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/opt/pixel-server/auth.cfg` in container
- `./data/*`: Mapped to `/opt/pixel-server/pixelserver.cfg` in container
- `./data/*`: Mapped to `/opt/pixel-server/users.cfg` in container
- `./data/*`: Mapped to `/etc/crontabs/` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other

---

*Converted from Portainer template to Dockge format*