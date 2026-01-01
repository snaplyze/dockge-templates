# McMyAdmin 2

McMyAdmin 2 is the leading web control panel and administration console for Minecraft servers.

## Quick Start

```bash
cd /opt/stacks/mcmyadmin2
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8080:8080`: Service port
- `25565:25565`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/minecraft` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Other

---

*Converted from Portainer template to Dockge format*