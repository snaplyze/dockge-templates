# TheLounge

A self-hosted web IRC client.

## Quick Start

```bash
cd /opt/stacks/thelounge
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `9000:9000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Messenger

---

*Converted from Portainer template to Dockge format*