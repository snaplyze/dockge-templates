# Dozzle

Dozzle is a small lightweight application with a web based interface to monitor Docker logs. It doesn’t store any log files. It is for live monitoring of your container logs only.

## Quick Start

```bash
cd /opt/stacks/dozzle
docker compose up -d
```

## Ports

- `8888:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/run/docker.sock` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*