# Logzio Logs Collector

Docker container that uses Filebeat to collect logs from other Docker containers and forward those logs to your Logz.io account.

## Quick Start

```bash
cd /opt/stacks/logzio-logs-collector
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `LOGZIO_TOKEN`: LOGZIO_TOKEN
- `LOGZIO_URL`: LOGZIO_URL

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/run/docker.sock` in container
- `./data/*`: Mapped to `/var/lib/docker/containers` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*