# Piwigo

Piwigo is photo gallery software for the web, built by an active community of users and developers.

## Quick Start

```bash
cd /opt/stacks/piwigo
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

Photos

---

*Converted from Portainer template to Dockge format*