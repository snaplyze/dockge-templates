# Passbolt

Passbolt is a free and open source password manager designed for collaboration. With Passbolt you can securely generate, store, manage and monitor your team credentials. Get access to all of your logins and passwords from multiple browsers or even your mobile phone.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://github.com/pi-hosted/pi-hosted/blob/master/docs/passbolt.mdOfficial Docker Documentation: https://github.com/pi-hosted/pi-hosted/blob/master/docs/passbolt.mdPi-Hosted dedicated documentation: passbolt.md

## Quick Start

```bash
cd /opt/stacks/passbolt
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `MYSQL_ROOT_PASSWORD`: MYSQL_ROOT_PASSWORD
- `MYSQL_DATABASE`: MYSQL_DATABASE
- `MYSQL_USER`: MYSQL_USER
- `MYSQL_PASSWORD`: MYSQL_PASSWORD
- `PASSBOLT_PORT`: PASSBOLT_PORT
- `PASSBOLT_URL`: PASSBOLT_URL
- `EMAIL_FROM_NAME`: EMAIL_FROM_NAME
- `EMAIL_FROM_ADDRESS`: EMAIL_FROM_ADDRESS
- `EMAIL_SMTP_SERVER`: EMAIL_SMTP_SERVER
- `EMAIL_SMTP_PORT`: EMAIL_SMTP_PORT
- `EMAIL_USERNAME`: EMAIL_USERNAME
- `EMAIL_PASSWORD`: EMAIL_PASSWORD
- `EMAIL_TLS`: EMAIL_TLS

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*