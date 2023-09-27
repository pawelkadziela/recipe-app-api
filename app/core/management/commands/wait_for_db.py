"""
Django command to wait for db to be available
"""

import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        is_db_up = False

        while not is_db_up:
            try:
                self.check(databases=['default'])
                is_db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable.' +
                                  'Waiting one second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
