# Resilio Sync

Resilio Sync (formerly BitTorrent Sync) uses the BitTorrent protocol to sync files and folders between all of your devices. There are both free and paid versions, this container supports both.

## Quick Start

```bash
cd /opt/stacks/resilio-sync
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/sync` in container
- `./data/*`: Mapped to `/downloads` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Backup, Cloud, Tools

---

*Converted from Portainer template to Dockge format*