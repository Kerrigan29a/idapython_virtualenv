#Virtualenv support for IDAPython
by Javier Escalada Gómez

##How to install in IDA

Open IDA and paste the folloging code:

```python
import urllib2,os,hashlib
urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler()))
h = "7f77aedebcf28f7010d1c6629b607826d9ff0f35b8db66c91f042ab2c59adfcb"
ves = urllib2.urlopen('https://fake_url').read()
dh = hashlib.sha256(ves).hexdigest()
idadir = get_user_idadir()
code = "from ida_virtualenv import detectVirtualenv; detectVirtualenv()"
if dh == h:
    open(os.path.join(idadir,'ida_virtualenv.py'),'wb').write(ves)
    open(os.path.join(idadir,'idapythonrc.py'),'ab').write(code)
    Warning('Please restart IDA to finish installation')
else:
    Warning('Error validating download (got {} instead of {}), please try manual install'.format(dh, h))
```

then restart.

##How it works
This script try to detect automatically if the environment variable `VIRTUAL_ENV` is defined. In this case it uses it to activate the Python virtual environment. If the variable is not defined you can call `activateVirtualenv` with the path to the directory.
