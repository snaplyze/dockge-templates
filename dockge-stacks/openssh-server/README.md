# Openssh-server

[Openssh-server](https://www.openssh.com/) is a sandboxed environment that allows ssh access without giving keys to the entire server. Giving ssh access via private key often means giving full access to the server. This container creates a limited and sandboxed environment that others can ssh into. The users only have access to the folders mapped and the processes running inside this container.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/openssh-server/config

## Quick Start

```bash
cd /opt/stacks/openssh-server
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `PUBLIC_KEY`: PUBLIC_KEY
- `PUBLIC_KEY_FILE`: PUBLIC_KEY_FILE
- `PUBLIC_KEY_DIR`: PUBLIC_KEY_DIR
- `PUBLIC_KEY_URL`: PUBLIC_KEY_URL
- `SUDO_ACCESS`: SUDO_ACCESS
- `PASSWORD_ACCESS`: PASSWORD_ACCESS
- `USER_PASSWORD`: USER_PASSWORD
- `USER_PASSWORD_FILE`: USER_PASSWORD_FILE
- `USER_NAME`: USER_NAME

## Ports

- `2222:2222`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Managementutilityserver

---

*Converted from Portainer template to Dockge format*