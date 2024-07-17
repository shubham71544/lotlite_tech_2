# yourapp/management/commands/create_db.py

import mysql.connector
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates the database if it does not exist'

    def handle(self, *args, **kwargs):
        db_settings = settings.DATABASES['default']
        db_name = db_settings['NAME']
        db_user = db_settings['USER']
        db_password = db_settings['PASSWORD']
        db_host = db_settings['HOST']
        db_port = db_settings['PORT'] or '3306'

        try:
            conn = mysql.connector.connect(
                host=db_host,
                user=db_user,
                password=db_password,
                port=db_port
            )
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            self.stdout.write(self.style.SUCCESS(f"Database '{db_name}' created or already exists."))
        except mysql.connector.Error as err:
            self.stdout.write(self.style.ERROR(f"MySQL Error: {err}"))
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()
