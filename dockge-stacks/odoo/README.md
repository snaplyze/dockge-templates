# Odoo

Open-source business apps

## Quick Start

```bash
cd /opt/stacks/odoo
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `HOST`: PostgreSQL database host
- `USER`: Database user
- `PASSWORD`: Database password

## Ports

- `8069`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/lib/odoo` in container
- `./data/*`: Mapped to `/mnt/extra-addons` in container

## Source

Template maintainer:  https://github.com/mikestraney/portainer-templates/

## Categories

Projectmanagement

---

*Converted from Portainer template to Dockge format*