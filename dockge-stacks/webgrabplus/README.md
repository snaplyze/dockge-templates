# WebGrab+Plus

WebGrab+Plus is a multi-site incremental xmltv epg grabber. It collects tv-program guide data from selected tvguide sites for your favourite channels.

## Important Note

Configuration /config - This is where WebGrab+Plus will store it's configuration/data - This is where tv_grab_wg script in the Tvheadend container looks for the guide.xml file.

## Quick Start

```bash
cd /opt/stacks/webgrabplus
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Downloaders

---

*Converted from Portainer template to Dockge format*