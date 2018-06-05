from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        '아이디',
        max_length=32,
        unique=True,
        help_text=_('아이디를 입력해 주세요.'),
        validators=[
            MinLengthValidator(4, '4자 이상 32자 이하로 입력해주세요.'),
            RegexValidator(r'^[a-z0-9]+$', '알파벳 소문자와 숫자만 허용됩니다.')
        ],
        error_messages={
            'unique': '이미 존재하는 아이디 입니다.',
            'max_length': '4자 이상 32자 이하로 입력해주세요.'
        },
    )
    email = models.EmailField(
        '이메일',
        unique=True,
        error_messages={
            'unique': '이미 가입된 이메일입니다.'
        }
    )
    class_number = models.CharField(
        '학번',
        max_length=8,
        unique=True,
        help_text='학번을 입력해주세요.',
        validators=[
            MinLengthValidator(8, '8자의 학번을 입력해주세요.'),
            RegexValidator(r'^[0-9]+$', '숫자만 허용됩니다.')
        ],
        error_messages={
            'unique': '이미 가입된 학번입니다.',
            'max_length': '8자의 학번을 입력해주세요.'
        }
    )
    phone_number = models.CharField(
        '핸드폰 번호',
        max_length=11,
        unique=True,
        help_text='핸드폰 번호를 입력해주세요.',
        validators=[
            MinLengthValidator(10),
            RegexValidator(r'^[0-9]+$')
        ],
        error_messages={
            'unique': '이미 가입된 휴대폰 번호입니다.'
        }
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'class_number']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username
