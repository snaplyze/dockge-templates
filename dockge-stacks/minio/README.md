# Minio

A distributed object storage server built for cloud applications and devops

## Quick Start

```bash
cd /opt/stacks/minio
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `MINIO_ROOT_USER`: Root user
- `MINIO_ROOT_PASSWORD`: Root password

## Ports

- `9000`: Service port
- `9001`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data` in container
- `./data/*`: Mapped to `/root/.minio` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Storage

---

*Converted from Portainer template to Dockge format*