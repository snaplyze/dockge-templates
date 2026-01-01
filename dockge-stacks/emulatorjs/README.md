# Emulatorjs

[Emulatorjs](https://github.com/linuxserver/emulatorjs) - In browser web based emulation portable to nearly any device for many retro consoles. A mix of emulators is used between Libretro and EmulatorJS.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/emulatorjs/configmkdir -p /volume1/docker/emulatorjs/data

## Quick Start

```bash
cd /opt/stacks/emulatorjs
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `SUBFOLDER`: SUBFOLDER

## Ports

- `3000:3000`: Service port
- `80:80`: Service port
- `4001:4001`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Gamingserver

---

*Converted from Portainer template to Dockge format*