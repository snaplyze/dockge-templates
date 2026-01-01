# Registry (cache)

Docker image registry configured as a DockerHub pull through cache

## Quick Start

```bash
cd /opt/stacks/registrycache
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `REGISTRY_PROXY_REMOTEURL`: REGISTRY_PROXY_REMOTEURL

## Ports

- `5000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/lib/registry` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Docker

---

*Converted from Portainer template to Dockge format*