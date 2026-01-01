# Twitch Points Miner

A simple script that will watch a stream for you and earn the channel points.

## Important Note

Requires run.py, this is your starter script with your configuration. Please copy and modify accordingly Here

## Quick Start

```bash
cd /opt/stacks/twitch-points-miner
docker compose up -d
```

## Ports

- `5000:5000`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/usr/src/app/run.py` in container
- `./data/*`: Mapped to `/usr/src/app/cookies` in container
- `./data/*`: Mapped to `/usr/src/app/logs` in container
- `./data/*`: Mapped to `/usr/src/app/analytics` in container

## Source

Template maintainer:  https://github.com/Qballjos/portainer_templates/

## Categories

Tools, Other

---

*Converted from Portainer template to Dockge format*