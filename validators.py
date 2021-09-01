from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re
# from string import ascii_lowercase, digits

# def contain_any(target, condition_list):
#     return any([i in target for i in condition_list])

# def contain_all(target, condition_list):
#     return all([i in target for i in condition_list])


class MaximumLengthValidator:
    def __init__(self, max_length=8):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                _("このパスワードは %(max_length)d 文字を超えています。"),
                code='password_too_long',
                params={'max_length': self.max_length},
            )

    def get_help_text(self):
        return _(
            "パスワードは最大 %(max_length)d 文字までです."
            % {'max_length': self.max_length}
        )

class AlphanumericValidator:
    def validate(self, password, user=None):
        if re.match('^[a-zA-Z]+$', password):
            raise ValidationError(
            _("半角の英字と数字を両方使用してください。"),
            code='password_only_alphabet'
            )
        elif re.match('[0-9]+$', password):
            raise ValidationError(
            _("半角の英字と数字を両方使用してください。"),
            code='password_only_number'
            )
        elif not re.match('^[a-zA-Z0-9]+$', password):
            raise ValidationError(
            _("半角英数字で入力してください。"),
            code='password_not_alphanumeric',
            )
    def get_help_text(self):
        return _("半角英数字で入力してください。")
