"""
One time execution script, transfering data from
oc_lettings_site.models to profiles.models & lettings.models
after database migration.

This script can only work from the original models config (one app only).
"""
import os
import django
from oc_lettings_site.models import Letting, Profile, Address  # noqa
from lettings.models import Letting as NewLetting
from profiles.models import Profile as NewProfile
from lettings.models import Address as NewAddress

# Django environnement configuration
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
django.setup()

# Copying datas into new model for lettings app
anciennes_adresses = Address.objects.all()
for ancienne_adresse in anciennes_adresses:
    nouvelle_adresse = NewAddress.objects.create(
        number=ancienne_adresse.number,
        street=ancienne_adresse.street,
        city=ancienne_adresse.city,
        state=ancienne_adresse.state,
        zip_code=ancienne_adresse.zip_code,
        country_iso_code=ancienne_adresse.country_iso_code
    )

# Copying datas into new model for lettings app
anciennes_lettings = Letting.objects.all()
for ancienne_letting in anciennes_lettings:
    ancienne_address = ancienne_letting.address
    nouvelle_address = NewAddress.objects.get(number=ancienne_address.number,
                                              street=ancienne_address.street)
    nouvelle_letting = NewLetting(
        title=ancienne_letting.title,
        address=nouvelle_address,
    )
    nouvelle_letting.save()

# Copying datas into new model for profiles app
anciens_profiles = Profile.objects.all()
for ancien_profile in anciens_profiles:
    nouvel_utilisateur = ancien_profile.user
    nouveau_profile = NewProfile(
        user=nouvel_utilisateur,
        favorite_city=ancien_profile.favorite_city,
    )
    nouveau_profile.save()

print("Migration des données terminée avec succès !")
