# Klipper[Testing], Mainsail, Moonraker

Klipper is a 3d-Printer firmware. It combines the power of a general purpose computer with one or more micro-controllers. See the features document for more information on why you should use Klipper.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://hub.docker.com/r/mkuf/klipperOfficial Docker Documentation: https://hub.docker.com/r/mkuf/klipperPre-installation script must be RAN before you install: wget -qO- https://raw.githubusercontent.com/pi-hosted/pi-hosted/master/tools/install_klipper.sh | bashFirst you will need to download a printer.conf file from https://github.com/Klipper3d/klipper/tree/master/config and copy it to 

## Quick Start

```bash
cd /opt/stacks/klipper-mainsail-moonraker
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `3D_PRINTER_DEVICE`: 3D_PRINTER_DEVICE

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, 3dprinters, Tools

---

*Converted from Portainer template to Dockge format*