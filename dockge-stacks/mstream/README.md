# Mstream

Mstream is a personal music streaming server. You can use mStream to stream your music from your home computer to any device, anywhere. There are mobile apps available for both Android and iPhone.

## Quick Start

```bash
cd /opt/stacks/mstream
docker compose up -d
```

## Ports

- `3000:3000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/music` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Music

---

*Converted from Portainer template to Dockge format*