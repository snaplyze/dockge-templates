# GitLab CE

Open-source end-to-end software development platform

## Important Note

Default username is root. Check the GitLab documentation to get started.

## Quick Start

```bash
cd /opt/stacks/gitlabce
docker compose up -d
```

## Ports

- `80`: Service port
- `443`: Service port
- `22`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/etc/gitlab` in container
- `./data/*`: Mapped to `/var/log/gitlab` in container
- `./data/*`: Mapped to `/var/opt/gitlab` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Development, Projectmanagement

---

*Converted from Portainer template to Dockge format*