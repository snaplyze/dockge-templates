# Rdesktop

[Rdesktop](http://xrdp.org/) - Ubuntu based containers containing full desktop environments in officially supported flavors accessible via RDP.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/rdesktop/config

## Quick Start

```bash
cd /opt/stacks/rdesktop
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ

## Ports

- `3389:3389`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/run/docker.sock` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Managementutilityserver

---

*Converted from Portainer template to Dockge format*