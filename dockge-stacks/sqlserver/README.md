# SQL Server

Microsoft SQL Server on Linux

## Important Note

Password needs to include at least 8 characters including uppercase, lowercase letters, base-10 digits and/or non-alphanumeric symbols.

## Quick Start

```bash
cd /opt/stacks/sqlserver
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `ACCEPT_EULA`: ACCEPT_EULA
- `SA_PASSWORD`: SA password

## Ports

- `1433`: Service port

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Database

---

*Converted from Portainer template to Dockge format*