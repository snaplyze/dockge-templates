# Codiad

Codiad is a web-based IDE framework with a small footprint and minimal requirements.

## Quick Start

```bash
cd /opt/stacks/codiad
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Productivity

---

*Converted from Portainer template to Dockge format*