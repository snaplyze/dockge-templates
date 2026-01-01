# Rsnapshot

[Rsnapshot](http://www.rsnapshot.org/) is a filesystem snapshot utility based on rsync. rsnapshot makes it easy to make periodic snapshots of local machines, and remote machines over ssh. The code makes extensive use of hard links whenever possible, to greatly reduce the disk space required.'

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/rsnapshot/configmkdir -p /volume1/docker/rsnapshot/.snapshotsmkdir -p /volume1/docker/rsnapshot/data

## Quick Start

```bash
cd /opt/stacks/rsnapshot
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ

## Ports

- `80:80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/.snapshots` in container
- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Backupandsyncserver

---

*Converted from Portainer template to Dockge format*