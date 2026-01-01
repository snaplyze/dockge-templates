# Code-server {shmolf}

Code-server (https://coder.com) is VS Code running on a remote server, accessible through the browser. - Code on your Chromebook, tablet, and laptop with a consistent dev environment. - If you have a Windows or Mac workstation, more easily develop for Linux. - Take advantage of large cloud servers to speed up tests, compilations, downloads, and more. - Preserve battery life when you're on the go. - All intensive computation runs on your server. - You're no longer running excess instances of Chrome.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.This will bind to the following directory on the host filesystem:/portainer/Files/AppData/Config/code-serverProxy Domain: See Documentation 🗗Timezones: See list 🗗

## Quick Start

```bash
cd /opt/stacks/code-server
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PUID`: PUID
- `PGID`: PGID
- `TZ`: TZ
- `PASSWORD`: PASSWORD
- `HASHED_PASSWORD`: HASHED_PASSWORD
- `SUDO_PASSWORD`: SUDO_PASSWORD
- `SUDO_PASSWORD_HASH`: SUDO_PASSWORD_HASH
- `PROXY_DOMAIN`: PROXY_DOMAIN
- `DEFAULT_WORKSPACE`: DEFAULT_WORKSPACE

## Ports

- `8443:8443`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/config` in container

## Source

Template maintainer:  https://github.com/shmolf/portainer-templates/

## Categories

Development

---

*Converted from Portainer template to Dockge format*