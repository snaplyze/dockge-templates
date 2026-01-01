# qdirstat

QDirStat is a graphical application to show where your disk space has gone and to help you to clean it up.

## Quick Start

```bash
cd /opt/stacks/qdirstat
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PGID`: PGID
- `PUID`: PUID

## Ports

- `5800`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/storage/opt` in container
- `./data/*`: Mapped to `/storage/mnt` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Utilities

---

*Converted from Portainer template to Dockge format*