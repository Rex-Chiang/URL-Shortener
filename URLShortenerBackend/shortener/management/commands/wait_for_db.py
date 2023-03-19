"""
Django command to pause execution until database is available
"""
import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        is_connect = False

        while not is_connect:
            try:
                db_conn = connections["default"]
                db_conn.ensure_connection()
                is_connect = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available !"))