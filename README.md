# Odoo 19 Community - Docker Setup

This project runs Odoo 19 Community Edition using Docker and Docker Compose, optimized for a lightweight footprint with Alpine images.

## Prerequisites

- Docker
- Docker Compose

## Setup
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd odoo19-docker
   ```

2. **Configure Environment Variables**:
   Create a `.env` file in the root directory (this file is ignored by git):
   ```bash
   cp .env.example .env  # If you have an example file, otherwise create one manually
   ```
   *Note: If `.env.example` doesn't exist, create `.env` with the following variables:*
   ```env
   ODOO_ADMIN_PASSWD=your_secure_master_password
   POSTGRES_USER=odoo
   POSTGRES_PASSWORD=odoo
   POSTGRES_DB=postgres
   ```

3. **Start the services**:
   ```bash
   docker compose up -d
   ```
   This will start Odoo 19 on port `8069` and Postgres 15.

4. **Access Odoo**:
   Open your browser and navigate to:
   - [http://localhost:8069](http://localhost:8069)

## Configuration & Credentials

### Environment Variables (.env)
We use environment variables to manage sensitive information. Ensure your `.env` file is properly configured before starting.

- **Master Password (`admin_passwd`)**: Managed via `ODOO_ADMIN_PASSWORD` in `.env`. This is used to create or manage databases at `/web/database/manager`.
- **Database Credentials**: Managed via `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` in `.env`.

### Odoo Config (`config/odoo.conf`)
The `config/odoo.conf` file is also ignored by git to prevent accidental secret leaks. You can add extra Odoo options there.

## Custom Modules

### Theme Login Custom (`theme_login_custom`)
A custom module is included to customize the login page with a gradient background and a welcome message.

#### How to Install/Update:
1.  **Activate Developer Mode** in Odoo (Settings -> scrolling down -> Activate the developer mode).
2.  Go to **Apps** menu.
3.  Click **Update Apps List** in the top menu bar.
4.  Search for `Custom Login Theme` (or `theme_login_custom`).
5.  Click **Activate** (or **Upgrade** if you made changes).

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
- `.env`: Environment variables (Ignored by git).
- `docker-compose.yml`: Docker services definition.
