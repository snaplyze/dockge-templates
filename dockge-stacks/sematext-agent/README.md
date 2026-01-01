# Sematext Docker Agent

Collect logs, metrics and docker events

## Quick Start

```bash
cd /opt/stacks/sematext-agent
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `LOGSENE_TOKEN`: Logs token
- `SPM_TOKEN`: SPM monitoring token

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/run/docker.sock` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Logmanagement, Monitoring

---

*Converted from Portainer template to Dockge format*