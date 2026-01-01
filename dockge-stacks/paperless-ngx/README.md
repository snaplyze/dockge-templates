# Paperless NGX

Paperless-ngx is a document management system that transforms your physical documents into a searchable online archive so you can keep, well, less paper.  Paperless-ngx forked from paperless-ng to continue the great work and distribute responsibility of supporting and advancing the project among a team of people. Consider joining us! Discussion of this transition can be found in issues #1599 and #1632.  A demo is available at demo.paperless-ngx.com using login demo / demo. Note: demo content is reset frequently and confidential information should not be uploaded.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://github.com/paperless-ngx/paperless-ngxOfficial Docker Documentation: https://github.com/paperless-ngx/paperless-ngx

## Quick Start

```bash
cd /opt/stacks/paperless-ngx
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `PAPERLESSURL`: PAPERLESS_URL
- `ADMIN_USER`: Administrator username
- `ADMIN_PASS`: Administrator password
- `RANDOMKEY`: Secret Key
- `LANG`: OCR Language

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Cloud, Management, Productivity

---

*Converted from Portainer template to Dockge format*