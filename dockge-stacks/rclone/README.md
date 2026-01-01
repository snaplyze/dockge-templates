# Rclone Config Backup

Rclone is a command line program to sync files and directories to and from cloud providers (Dropbox, GDrive, Box, etc)

## Quick Start

```bash
cd /opt/stacks/rclone
docker compose up -d
```

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/srv/rclone/config` in container
- `./data/*`: Mapped to `/mnt/data` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Backup, Cloud, Networkother, Tools

---

*Converted from Portainer template to Dockge format*