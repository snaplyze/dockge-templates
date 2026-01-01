# Scrutiny

WebUI for smartd S.M.A.R.T monitoring

## Quick Start

```bash
cd /opt/stacks/scrutiny
docker compose up -d
```

## Ports

- `8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/scrutiny/config/` in container
- `./data/*`: Mapped to `/run/udev` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Monitoring

---

*Converted from Portainer template to Dockge format*