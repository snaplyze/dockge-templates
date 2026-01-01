# LazyLibrarian

LazyLibrarian is a program to follow authors and grab metadata for all your digital reading needs.

## Quick Start

```bash
cd /opt/stacks/lazylibrarian
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `5299:5299`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/downloads` in container
- `./data/*`: Mapped to `/books` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Books

---

*Converted from Portainer template to Dockge format*