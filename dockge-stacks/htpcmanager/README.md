# HTPC Manager

HTPC Manager, a front end for many htpc related applications. Uses the Hellowlol HTPC Manager fork.

## Quick Start

```bash
cd /opt/stacks/htpcmanager
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8085:8085`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Video, Music

---

*Converted from Portainer template to Dockge format*