# Tautulli

Tautulli is a 3rd party application that you can run along side your Plex Media Server to monitor activity and track various statistics. Most importantly, these statistics include what has been watched, who watched it, when and where they watched it, and how it was watched. All statistics are presented in a nice and clean interface with many tables and graphs, which makes it easy to brag about your server to everyone else.

## Important Note

Port 8181 The webui for Tautulli's webuiConfiguration /config - Storing Configuration and the Tautulli database/logs - Map to you plex logs (required for IP logging)

## Quick Start

```bash
cd /opt/stacks/tautulli
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8181:8181`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/logs` in container
- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*