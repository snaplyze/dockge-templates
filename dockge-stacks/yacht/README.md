# Yacht

A web interface for managing docker containers with an emphasis on templating to provide 1 click deployments. Think of it like a decentralized app store for servers that anyone can make packages for.

## Quick Start

```bash
cd /opt/stacks/yacht
docker compose up -d
```

## Ports

- `8001:8000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/var/run/docker.sock` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*