# Deployment Guide

This guide covers deploying CashMeOutside to various environments.

## Table of Contents

1. [Docker Deployment](#docker-deployment)
2. [Production Considerations](#production-considerations)
3. [Environment Variables](#environment-variables)
4. [Database Setup](#database-setup)
5. [SSL/TLS Configuration](#ssltls-configuration)
6. [Monitoring](#monitoring)
7. [Backup and Recovery](#backup-and-recovery)

## Docker Deployment

### Using Docker Compose (Recommended for Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/jochst/CashMeOutside.git
   cd CashMeOutside
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with production values
   ```

3. **Deploy**
   ```bash
   docker compose up -d
   ```

4. **Run migrations**
   ```bash
   docker compose exec api alembic upgrade head
   ```

5. **Create superuser**
   ```bash
   docker compose exec api python scripts/create_superuser.py
   ```

### Production Docker Deployment

For production, modify the `docker-compose.yml`:

```yaml
services:
  api:
    command: ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
    environment:
      ENVIRONMENT: production
```

## Production Considerations

### Security

1. **Change Secret Keys**
   - Generate a strong JWT secret key:
     ```bash
     openssl rand -hex 32
     ```
   - Update `JWT_SECRET_KEY` in `.env`

2. **Database Security**
   - Use strong passwords
   - Restrict database access to API container only
   - Use SSL for database connections

3. **CORS Configuration**
   - Set specific allowed origins
   - Don't use wildcards in production

4. **API Rate Limiting**
   - Implement rate limiting (see example below)
   - Use reverse proxy for additional security

### Performance

1. **Use Multiple Workers**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
   ```

2. **Connection Pooling**
   - Configure SQLAlchemy pool size in `app/db/session.py`

3. **Caching**
   - Implement Redis for caching
   - Cache frequently accessed data

### Monitoring

1. **Logging**
   ```python
   # Add structured logging
   import logging
   logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   )
   ```

2. **Health Checks**
   - The `/health` endpoint is already available
   - Monitor database connectivity

3. **Metrics**
   - Consider adding Prometheus metrics
   - Monitor API response times

## Environment Variables

### Required Production Variables

```bash
# Database
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=strong_password_here
POSTGRES_DB=production_db

# Security
JWT_SECRET_KEY=your_generated_secret_key_here

# API
ENVIRONMENT=production
CORS_ORIGINS=["https://yourdomain.com"]
```

## Database Setup

### PostgreSQL Configuration

1. **Backup Database**
   ```bash
   docker compose exec db pg_dump -U postgres cashmeoutside_db > backup.sql
   ```

2. **Restore Database**
   ```bash
   docker compose exec -T db psql -U postgres cashmeoutside_db < backup.sql
   ```

3. **Database Migrations**
   ```bash
   # Always test migrations in staging first
   docker compose exec api alembic upgrade head
   ```

### External PostgreSQL

To use an external PostgreSQL instance:

```bash
# .env
DATABASE_URL=postgresql+asyncpg://user:password@external-db.example.com:5432/dbname
SYNC_DATABASE_URL=postgresql://user:password@external-db.example.com:5432/dbname
```

## SSL/TLS Configuration

### Using Nginx as Reverse Proxy

1. **Create nginx configuration**
   ```nginx
   server {
       listen 80;
       server_name api.example.com;
       
       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

2. **Add SSL with Certbot**
   ```bash
   sudo certbot --nginx -d api.example.com
   ```

### Using Traefik

Add labels to `docker-compose.yml`:

```yaml
services:
  api:
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.api.rule=Host(`api.example.com`)"
      - "traefik.http.routers.api.tls=true"
      - "traefik.http.routers.api.tls.certresolver=letsencrypt"
```

## Cloud Deployment

### AWS ECS

1. Build and push image to ECR
2. Create ECS task definition
3. Configure RDS for PostgreSQL
4. Set up Application Load Balancer
5. Deploy ECS service

### Google Cloud Run

```bash
# Build image
gcloud builds submit --tag gcr.io/PROJECT-ID/cashmeoutside

# Deploy
gcloud run deploy cashmeoutside \
  --image gcr.io/PROJECT-ID/cashmeoutside \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Heroku

1. Create `Procfile`:
   ```
   web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT}
   ```

2. Deploy:
   ```bash
   heroku create your-app-name
   heroku addons:create heroku-postgresql:hobby-dev
   git push heroku main
   heroku run alembic upgrade head
   ```

## Monitoring

### Docker Logging

```bash
# View logs
docker compose logs -f api

# Configure log rotation
# Add to docker-compose.yml
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"
```

### Application Monitoring

Consider adding:
- Sentry for error tracking
- Datadog for APM
- Prometheus + Grafana for metrics

## Backup and Recovery

### Automated Backups

Create a backup script:

```bash
#!/bin/bash
# backup.sh
DATE=$(date +%Y%m%d_%H%M%S)
docker compose exec -T db pg_dump -U postgres cashmeoutside_db > backup_$DATE.sql
# Upload to S3 or other storage
```

Run with cron:
```bash
0 2 * * * /path/to/backup.sh
```

### Disaster Recovery

1. Keep backups in multiple locations
2. Test restore procedures regularly
3. Document recovery steps
4. Maintain infrastructure as code

## Scaling

### Horizontal Scaling

1. **Deploy multiple API instances**
2. **Use load balancer**
3. **Share database connection**
4. **Use Redis for session storage**

### Database Scaling

1. **Read replicas** for read-heavy workloads
2. **Connection pooling** with PgBouncer
3. **Database partitioning** for large datasets

## Security Checklist

- [ ] Changed default passwords
- [ ] Generated new JWT secret key
- [ ] Configured CORS for specific domains
- [ ] Set up SSL/TLS
- [ ] Enabled database SSL
- [ ] Implemented rate limiting
- [ ] Set up monitoring and alerting
- [ ] Configured automated backups
- [ ] Reviewed security headers
- [ ] Set up firewall rules
- [ ] Enabled database backups
- [ ] Configured log retention
- [ ] Set up intrusion detection

## Troubleshooting

### Common Issues

1. **Database connection fails**
   - Check database is running
   - Verify connection string
   - Check firewall rules

2. **Migrations fail**
   - Backup database first
   - Check migration files
   - Review error logs

3. **API not responding**
   - Check container logs
   - Verify environment variables
   - Check network connectivity

### Support

For deployment issues:
- Check logs: `docker compose logs -f`
- Review documentation
- Open an issue on GitHub

## Next Steps

After deployment:
1. Monitor application logs
2. Set up alerts
3. Configure backups
4. Implement CI/CD
5. Add monitoring dashboards
6. Document custom procedures

## Resources

- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Nginx Documentation](https://nginx.org/en/docs/)
