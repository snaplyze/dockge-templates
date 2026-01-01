# UniFi Controller

The Unifi-controller Controller software is a powerful, enterprise wireless software engine ideal for high-density client deployments requiring low latency and high uptime performance.

## Quick Start

```bash
cd /opt/stacks/unifi-controller
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `3478:3478`: Service port
- `10001:10001`: Service port
- `8080:8080`: Service port
- `8081:8081`: Service port
- `8443:8443`: Service port
- `8843:8843`: Service port
- `8880:8880`: Service port
- `6789:6789`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Management, Tools

---

*Converted from Portainer template to Dockge format*