# Homer

A dead simple static Homepage for your server to keep your services on hand, from a simple yaml configuration file.

## Important Note

This container requires a yml file within the config volume. See the documentation here https://github.com/bastienwirtz/homer

## Quick Start

```bash
cd /opt/stacks/homer
docker compose up -d
```

## Ports

- `8902:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/www/assets` in container
- `./data/*`: Mapped to `/www/config.yml` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Tools, Dashboard

---

*Converted from Portainer template to Dockge format*