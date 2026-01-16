import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

def initialize():
    # 1. Setup Site
    site, created = Site.objects.get_or_create(id=1, defaults={'domain': '127.0.0.1:8000', 'name': '127.0.0.1:8000'})
    if not created:
        site.domain = '127.0.0.1:8000'
        site.name = '127.0.0.1:8000'
        site.save()
    print(f"Site configured: {site.domain}")

    # 2. Setup Google SocialApp
    google_app, created = SocialApp.objects.get_or_create(
        provider='google',
        defaults={
            'name': 'Google Login',
            'client_id': 'PLACEHOLDER_GOOGLE_CLIENT_ID',
            'secret': 'PLACEHOLDER_GOOGLE_SECRET',
        }
    )
    google_app.sites.add(site)
    print(f"Google SocialApp {'created' if created else 'already exists'}")

    # 3. Setup GitHub SocialApp
    github_app, created = SocialApp.objects.get_or_create(
        provider='github',
        defaults={
            'name': 'GitHub Login',
            'client_id': 'PLACEHOLDER_GITHUB_CLIENT_ID',
            'secret': 'PLACEHOLDER_GITHUB_SECRET',
        }
    )
    github_app.sites.add(site)
    print(f"GitHub SocialApp {'created' if created else 'already exists'}")

if __name__ == "__main__":
    initialize()
