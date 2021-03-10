import logging

log = logging.getLogger(__name__)


def pre_login(request):
    """
    Do not allow logins if the user email starts with "staff".
    """
    email = request.POST.get("email") or ""
    if email.startswith("staff"):
        return {"cannot_login": True}
