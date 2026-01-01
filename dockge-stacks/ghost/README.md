# Ghost

Free and open-source blogging platform

## Important Note

Access the blog management interface under /ghost/.

## Quick Start

```bash
cd /opt/stacks/ghost
docker compose up -d
```

## Ports

- `2368`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/lib/ghost/content` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Blog

---

*Converted from Portainer template to Dockge format*