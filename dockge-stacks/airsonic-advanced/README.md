# Airsonic-advanced

[Airsonic-advanced](https://github.com/airsonic-advanced/airsonic-advanced) is a free, web-based media streamer, providing ubiquitious access to your music. Use it to share your music with friends, or to listen to your own music while at work. You can stream to multiple players simultaneously, for instance to one player in your kitchen and another in your living room.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.mkdir -p /volume1/docker/airsonic-advanced/configmkdir -p /volume1/docker/airsonic-advanced/musicmkdir -p /volume1/docker/airsonic-advanced/playlistsmkdir -p /volume1/docker/airsonic-advanced/podcastsmkdir -p /volume1/docker/airsonic-advanced/media

## Quick Start

```bash
cd /opt/stacks/airsonic-advanced
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `CONTEXT_PATH`: CONTEXT_PATH
- `JAVA_OPTS`: JAVA_OPTS

## Ports

- `4040:4040`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container
- `./data/*`: Mapped to `/music` in container
- `./data/*`: Mapped to `/playlists` in container
- `./data/*`: Mapped to `/podcasts` in container
- `./data/*`: Mapped to `/media` in container

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Musicserver

---

*Converted from Portainer template to Dockge format*