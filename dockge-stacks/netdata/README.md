# Netdata

Troubleshoot slowdowns and anomalies in your infrastructure with thousands of per-second metrics, meaningful visualizations, and insightful health alarms with zero configuration.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://www.netdata.cloud/Official Docker Documentation: https://learn.netdata.cloud/docs/agent/packaging/dockerDocumentation is Available here.

## Quick Start

```bash
cd /opt/stacks/netdata
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `DOCKER_USR`: DOCKER_USR
- `DOCKER_GRP`: DOCKER_GRP

## Ports

- `19999:19999`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/etc/netdata` in container
- `./data/*`: Mapped to `/var/lib/netdata` in container
- `./data/*`: Mapped to `/host/etc/passwd:ro` in container
- `./data/*`: Mapped to `/host/etc/group:ro` in container
- `./data/*`: Mapped to `/host/proc:ro` in container
- `./data/*`: Mapped to `/host/sys:ro` in container
- `./data/*`: Mapped to `/host/etc/os-release:ro` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*