# Scality S3

Standalone AWS S3 protocol server

## Quick Start

```bash
cd /opt/stacks/scalitys3
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `SCALITY_ACCESS_KEY`: Scality S3 access key
- `SCALITY_SECRET_KEY`: Scality S3 secret key

## Ports

- `8000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/usr/src/app/localData` in container
- `./data/*`: Mapped to `/usr/src/app/localMetadata` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Storage

---

*Converted from Portainer template to Dockge format*