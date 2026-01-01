# Nginx Proxy Manager v3 [DEVEL] NOT READY FOR USE

[DEVEL] Not ready for production.  Nginx Proxy Manager v3 Develop enables you to easily forward to your websites running at home or otherwise, including free SSL, without having to know too much about Nginx or Letsencrypt.  Please see the install document at https://github.com/pi-hosted/pi-hosted/tree/master/docs installing the template

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://nginxproxymanager.com/Official Docker Documentation: https://nginxproxymanager.com/setup/Pi-Hosted dedicated documentation: nginx_proxy_manager.mdYoutube Video: Novaspirit Tech - Installing Nginx Proxy Manager on Docker

## Quick Start

```bash
cd /opt/stacks/nginx-proxy-manager-v3
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ

## Ports

- `80:80`: Service port
- `81:81`: Service port
- `443:443`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Proxy, Tools

---

*Converted from Portainer template to Dockge format*