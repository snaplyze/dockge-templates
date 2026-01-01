# Tvheadend

Tvheadend is a TV streaming server and recorder for Linux, FreeBSD and Android supporting DVB-S, DVB-S2, DVB-C, DVB-T, ATSC, ISDB-T, IPTV, SAT&gt;IP and HDHomeRun as input sources. Tvheadend offers the HTTP (VLC, MPlayer), HTSP (Kodi, Movian) and SAT&gt;IP streaming. Multiple EPG sources are supported (over-the-air DVB and ATSC including OpenTV DVB extensions, XMLTV, PyXML).

## Quick Start

```bash
cd /opt/stacks/tvheadend
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `9981:9981`: Service port
- `9982:9982`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/recordings` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Video, Other

---

*Converted from Portainer template to Dockge format*