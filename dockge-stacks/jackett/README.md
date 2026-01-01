# Jackett

Jackett works as a proxy server it translates queries from apps like Sonarr etc into tracker-site-specific http queries and parses the html response sending results back to the requesting software.

## Quick Start

```bash
cd /opt/stacks/jackett
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `9117:9117`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/downloads` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Downloaders, Tools

---

*Converted from Portainer template to Dockge format*