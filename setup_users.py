import os
import sys
from pathlib import Path
import django

PROJECT_ROOT = Path(__file__).parent
sys.path.append(str(PROJECT_ROOT))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elearning.settings')
django.setup()

print("Setting up users...")

from django.contrib.auth.models import User, Group


for user in User.objects.all():
    print(user.username)

for group in Group.objects.all():
    print(group.name)


print("Done.")
