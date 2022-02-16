import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medium.settings")
django.setup()

from users.models import User

User.objects.create_user(
    "ifl@ger.com", "ramzi", username="orlog", bio="this is orlog"
)
User.objects.create_superuser("orlog@admin.com", "orlog", username="orlog admin")
