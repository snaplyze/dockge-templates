# LLDAP

This project is a lightweight authentication server that provides an opinionated, simplified LDAP interface for authentication.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://github.com/nitnelave/lldapOfficial Docker Documentation: https://github.com/nitnelave/lldapPre-installation script must be RAN before you install: wget -qO- https://raw.githubusercontent.com/pi-hosted/pi-hosted/master/tools/install_lldap.sh | bash

## Quick Start

```bash
cd /opt/stacks/lldap
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `LLDAP_JWT_SECRET`: LLDAP_JWT_SECRET
- `LLDAP_LDAP_USER_PASS`: LLDAP_LDAP_USER_PASS
- `LLDAP_LDAP_BASE_DN`: LLDAP_LDAP_BASE_DN

## Ports

- `3890:3890`: Service port
- `17170:17170`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/data` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Tools, Productivity

---

*Converted from Portainer template to Dockge format*