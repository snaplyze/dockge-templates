# Deluge

Deluge is a lightweight, Free Software, cross-platform BitTorrent client providing: Full Encryption, WebUI, Plugin System, Much more...

## Quick Start

```bash
cd /opt/stacks/deluge
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `UMASK_SET`: UMASK_SET

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/downloads` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Downloaders

---

*Converted from Portainer template to Dockge format*