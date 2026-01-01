# SearXNG

Open-Source Privacy-respecting metasearch engine

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://docs.searxng.org/Official Docker Documentation: https://docs.searxng.org/admin/installation-docker.htmlPi-Hosted dedicated documentation: searxng.md

## Quick Start

```bash
cd /opt/stacks/searxng
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `BASE_URL`: BASE_URL
- `INSTANCE_NAME`: INSTANCE_NAME

## Ports

- `9017:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/etc/searxng` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*