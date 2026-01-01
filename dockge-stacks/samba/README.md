# Samba

Samba has provided secure, stable and fast file and print services for all clients using the SMB/CIFS protocol, such as all versions of DOS and Windows, OS/2, Linux and many others.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://www.samba.org/Official Docker Documentation: https://github.com/dperson/sambaYoutube Videos:Novaspirit Tech - Setting up Raspberry Pi Samba Server For File Sharing on DockerNovaspirit Tech - Building NAS with Container

## Quick Start

```bash
cd /opt/stacks/samba
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `USERID`: USERID
- `GROUPID`: GROUPID
- `USER`: USER
- `PERMISSIONS`: PERMISSIONS
- `SHARE`: SHARE

## Ports

- `139:139`: Service port
- `445:445`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/share` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*