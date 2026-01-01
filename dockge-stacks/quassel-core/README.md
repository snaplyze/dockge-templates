# quassel-core

Quassel IRC is a modern, cross-platform, distributed IRC client, meaning that one (or multiple) client(s) can attach to and detach from a central core -- much like the popular combination of screen and a text-based IRC client such as WeeChat, but graphical. Blowfish support and optional web-ui included.

## Quick Start

```bash
cd /opt/stacks/quassel-core
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PGID`: PGID
- `PUID`: PUID
- `TZ`: TZ

## Ports

- `4242`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/dnburgess/self-hosted-template/

---

*Converted from Portainer template to Dockge format*