# JDownloader

JDownloader docker image

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://my.jdownloader.org/Official Docker Documentation: https://github.com/jaymoulin/docker-jdownloaderYoutube Video: Novaspirit Tech - Installing JDownloader and File Browser On The Pi Docker Server

## Quick Start

```bash
cd /opt/stacks/jdownloader
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `MYJD_DEVICE_NAME`: MYJD_DEVICE_NAME
- `MYJD_USER`: MYJD_USER
- `MYJD_PASSWORD`: MYJD_PASSWORD

## Ports

- `3129:3129`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/opt/JDownloader/app/cfg` in container
- `./data/*`: Mapped to `/opt/JDownloader/Downloads` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Downloaders, Tools

---

*Converted from Portainer template to Dockge format*