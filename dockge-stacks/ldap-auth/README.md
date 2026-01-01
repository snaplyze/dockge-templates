# Ldap-auth

[Ldap-auth](https://github.com/nginxinc/nginx-ldap-auth) software is for authenticating users who request protected resources from servers proxied by nginx. It includes a daemon (ldap-auth) that communicates with an authentication server, and a webserver daemon that generates an authentication cookie based on the user’s credentials. The daemons are written in Python for use with a Lightweight Directory Access Protocol (LDAP) authentication server (OpenLDAP or Microsoft Windows Active Directory 2003 and 2012).

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.

## Quick Start

```bash
cd /opt/stacks/ldap-auth
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `TZ`: TZ
- `FERNETKEY`: FERNETKEY
- `CERTFILE`: CERTFILE
- `KEYFILE`: KEYFILE

## Ports

- `8888:8888`: Service port
- `9000:9000`: Service port

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Proxyserver

---

*Converted from Portainer template to Dockge format*