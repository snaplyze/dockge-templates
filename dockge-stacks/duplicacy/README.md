# Duplicacy

Duplicacy backs up your files to many cloud storages with client-side encryption and the highest level of deduplication

## Quick Start

```bash
cd /opt/stacks/duplicacy
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `TZ`: TZ

## Ports

- `3875`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/logs` in container
- `./data/*`: Mapped to `/cache` in container
- `./data/*`: Mapped to `/source/apps` in container
- `./data/*`: Mapped to `/source/storage` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Utilitybackup

---

*Converted from Portainer template to Dockge format*