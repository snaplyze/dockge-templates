# Nano-wallet

[Nano-wallet](https://nano.org/) is a digital payment protocol designed to be accessible and lightweight, with a focus on removing inefficiencies present in other cryptocurrencies. With ultrafast transactions and zero fees on a secure, green and decentralized network, this makes Nano ideal for everyday transactions. This container is a simple nginx wrapper for the light wallet located [here](https://github.com/linuxserver/nano-wallet). You will need to pass a valid RPC host when accessing this container.

## Important Note

Portainer App Templates by Technorabilia based on data provided by LinuxServer.io.Don't forget to create the volume directories on the host file system.

## Quick Start

```bash
cd /opt/stacks/nano-wallet
docker compose up -d
```

## Ports

- `80:80`: Service port

## Source

Template maintainer:  https://github.com/mycroftwilde/portainer_templates/

## Categories

Tools

---

*Converted from Portainer template to Dockge format*