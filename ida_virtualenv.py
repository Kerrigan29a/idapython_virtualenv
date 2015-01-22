# -*- coding: utf-8 -*-



from __future__ import absolute_import

import os



def detectVirtualenv():
    try:
        activateVirtualenv(virtualenv=os.environ["VIRTUAL_ENV"])
    except:
        pass



def activateVirtualenv(virtualenv=None, interactive=True):
    if virtualenv == None:
        try:
            virtualenv = os.environ["VIRTUAL_ENV"]
        except KeyError:
            if interactive:
                default_virtual_env = os.path.join(get_user_idadir(), "venv")
                virtualenv = idaapi.askstr(0, default_virtual_env, "Select a virtualenv")
    if not virtualenv:
        raise ValueError("Incorrect virtualenv: " + str(virtualenv))
    if not os.path.isdir(virtualenv):
        raise ValueError("This virtualenv is not a dir: " + virtualenv)

    virtualenv_script = os.path.join(virtualenv, "Scripts", "activate_this.py")
    if not os.path.isfile(virtualenv_script):
        raise ValueError('Enable to find "activate_this.py" in virtualenv: ' + virtualenv)

    execfile(virtualenv_script, dict(__file__=virtualenv_script))
