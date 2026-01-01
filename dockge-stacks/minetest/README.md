# Minetest

Server version of minetest, a free, open source alternative to minecraft.

## Quick Start

```bash
cd /opt/stacks/minetest
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `30000:30000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config/.minetest` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Other

---

*Converted from Portainer template to Dockge format*