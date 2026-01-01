# Limnoria

[Limnoria](https://github.com/ProgVal/limnoria) A robust, full-featured, and user/programmer-friendly Python IRC bot, with many existing plugins. Successor of the well-known Supybot.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/limnoria/config

## Quick Start

```bash
cd /opt/stacks/limnoria
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ

## Ports

- `8080:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Codeserver

---

*Converted from Portainer template to Dockge format*