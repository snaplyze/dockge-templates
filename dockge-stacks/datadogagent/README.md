# Datadog agent

Collect events and metrics

## Quick Start

```bash
cd /opt/stacks/datadogagent
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `DD_API_KEY`: Datadog API key

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/run/docker.sock` in container
- `./data/*`: Mapped to `/host/sys/fs/cgroup` in container
- `./data/*`: Mapped to `/host/proc` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Monitoring

---

*Converted from Portainer template to Dockge format*