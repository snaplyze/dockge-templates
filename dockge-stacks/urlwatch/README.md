# UrlWatch

A tool for monitoring webpages for updates

## Quick Start

```bash
cd /opt/stacks/urlwatch
docker compose up -d
```

## Ports

- `8081`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/srv/urlwatch/config` in container
- `./data/*`: Mapped to `/etc/localtime` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*