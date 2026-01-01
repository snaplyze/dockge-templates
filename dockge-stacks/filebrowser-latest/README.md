# FileBrowser latest

Web File Browser which can be used as a middleware or standalone app.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://filebrowser.org/Official Docker Documentation: https://filebrowser.org/installation#dockerYoutube Video: Novaspirit Tech - Installing JDownloader and File Browser On The Pi Docker ServerThe default user and password is admin/admin.

## Quick Start

```bash
cd /opt/stacks/filebrowser-latest
docker compose up -d
```

## Ports

- `8082:80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/srv` in container
- `./data/*`: Mapped to `/database/filebrowser.db` in container
- `./data/*`: Mapped to `/config/settings.json` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*