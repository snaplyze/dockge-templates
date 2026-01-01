# Traefik

Cloud-Native Networking Stack That Just Works.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://doc.traefik.io/traefik/Official Docker Documentation: https://doc.traefik.io/traefik/getting-started/install-traefik/Pre-installation script must be RAN before you install: wget -qO- https://raw.githubusercontent.com/pi-hosted/pi-hosted/master/tools/traefik.sh | bashA simple and lightweight reverse proxy

## Quick Start

```bash
cd /opt/stacks/traefik
docker compose up -d
```

## Ports

- `80:80`: Service port
- `443:443`: Service port
- `8080:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/traefik.yml` in container
- `./data/*`: Mapped to `/config.yml` in container
- `./data/*`: Mapped to `/acme.json` in container
- `./data/*`: Mapped to `/var/run/docker.sock` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Proxy, Security, Tools

---

*Converted from Portainer template to Dockge format*