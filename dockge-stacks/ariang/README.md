# AriaNG

AriaNg is a modern web frontend making aria2 easier to use. AriaNg is written in pure html & javascript, thus it does not need any compilers or runtime environment. You can just put AriaNg in your web server and open it in your browser. AriaNg uses responsive layout, and supports any desktop or mobile devices.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://github.com/hurlenko/aria2-ariang-dockerOfficial Docker Documentation: https://github.com/hurlenko/aria2-ariang-docker

## Quick Start

```bash
cd /opt/stacks/ariang
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `ARIA2RPCPORT`: ARIA2RPCPORT

## Ports

- `8080:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/aria2/conf` in container
- `./data/*`: Mapped to `/aria2/data` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Downloader

---

*Converted from Portainer template to Dockge format*