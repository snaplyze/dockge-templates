# Archivebox

ArchiveBox is a powerful, self-hosted internet archiving solution to collect, save, and view sites you want to preserve offline.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://archivebox.io/Official Docker Documentation: https://github.com/ArchiveBox/ArchiveBox/wiki/DockerBy default an admin user is not created. You can do so by launching a shell in the container and executing 'archivebox manage createsuperuser'. Documentation is Available here.

## Quick Start

```bash
cd /opt/stacks/archivebox
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `ALLOWED_HOSTS`: ALLOWED_HOSTS
- `MEDIA_MAX_SIZE`: MEDIA_MAX_SIZE
- `PUBLIC_INDEX`: PUBLIC_INDEX
- `PUBLIC_SNAPSHOTS`: PUBLIC_SNAPSHOTS
- `PUBLIC_ADD_VIEW`: PUBLIC_ADD_VIEW

## Ports

- `8002:8000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*