# Endlessh

[Endlessh](https://github.com/skeeto/endlessh) is an SSH tarpit that very slowly sends an endless, random SSH banner. It keeps SSH clients locked up for hours or even days at a time. The purpose is to put your real SSH server on another port and then let the script kiddies get stuck in this tarpit instead of bothering a real server.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/endlessh/config

## Quick Start

```bash
cd /opt/stacks/endlessh
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `MSDELAY`: MSDELAY
- `MAXLINES`: MAXLINES
- `MAXCLIENTS`: MAXCLIENTS
- `LOGFILE`: LOGFILE
- `BINDFAMILY`: BINDFAMILY

## Ports

- `22:2222`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*