# MagicMirror2

MagicMirror2 Server

## Quick Start

```bash
cd /opt/stacks/magicmirror2
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8080:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/opt/magic_mirror/config` in container
- `./data/*`: Mapped to `/opt/magic_mirror/modules` in container
- `./data/*`: Mapped to `/opt/magic_mirror/css` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Dashboardserver

---

*Converted from Portainer template to Dockge format*