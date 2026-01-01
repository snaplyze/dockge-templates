# Muximux

A lightweight portal to view, manage your HTPC apps without having to run anything more than a PHP enabled webserver. With Muximux you don't need to keep multiple tabs open, or bookmark the URL to all of your apps.

## Quick Start

```bash
cd /opt/stacks/muximux
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

Web, Tools

---

*Converted from Portainer template to Dockge format*