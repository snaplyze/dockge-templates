# Webtop

Webtop - Alpine, Ubuntu, Fedora, and Arch based containers containing full desktop environments in officially supported flavors accessible via any modern web browser.

## Quick Start

```bash
cd /opt/stacks/webtop
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `GUID`: PUID
- `TZ`: TZ

## Ports

- `3000:3000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Other

---

*Converted from Portainer template to Dockge format*