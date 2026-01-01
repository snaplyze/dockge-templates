# Habridge

Habridge emulates Philips Hue API to other home automation gateways such as an Amazon Echo/Dot Gen 1 (gen 2 has issues discovering ha-bridge) or other systems that support Philips Hue.  [https://github.com/bwssytems/ha-bridge/wiki](https://github.com/bwssytems/ha-bridge/wiki)

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/habridge/config

## Quick Start

```bash
cd /opt/stacks/habridge
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `SEC_KEY`: SEC_KEY
- `TZ`: TZ

## Ports

- `8080:8080`: Service port
- `50000:50000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Smarthome

---

*Converted from Portainer template to Dockge format*