# Mozilla Syncserver

Run-Your-Own Firefox Sync Server

## Quick Start

```bash
cd /opt/stacks/syncserver
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `SYNCSERVER_PUBLIC_URL`: SYNCSERVER_PUBLIC_URL
- `SYNCSERVER_SECRET_FILE`: SYNCSERVER_SECRET_FILE
- `SYNCSERVER_SQLURI`: SYNCSERVER_SQLURI
- `SYNCSERVER_BATCH_UPLOAD_ENABLED`: SYNCSERVER_BATCH_UPLOAD_ENABLED
- `SYNCSERVER_FORCE_WSGI_ENVIRON`: SYNCSERVER_FORCE_WSGI_ENVIRON
- `PORT`: PORT

## Ports

- `5000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*