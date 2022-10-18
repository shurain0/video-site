from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


# 最大文字を超えるものをはじく（デフォルトは最大8文字）
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


# 半角英数字以外を含むものをはじく
class AlphanumericValidator:
    def validate(self, password, user=None):
        if not re.search('^[a-z0-9]+$', password):
            raise ValidationError(
                _("このパスワードには半角英数字以外が含まれています。"),
                code='password_no_alphanumeric'
            )

    def get_help_text(self):
        return _("半角英数字で入力してください。")


# a-zを含まないものをはじく
class LowercaseValidator:
    def validate(self, password, user=None):
        if not re.search('[a-z]', password):
            raise ValidationError(
                _("このパスワードには1文字も小文字のa-zが含まれていません。"),
                code='password_no_lower'
            )

    def get_help_text(self):
        return _("小文字のa-zを含めてください。")


# 数字を含まないものをはじく
class NumberValidator:
    def validate(self, password, user=None):
        if not re.search('\d', password):
            raise ValidationError(
                _("このパスワードには1文字も数字が含まれていません。"),
                code='password_no_number',
            )

    def get_help_text(self):
        return _("数字を含めてください。")
