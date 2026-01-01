# Murmur

Mumble is a voicechat program for gamers written on top of Qt and Opus. Murmur is the server backend for Mumble.

## Quick Start

```bash
cd /opt/stacks/murmur
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ

## Ports

- `64738:64738`: Service port
- `64738:64738`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/etc/localtime` in container
- `./data/*`: Mapped to `/opt/murmur/config` in container
- `./data/*`: Mapped to `/opt/murmur/data` in container
- `./data/*`: Mapped to `/opt/murmur/log` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Voice, Chat

---

*Converted from Portainer template to Dockge format*