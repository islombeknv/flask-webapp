# startup.sh is used by infra/resources.bicep to automate database migrations and isn't used by the sample application
cd /home/site/wwwroot
source /antenv/bin/activate
alembic upgrade head
gunicorn --workers 2 --threads 4 --timeout 60 --access-logfile \
    '-' --error-logfile '-' --bind=0.0.0.0:8000 \
     --chdir=/home/site/wwwroot app:app