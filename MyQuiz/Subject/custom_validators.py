from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_min_max(value):
    if not (value >= 10.00 and value <= 100.00):
        raise ValidationError(
            _('%(value)s is not on range'),
            params={'value': value},
        )