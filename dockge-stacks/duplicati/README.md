# Duplicati

Free backup software to store encrypted backups online, Duplicati works with standard protocols like FTP, SSH, WebDAV as well as popular services like Microsoft OneDrive, Amazon Cloud Drive and S3, Google Drive, box.com, Mega, hubiC and many others.

## Quick Start

```bash
cd /opt/stacks/duplicati
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `8200:8200`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/tmp` in container
- `./data/*`: Mapped to `/backups` in container
- `./data/*`: Mapped to `/source` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Backup, Cloud, Productivity, Tools

---

*Converted from Portainer template to Dockge format*