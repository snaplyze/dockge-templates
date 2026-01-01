# OpenAMT

OpenAMT Cloud Toolkit

## Important Note

MPS password needs to be 8-32 characters including one uppercase, one lowercase letters, one base-10 digit and one special character.

## Quick Start

```bash
cd /opt/stacks/openamt
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `POSTGRES_USER`: Database user
- `POSTGRES_PASSWORD`: Database password
- `MPS_USER`: MPS user
- `MPS_PASSWORD`: MPS password
- `MPS_COMMON_NAME`: MPS URL
- `MPS_SECRET`: MPS Secret
- `VAULT_SECRET`: Vault secret

## Source

Template maintainer:  https://github.com/portainer/templates/

## Categories

Cloud

---

*Converted from Portainer template to Dockge format*