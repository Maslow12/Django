import pandas as pd
import csv
from django.core.management.base import BaseCommand
from manage_customer.models import Customer

class Command(BaseCommand):
    help = 'Add CVS to Django-Model'
    def add_arguments(self, parser):
        parser.add_argument("path", type=str, help='Path to .CVS file')
    def handle(self,*args, **options):
        df = pd.read_csv(str(options['path']))
        for i in range(len(df.index)):
            c=Customer(first_name=df['first_name'][i], last_name=df['last_name'][i])  
            c.save()  