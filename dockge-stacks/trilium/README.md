# Trilium

Trilium Notes is a hierarchical note taking application with focus on building large personal knowledge bases

## Quick Start

```bash
cd /opt/stacks/trilium
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `TRILIUM_DATA_DIR`: TRILIUM_DATA_DIR
- `PORT`: PORT

## Ports

- `3388:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/home/node/trilium-data` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Productivity

---

*Converted from Portainer template to Dockge format*