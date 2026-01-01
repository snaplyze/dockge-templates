# Cloud9

[Cloud9](https://github.com/c9/core) Cloud9 is a complete web based IDE with terminal access. This container is for running their core SDK locally and developing plugins.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/cloud9/configmkdir -p /volume1/docker/cloud9/code

## Quick Start

```bash
cd /opt/stacks/cloud9
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `GITURL`: GITURL
- `USERNAME`: USERNAME
- `PASSWORD`: PASSWORD

## Ports

- `8000:8000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/code` in container
- `./data/*`: Mapped to `/var/run/docker.sock` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Codeserver

---

*Converted from Portainer template to Dockge format*