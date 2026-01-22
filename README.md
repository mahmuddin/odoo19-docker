# Odoo 19 Community - Docker Setup

This project runs Odoo 19 Community Edition using Docker and Docker Compose, optimized for a lightweight footprint with Alpine images.

## Prerequisites

- Docker
- Docker Compose

## Quick Start
1. **Clone the repository** (if not already):
   ```bash
   git clone <repository-url>
   cd odoo19-docker
   ```

2. **Start the services**:
   ```bash
   docker compose up -d
   ```
   This will start Odoo 19 on port `8069` and Postgres 15.

3. **Access Odoo**:
   Open your browser and navigate to:
   - [http://localhost:8069](http://localhost:8069)

## Credentials

### Database Configuration (Docker)
- **User**: `odoo`
- **Password**: `odoo`
- **Database Name**: `postgres` (default superuser db)

### Master Password
The master password for database management is set in the configuration or generated on first use.
- **Master Password**: `dyqz-ivrj-4qwk` (based on your configuration)

## Custom Modules

### Theme Login Custom (`theme_login_custom`)
A custom module is included to customize the login page with a gradient background and a welcome message.

#### How to Install/Update:
1.  **Activate Developer Mode** in Odoo (Settings -> Activate developer mode).
2.  Go to **Apps** and click **Update Apps List**.
3.  Search for `Custom Login Theme` (or `theme_login_custom`).
4.  Click **Activate** (or **Upgrade** if you made changes).

#### How to Verify:
Logout (`http://localhost:8069/web/session/logout`) and check the login page. You should see:
- A gradient background.
- A "Selamat Datang" welcome message inside the login card.

## Useful Commands

- **Stop services**:
  ```bash
  docker compose down
  ```
- **Restart Odoo only**:
  ```bash
  docker compose restart web
  ```
- **View logs**:
  ```bash
  docker compose logs -f web
  ```
- **Reinstall Custom Module (via CLI)**:
  ```bash
  docker compose exec web odoo -u theme_login_custom -d odoo_db --stop-after-init
  ```

## Directory Structure
- `addons/`: Custom modules (mounted to `/mnt/extra-addons`).
- `config/`: Odoo configuration files (mounted to `/etc/odoo`).
- `docker-compose.yml`: Docker services definition.
