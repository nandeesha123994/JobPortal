import os
import django
import sys

# Setup Django environment
sys.path.append(r'c:\Users\Nandeesha M\OneDrive\Desktop\Django\jobportal')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

print(f"Current Site ID: {django.conf.settings.SITE_ID}")
try:
    current_site = Site.objects.get(id=django.conf.settings.SITE_ID)
    print(f"Current Site Domain: {current_site.domain}")
    print(f"Current Site Name: {current_site.name}")
except Site.DoesNotExist:
    print("Current Site ID does not exist in DB!")

print("\nSocial Apps:")
apps = SocialApp.objects.all()
if not apps:
    print("No SocialApps found.")
else:
    for app in apps:
        print(f"Provider: {app.provider}")
        print(f"Name: {app.name}")
        print(f"Client ID: {app.client_id}")
        print(f"Sites: {[s.id for s in app.sites.all()]}")
