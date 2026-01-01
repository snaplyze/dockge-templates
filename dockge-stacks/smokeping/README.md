# SmokePing

SmokePing is a latency logging and graphing and alerting system. It consists of a daemon process which organizes the latency measurements and a CGI which presents the graphs.

## Quick Start

```bash
cd /opt/stacks/smokeping
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Management, Network

---

*Converted from Portainer template to Dockge format*