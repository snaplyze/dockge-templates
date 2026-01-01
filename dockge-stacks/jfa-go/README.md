# Jellyfin-Accounts

jfa-go is a user management app for Jellyfin (and now Emby) that provides invite-based account creation as well as other features that make one's instance much easier to manage.

## Important Note

Template created by Pi-Hosted SeriesCheck our Github page: https://github.com/pi-hosted/pi-hostedOfficial Webpage: https://jfa-go.com/Official Docker Documentation: https://wiki.jfa-go.com/This system is setup to work with either Emby or Jellyfin out of the box.  During the initial setup the user will have the option of which server they will be administering.

## Quick Start

```bash
cd /opt/stacks/jfa-go
docker compose up -d
```

## Ports

- `8056:8056`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/jf` in container
- `./data/*`: Mapped to `/data` in container
- `./data/*`: Mapped to `/etc/localtime` in container

## Source

Template maintainer:  https://github.com/novaspirit/pi-hosted/

## Categories

Video, Music, Photos, Management

---

*Converted from Portainer template to Dockge format*