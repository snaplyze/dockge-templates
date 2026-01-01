# Transmission

Transmission is designed for easy, powerful use. Transmission has the features you want from a BitTorrent client: encryption, a web interface, peer exchange, magnet links, DHT, µTP, UPnP and NAT-PMP port forwarding, webseed support, watch directories, tracker editing, global and per-torrent speed limits, and more.

## Quick Start

```bash
cd /opt/stacks/transmission
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `9091:9091`: Service port
- `51413:51413`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/downloads` in container
- `./data/*`: Mapped to `/watch` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Downloaders

---

*Converted from Portainer template to Dockge format*