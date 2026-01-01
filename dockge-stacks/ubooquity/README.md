# Ubooquity

Ubooquity is a free, lightweight and easy-to-use home server for your comics and ebooks. Use it to access your files from anywhere, with a tablet, an e-reader, a phone or a computer.

## Quick Start

```bash
cd /opt/stacks/ubooquity
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `MAXMEM`: MAXMEM
- `PUID`: PUID
- `PGID`: PGID

## Ports

- `2202:2202`: Service port
- `2203:2203`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/books` in container
- `./data/*`: Mapped to `/comics` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Cloud, Books

---

*Converted from Portainer template to Dockge format*