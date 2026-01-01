# Cloud Commander

Cloud Commander a file manager for the web with console and editor.

## Quick Start

```bash
cd /opt/stacks/cloudcmd
docker compose up -d
```

## Ports

- `8000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/media/host/opt/mediadepot` in container
- `./data/*`: Mapped to `/media/host/media/storage` in container
- `./data/*`: Mapped to `/media/host/media/temp` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Documents, Networkother, Tools

---

*Converted from Portainer template to Dockge format*