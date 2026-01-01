# Infisical {shmolf}

The open-source secret management platform: Sync secrets/configs across your team/infrastructure and prevent secret leaks.

## Important Note

Application documentation 🗗

## Quick Start

```bash
cd /opt/stacks/infisical
docker compose up -d
```

## Configuration

Edit `.env` file to customize your deployment:

- `PORT`: Http Port
- `ENCRYPTION_KEY`: Encryption Key
- `AUTH_SECRET`: JWT Key
- `POSTGRES_PASSWORD`: Postgres Password
- `POSTGRES_USER`: Postgres User
- `POSTGRES_DB`: Postgres Database
- `DB_CONNECTION_URI`: DB Connection URI
- `SITE_URL`: Website URL
- `REDIS_URL`: Redis URL
- `SMTP_HOST`: Email Host (Optional)
- `SMTP_PORT`: Email Port (Optional)
- `SMTP_NAME`: Email Name (Optional)
- `SMTP_USERNAME`: Email Username (Optional)
- `SMTP_PASSWORD`: Email Password (Optional)
- `CLIENT_ID_HEROKU`: Heroku Client ID (Optional)
- `CLIENT_SECRET_HEROKU`: Heroku Client Secret (Optional)
- `CLIENT_ID_VERCEL`: Vercel Client ID (Optional)
- `CLIENT_SECRET_VERCEL`: Vercel Client Secret (Optional)
- `CLIENT_SLUG_VERCEL`: Vercel Client Slug (Optional)
- `CLIENT_ID_NETLIFY`: Netlify Client ID (Optional)
- `CLIENT_SECRET_NETLIFY`: Netlify Client Secret (Optional)
- `CLIENT_ID_GITHUB`: GitHub Client ID (Optional)
- `CLIENT_SECRET_GITHUB`: GitHub Client Secret (Optional)
- `CLIENT_ID_GITLAB`: GitLab Client ID (Optional)
- `CLIENT_SECRET_GITLAB`: GitLab Client Secret (Optional)
- `CLIENT_ID_BITBUCKET`: Bitbucket Client ID (Optional)
- `CLIENT_SECRET_BITBUCKET`: Bitbucket Client Secret (Optional)
- `SENTRY_DSN`: Sentry DSN (Optional)
- `CLIENT_ID_GOOGLE_LOGIN`: Google Client ID (Optional)
- `CLIENT_SECRET_GOOGLE_LOGIN`: Google Client Secret (Optional)
- `CLIENT_ID_GITHUB_LOGIN`: GitHub Client ID (Optional)
- `CLIENT_SECRET_GITHUB_LOGIN`: GitHub Client Secret (Optional)
- `CLIENT_ID_GITLAB_LOGIN`: GitLab Client ID (Optional)
- `CLIENT_SECRET_GITLAB_LOGIN`: GitLab Client Secret (Optional)
- `CAPTCHA_SECRET`: Captcha Secret (Optional)
- `NEXT_PUBLIC_CAPTCHA_SITE_KEY`: Captcha Site Key (Optional)
- `PLAIN_API_KEY`: Plain API Key (Optional)
- `PLAIN_WISH_LABEL_IDS`: Plain Wish Label IDs (Optional)

## Source

Template maintainer:  https://github.com/shmolf/portainer-templates/

## Categories

Secrets, Management

---

*Converted from Portainer template to Dockge format*