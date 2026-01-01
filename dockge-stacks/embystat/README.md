# EmbyStat

Embystat is a personal web server that can calculate all kinds of statistics from your (local) Emby server. Just install this on your server and let him calculate all kinds of fun stuff.

## Important Note

Access the ui at your-ip:6555. Follow the setup wizard on initial install. Then configure the required services.

## Quick Start

```bash
cd /opt/stacks/embystat
docker compose up -d
```

## Ports

- `6555:6555`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*