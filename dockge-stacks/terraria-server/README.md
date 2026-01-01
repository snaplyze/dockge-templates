# Terraria Server {shmolf}

Docker container for a Terraria dedicated server.

## Important Note

Link to Official documentation 🗗 for setting up the server.

## Quick Start

```bash
cd /opt/stacks/terraria-server
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `WORLD`: World name

## Ports

- `7777:7777`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/usr/share/tesseract-ocr/5/tessdata` in container

## Source

Template maintainer:  https://github.com/shmolf/portainer-templates/

## Categories

Games

---

*Converted from Portainer template to Dockge format*