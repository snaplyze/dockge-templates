# Healthchecks

[Healthchecks](https://github.com/healthchecks/healthchecks) is a watchdog for your cron jobs. It's a web server that listens for pings from your cron jobs, plus a web interface.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/healthchecks/config

## Quick Start

```bash
cd /opt/stacks/healthchecks
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `SITE_ROOT`: SITE_ROOT
- `SITE_NAME`: SITE_NAME
- `DEFAULT_FROM_EMAIL`: DEFAULT_FROM_EMAIL
- `EMAIL_HOST`: EMAIL_HOST
- `EMAIL_PORT`: EMAIL_PORT
- `EMAIL_HOST_USER`: EMAIL_HOST_USER
- `EMAIL_HOST_PASSWORD`: EMAIL_HOST_PASSWORD
- `EMAIL_USE_TLS`: EMAIL_USE_TLS
- `ALLOWED_HOSTS`: ALLOWED_HOSTS
- `SUPERUSER_EMAIL`: SUPERUSER_EMAIL
- `SUPERUSER_PASSWORD`: SUPERUSER_PASSWORD
- `REGENERATE_SETTINGS`: REGENERATE_SETTINGS
- `SITE_LOGO_URL`: SITE_LOGO_URL
- `SECRET_KEY`: SECRET_KEY
- `APPRISE_ENABLED`: APPRISE_ENABLED

## Ports

- `8000:8000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Taskserver

---

*Converted from Portainer template to Dockge format*