# Urbackup

Open-source network backup

## Important Note

This application web interface is exposed on the port 55414 inside the container.

## Quick Start

```bash
cd /opt/stacks/urbackup
docker compose up -d
```

## Ports

- `55413`: Service port
- `55414`: Service port
- `55415`: Service port
- `35622`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/urbackup` in container

## Source

Template maintainer:  https://github.com/mikestraney/portainer-templates/

## Categories

Backup

---

*Converted from Portainer template to Dockge format*