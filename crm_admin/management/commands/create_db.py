from django.core.management.base import BaseCommand
from django.db import connections, OperationalError
from django.conf import settings
import MySQLdb

class Command(BaseCommand):
    help = 'Create the database if it does not exist'

    def handle(self, *args, **kwargs):
        db_settings = settings.DATABASES['default']
        db_name = db_settings['NAME']
        db_user = db_settings['USER']
        db_password = db_settings['PASSWORD']
        db_host = db_settings['HOST']
        db_port = db_settings['PORT']

        try:
            # Try to connect to the database
            connection = connections['default']
            connection.ensure_connection()
            self.stdout.write(self.style.SUCCESS(f'Database "{db_name}" already exists.'))
        except OperationalError:
            # If connection fails, create the database
            self.stdout.write(self.style.WARNING(f'Database "{db_name}" does not exist. Creating database...'))
            try:
                conn = MySQLdb.connect(
                    user=db_user,
                    passwd=db_password,
                    host=db_host,
                    port=int(db_port)
                )
                cursor = conn.cursor()
                cursor.execute(f'CREATE DATABASE {db_name}')
                cursor.close()
                conn.close()
                self.stdout.write(self.style.SUCCESS(f'Database "{db_name}" created successfully.'))
            except MySQLdb.Error as e:
                self.stderr.write(self.style.ERROR(f'Error creating database: {e}'))
