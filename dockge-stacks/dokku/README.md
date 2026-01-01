# Dokku

Dokku setup as a container

## Quick Start

```bash
cd /opt/stacks/dokku
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `DOKKU_HOSTNAME`: Dokku hostname
- `DOKKU_HOST_ROOT`: Dokku host root

## Ports

- `22`: Service port
- `80`: Service port
- `443`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/mnt/dokku` in container
- `./data/*`: Mapped to `/var/run/docker.sock` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Paas

---

*Converted from Portainer template to Dockge format*