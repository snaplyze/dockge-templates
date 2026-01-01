# ProtonMail Bridge

This is an unofficial Docker container of the ProtonMail Bridge. Some of the scripts are based on Hendrik Meyer's work.

## Important Note

Please refer to the documentation here to set this up.

## Quick Start

```bash
cd /opt/stacks/protonmail-bridge
docker compose up -d
```

## Ports

- `143`: Service port
- `25`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/root` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Email, Productivity, Tools

---

*Converted from Portainer template to Dockge format*