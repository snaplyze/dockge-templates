# ArchiSteamFarm

C# application with primary purpose of farming Steam cards from multiple accounts simultaneously.

## Important Note

Requires an ASF.json with headless enabled, IPCPassword set and an IPC.config described by the wiki in order to work. Please generate the former here and copy the latter from here.

## Quick Start

```bash
cd /opt/stacks/archisteamfarm
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID

## Ports

- `1242:1242`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/app/config` in container
- `./data/*`: Mapped to `/app/plugins/customplugins` in container
- `./data/*`: Mapped to `/app/logs` in container

## Source

Template maintainer:  https://github.com/Qballjos/portainer_templates/

## Categories

Other, Tools

---

*Converted from Portainer template to Dockge format*