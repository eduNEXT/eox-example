import logging

log = logging.getLogger(__name__)


def post_login(request, user):
    """
    Logs the username and the site of this new login.
    """
    log.info("%s has logged in on site {}", user.username, request.get_host())
