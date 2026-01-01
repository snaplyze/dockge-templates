# Jenkins

Open-source continuous integration tool

## Quick Start

```bash
cd /opt/stacks/jenkins
docker compose up -d
```

## Ports

- `8080`: Service port
- `50000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/var/jenkins_home` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Continuousintegration

---

*Converted from Portainer template to Dockge format*