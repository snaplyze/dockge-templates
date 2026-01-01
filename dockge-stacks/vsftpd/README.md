# vsftpd FTP Server

Secure, fast FTP server for UNIX-like systems

## Quick Start

```bash
cd /opt/stacks/vsftpd
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `ADDRESS`: ADDRESS
- `USERS`: USERS

## Ports

- `21`: Service port
- `21000`: Service port
- `21001`: Service port
- `21002`: Service port
- `21003`: Service port
- `21004`: Service port
- `21005`: Service port
- `21006`: Service port
- `21007`: Service port
- `21008`: Service port
- `21009`: Service port
- `21010`: Service port

## Data Volumes

Your data is stored in:

- `./data/*`: Mapped to `/home/depot/tvshows` in container
- `./data/*`: Mapped to `/home/depot/movies` in container
- `./data/*`: Mapped to `/home/depot/music` in container
- `./data/*`: Mapped to `/home/depot/ebooks` in container
- `./data/*`: Mapped to `/home/depot/photos` in container
- `./data/*`: Mapped to `/home/depot/documents` in container
- `./data/*`: Mapped to `/home/depot/downloads` in container
- `./data/*`: Mapped to `/home/depot/software` in container
- `./data/*`: Mapped to `/home/depot/blackhole` in container
- `./data/*`: Mapped to `/home/depot/processing` in container

## Source

Template maintainer:  https://github.com/mediadepot/templates/

## Categories

Networkother, Utilities

---

*Converted from Portainer template to Dockge format*