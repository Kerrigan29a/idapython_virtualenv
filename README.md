#Multiples virtual envs support for IDAPython
by Javier Escalada Gómez

##How to install in IDA

Open IDA and paste the folloging code:

```python
import urllib2,os,hashlib
urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler()))
h = "ca57d849754cdea2d15c709cb1c5345e71352b7908fe90ed2b97a8acb53faed1"
ves = urllib2.urlopen('https://raw.githubusercontent.com/Kerrigan29a/idapython_virtualenv/master/envs.py').read()
dh = hashlib.sha256(ves).hexdigest()
idadir = get_user_idadir()
code = "from envs import detect_env; detect_env()"
if dh == h:
    open(os.path.join(idadir,'envs.py'),'wb').write(ves)
    open(os.path.join(idadir,'idapythonrc.py'),'ab').write(code)
    Warning('Please restart IDA to finish installation')
else:
    Warning('Error validating download (got {} instead of {}), please try manual install'.format(dh, h))
```

then restart.

##Supported envs
- [Virtualenv](http://virtualenv.pypa.io/en/latest/)
- [Conda](http://conda.io/)

##How it works
This script try to detect automatically if the environment variables are defined. In this case it uses them to activate the Python virtual environment. If the variable is not defined you can call this functions manually:
- [activate_virtual_env](envs.py#L42)
- [activate_conda_env](envs.py#L64)
