# Authelia

An open-source authentication and authorization server providing 2-factor authentication and single sign-on (SSO) for your applications via a web portal.

## Important Note

Requires a configuration.yml file in order to work. Documentation is available here.

## Quick Start

```bash
cd /opt/stacks/authelia
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `TZ`: TZ

## Ports

- `9091:9091`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/etc/authelia/` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Tools, Authentication

---

*Converted from Portainer template to Dockge format*