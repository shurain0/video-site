from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MaximumLengthValidator:
    def __init__(self, max_length=8):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                _("パスワードは、最大 %(max_length)d 文字までで入力してください。"),
                code='password_too_long',
                params={'max_length': self.max_length},
            )

    def get_help_text(self):
        return _(
            "パスワードは、最大 %(max_length)d 文字までで入力してください."
            % {'max_length': self.max_length}
        )
