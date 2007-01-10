#!/usr/bin/env python

# NOTE: Path manipulation may require manual customisation.

import sys, os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../../Common")))

from WebStack.Adapters.ModPython import deploy
from WebStack.Resources.LoginRedirect import LoginRedirectResource, LoginRedirectAuthenticator
from Simple import SimpleResource

# NOTE: Not sure if the resource should be maintained in a resource pool.

resource = LoginRedirectResource(
    login_url="http://localhost/login/app",
    app_url="http://localhost",
    resource=SimpleResource(),
    authenticator=LoginRedirectAuthenticator(secret_key="horses"),
    anonymous_parameter_name="anonymous",
    logout_parameter_name="logout",
    use_logout_redirect=0
)

handler, _no_authentication = deploy(resource, handle_errors=0)

# vim: tabstop=4 expandtab shiftwidth=4
