# Nginx

High performance web server

## Quick Start

```bash
cd /opt/stacks/nginx
docker compose up -d
```

## Ports

- `80`: Service port
- `443`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/etc/nginx` in container
- `./data/*`: Mapped to `/usr/share/nginx/html` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Webserver

---

*Converted from Portainer template to Dockge format*