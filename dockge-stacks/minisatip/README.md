# Minisatip

Minisatip is a multi-threaded satip server version 1.2 that runs under Linux and it was tested with DVB-S, DVB-S2, DVB-T, DVB-T2, DVB-C, DVB-C2, ATSC and ISDB-T cards. The application is designed to stream the requested data to multiple clients (even with one dvb card) at the same time while opening different pids.

## Quick Start

```bash
cd /opt/stacks/minisatip
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8875:8875`: Service port
- `554:554`: Service port
- `1900:1900`: Service port

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Video, Tools

---

*Converted from Portainer template to Dockge format*