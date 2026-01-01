# YouTubeDL-Material

YoutubeDL-Material is a Material Design frontend for youtube-dl. It's coded using Angular 9 for the frontend, and Node.js on the backend.

## Quick Start

```bash
cd /opt/stacks/youtubedl-material
docker compose up -d
```

## Ports

- `17442:17442`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/app/appdata` in container
- `./data/*`: Mapped to `/app/video` in container
- `./data/*`: Mapped to `/app/subscriptions` in container
- `./data/*`: Mapped to `/app/users` in container
- `./data/*`: Mapped to `/app/audio` in container

## Source

Template maintainer:  https://github.com/xneo1/portainer_templates/

## Categories

Downloaders

---

*Converted from Portainer template to Dockge format*