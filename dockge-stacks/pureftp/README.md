# Pure-FTP Server

Pure-FTPd is a free (BSD), secure, production-quality and standard-conformant FTP server. 

## Quick Start

```bash
cd /opt/stacks/pureftp
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `FTP_USER_NAME`: FTP_USER_NAME
- `FTP_USER_PASS`: FTP_USER_PASS
- `FTP_USER_HOME`: FTP_USER_HOME
- `FTP_USER_GID`: FTP_USER_GID
- `FTP_USER_UID`: FTP_USER_UID
- `TZ`: TZ
- `PUBLICHOST`: PUBLICHOST

## Ports

- `21`: Service port
- `30000`: Service port
- `30001`: Service port
- `30002`: Service port
- `30003`: Service port
- `30004`: Service port
- `30005`: Service port
- `30006`: Service port
- `30007`: Service port
- `30008`: Service port
- `30009`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/etc/pure-ftpd/passwd` in container
- `./data/*`: Mapped to `/data/tvshows` in container
- `./data/*`: Mapped to `/data/movies` in container
- `./data/*`: Mapped to `/data/music` in container
- `./data/*`: Mapped to `/data/ebooks` in container
- `./data/*`: Mapped to `/data/photos` in container
- `./data/*`: Mapped to `/data/documents` in container
- `./data/*`: Mapped to `/data/downloads` in container
- `./data/*`: Mapped to `/data/software` in container
- `./data/*`: Mapped to `/data/blackhole` in container
- `./data/*`: Mapped to `/data/processing` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Networkother, Utilities

---

*Converted from Portainer template to Dockge format*