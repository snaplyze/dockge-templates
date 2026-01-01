# Swarm monitoring

Monitor your cluster performances with Prometheus & Grafana

## Important Note

Requires Docker version 19.03.0+. Make sure to add the monitoring == true one of your Swarm manager node before deploying this stack.

## Quick Start

```bash
cd /opt/stacks/swarmmonitoring
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `GRAFANA_USER`: Grafana admin user
- `GRAFANA_PASSWORD`: Grafana admin password

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Monitoring

---

*Converted from Portainer template to Dockge format*