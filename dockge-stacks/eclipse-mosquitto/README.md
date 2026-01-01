# Eclipse Mosquitto MQTT

Eclipse Mosquitto is an open source message broker that implements the MQTT protocol versions 5.0, 3.1.1 and 3.1. Mosquitto is lightweight and is suitable for use on all devices from low power single board computers to full servers.
Have a look on https://mosquitto.org/man/mosquitto_passwd-1.html

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://mosquitto.org/Official Docker Documentation: https://mosquitto.org/Pre-installation script must be RAN before you install: wget -qO- https://raw.githubusercontent.com/pi-hosted/pi-hosted/master/tools/install_mosquitto.sh | bash

## Quick Start

```bash
cd /opt/stacks/eclipse-mosquitto
docker compose up -d
```

## Ports

- `1883:1883`: Service port
- `9001:9001`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/mosquitto/config` in container
- `./data/*`: Mapped to `/mosquitto/data` in container
- `./data/*`: Mapped to `/mosquitto/log` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*