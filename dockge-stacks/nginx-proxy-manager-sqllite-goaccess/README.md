# Nginx Proxy Manager v2 with Sqlite and Goaccess Charts

Nginx Proxy Manager v2 with sqlite and Goaccess Charts enables you to easily forward to your websites running at home or otherwise, including free SSL, without having to know too much about Nginx or Letsencrypt.  Please see the install document at https://github.com/pi-hosted/pi-hosted/tree/master/docs installing the template

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://nginxproxymanager.com/Official Docker Documentation: https://nginxproxymanager.com/setup/#running-the-appPi-Hosted dedicated documentation: nginx_proxy_manager.mdYoutube Video: Novaspirit Tech - Installing Nginx Proxy Manager on Docker

## Quick Start

```bash
cd /opt/stacks/nginx-proxy-manager-sqllite-goaccess
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `SKIP_ARCHIVED_LOGS`: SKIP_ARCHIVED_LOGS
- `BASIC_AUTH`: BASIC_AUTH
- `BASIC_AUTH_USERNAME`: BASIC_AUTH_USERNAME Ignore if Basic Auth set to false
- `BASIC_AUTH_PASSWORD`: BASIC_AUTH_PASSWORD Ignore if Basic Auth set to false

## Ports

- `80:80`: Service port
- `81:81`: Service port
- `443:443`: Service port
- `7880:7880`: Service port

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Proxy, Tools

---

*Converted from Portainer template to Dockge format*