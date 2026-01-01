# Owncloud

ownCloud is a self-hosted file sync and share server. It provides access to your data through a web interface, sync clients or WebDAV while providing a platform to view, sync and share across devices easily—all under your control. ownCloud’s open architecture is extensible via a simple but powerful API for applications and plugins and it works with any storage.

## Important Note

The database user is owncloud and the database is owncloud.

## Quick Start

```bash
cd /opt/stacks/owncloud
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `OWNCLOUD_DOMAIN`: OWNCLOUD_DOMAIN
- `DB_PASSWORD`: DB_PASSWORD
- `ADMIN_USERNAME`: ADMIN_USERNAME
- `ADMIN_PASSWORD`: ADMIN_PASSWORD
- `PORT`: PORT

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Cloud, Productivity, Tools, Web

---

*Converted from Portainer template to Dockge format*