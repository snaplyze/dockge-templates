# Vaultwarden

This is a Bitwarden server API implementation written in Rust compatible with upstream Bitwarden clients*, perfect for self-hosted deployment where running the official resource-heavy service might not be ideal.

## Important Note

This project is not associated with the Bitwarden project nor 8bit Solutions LLC.

## Quick Start

```bash
cd /opt/stacks/vaultwarden
docker compose up -d
```

## Ports

- `80`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*