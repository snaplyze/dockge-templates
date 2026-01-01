# DeeMix

Deemix is a deezer downloader built from the ashes of Deezloader Remix.

## Important Note

Deemix may take a few minutes to install. Be sure to check the logs for details. Refer to this page for userToken details.

## Quick Start

```bash
cd /opt/stacks/deemix
docker compose up -d
```

## Ports

- `6595:6595`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/downloads` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Music

---

*Converted from Portainer template to Dockge format*