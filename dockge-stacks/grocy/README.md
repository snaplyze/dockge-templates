# Grocy

Grocy is an ERP system for your kitchen! Cut down on food waste, and manage your chores with this brilliant utility.

## Quick Start

```bash
cd /opt/stacks/grocy
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: Timezone

## Ports

- `80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Tools, Finance

---

*Converted from Portainer template to Dockge format*