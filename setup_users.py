import os
import sys
from pathlib import Path
import django

PROJECT_ROOT = Path(__file__).parent
sys.path.append(str(PROJECT_ROOT))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elearning.settings')
django.setup()

print("Setting up default professor user...")

from django.contrib.auth.models import User, Group

if User.objects.filter(username="prof").exists():
    default_user = User.objects.get(username="prof")
else:
    default_user = User.objects.create_user(username="prof", password="pass", email='prof@ecourses.com')

group, created = Group.objects.get_or_create(name="Professors")
if created:
    print("Group 'Professors' created")
else:
    print("Group 'Professors' already existed")

group.user_set.add(default_user)


print("Done.")
