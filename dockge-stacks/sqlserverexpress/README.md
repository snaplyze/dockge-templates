# SQL Server Express

Microsoft SQL Server Express for Windows containers

## Important Note

Password needs to include at least 8 characters including uppercase, lowercase letters, base-10 digits and/or non-alphanumeric symbols.

## Quick Start

```bash
cd /opt/stacks/sqlserverexpress
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `ACCEPT_EULA`: ACCEPT_EULA
- `sa_password`: SA password

## Ports

- `1433`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `C:/temp/` in container

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Database

---

*Converted from Portainer template to Dockge format*