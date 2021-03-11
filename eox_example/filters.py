import logging

log = logging.getLogger(__name__)
from openedx.core.djangoapps.user_authn.exceptions import UnathorizedLoginByHookException

def pre_login(request):
    """
    Do not allow logins if the user email starts with "staff".
    """
    email = request.POST.get("email") or ""
    if email.startswith("staff"):
        raise UnathorizedLoginByHookException("not authorized to login by hook. Your email starts with staff, that is not allowed.")
