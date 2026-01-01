# Syslog-ng

[syslog-ng](https://www.syslog-ng.com/products/open-source-log-management/) allows you to flexibly collect, parse, classify, rewrite and correlate logs from across your infrastructure and store or route them to log analysis tools.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/syslog-ng/config

## Quick Start

```bash
cd /opt/stacks/syslog-ng
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ

## Ports

- `514:5514`: Service port
- `601:6601`: Service port
- `6514:6514`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/var/log` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Taskserver

---

*Converted from Portainer template to Dockge format*