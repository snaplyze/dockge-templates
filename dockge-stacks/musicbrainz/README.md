# MusicBrainz

MusicBrainz is an open music encyclopedia that collects music metadata and makes it available to the public.

## Quick Start

```bash
cd /opt/stacks/musicbrainz
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `BRAINZCODE`: BRAINZCODE
- `PUID`: PUID
- `PGID`: PGID

## Ports

- `5000:5000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Music, Tools

---

*Converted from Portainer template to Dockge format*