# Logzio Metrics Collector

Docker Metrics Collector is a container that runs Metricbeat with the modules you enable at runtime.

## Quick Start

```bash
cd /opt/stacks/logzio-metrics-collector
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `LOGZIO_TOKEN`: LOGZIO_TOKEN
- `LOGZIO_MODULES`: LOGZIO_MODULES

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/run/docker.sock` in container
- `./data/*`: Mapped to `/hostfs/sys/fs/cgroup` in container
- `./data/*`: Mapped to `/hostfs/proc` in container
- `./data/*`: Mapped to `/hostfs` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*