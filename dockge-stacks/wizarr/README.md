# Wizarr

 Wizarr is an advanced user invitation and management system for Jellyfin, Plex, Emby etc. 

## Quick Start

```bash
cd /opt/stacks/wizarr
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `APP_URL`: APP_URL

## Ports

- `5690`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data/database` in container
- `./data/*`: Mapped to `/etc/localtime` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*