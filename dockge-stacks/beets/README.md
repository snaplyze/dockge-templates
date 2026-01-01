# Beets

The purpose of beets is to get your music collection right once and for all. It catalogs your collection, automatically improving its metadata as it goes using the MusicBrainz database. Then it provides a bouquet of tools for manipulating and accessing your music.

## Quick Start

```bash
cd /opt/stacks/beets
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8337:8337`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/downloads` in container
- `./data/*`: Mapped to `/music` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Music

---

*Converted from Portainer template to Dockge format*