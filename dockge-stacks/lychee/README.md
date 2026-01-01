# Lychee

Lychee is a free photo-management tool, which runs on your server or web-space. Installing is a matter of seconds. Upload, manage and share photos like from a native application. Lychee comes with everything you need and all your photos are stored securely.

## Quick Start

```bash
cd /opt/stacks/lychee
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
- `./data/*`: Mapped to `/pictures` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Cloud, Web, Management, Photos

---

*Converted from Portainer template to Dockge format*