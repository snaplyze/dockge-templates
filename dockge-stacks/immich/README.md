# Immich {shmolf}

Self-hosted backup solution for photos and videos on mobile device.

## Important Note

Application documentation 🗗

## Quick Start

```bash
cd /opt/stacks/immich
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `IMMICH_VERSION`: Immich version
- `DB_USERNAME`: Database username
- `DB_PASSWORD`: Database password
- `DB_DATABASE_NAME`: Database name
- `DB_HOSTNAME`: Database hostname
- `UPLOAD_LOCATION`: File backup location
- `REDIS_HOSTNAME`: Redis hostname
- `PORT`: Http Port

## Source

Template maintainer:  https://github.com/shmolf/portainer-templates/

## Categories

Photos, Backup

---

*Converted from Portainer template to Dockge format*