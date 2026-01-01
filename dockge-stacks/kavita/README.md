# Kavita

Lighting fast with a slick design, Kavita is a rocket fueled self-hosted digital library which supports a vast array of file formats. Install to start reading and share your server with your friends.

## Quick Start

```bash
cd /opt/stacks/kavita
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `5000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/books` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Books

---

*Converted from Portainer template to Dockge format*