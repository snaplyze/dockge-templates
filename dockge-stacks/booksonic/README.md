# Booksonic

Booksonic is a server and an app for streaming your audiobooks to any pc or android phone. Most of the functionality is also availiable on other platforms that have apps for subsonic.

## Quick Start

```bash
cd /opt/stacks/booksonic
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `CONTEXT_PATH`: CONTEXT_PATH

## Ports

- `4040:4040`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/books` in container
- `./data/*`: Mapped to `/podcast` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Books

---

*Converted from Portainer template to Dockge format*