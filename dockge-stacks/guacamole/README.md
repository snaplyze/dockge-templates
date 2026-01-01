# Guacamole

A clientless remote desktop gateway.

## Important Note

The default login will be guacadmin/guacadmin. It is common practice to add a new admin user and remove the default user for Guacamole.

## Quick Start

```bash
cd /opt/stacks/guacamole
docker compose up -d
```

## Ports

- `8080:8080`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Remotecontrol

---

*Converted from Portainer template to Dockge format*