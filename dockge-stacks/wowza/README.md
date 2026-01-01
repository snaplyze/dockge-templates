# Wowza

Streaming media server

## Quick Start

```bash
cd /opt/stacks/wowza
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `WOWZA_ACCEPT_LICENSE`: Agree to Wowza EULA
- `WOWZA_KEY`: License key

## Ports

- `1935`: Service port
- `8086`: Service port
- `8087`: Service port
- `8088`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/lib/wowza` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Mediaserver

---

*Converted from Portainer template to Dockge format*