# Multiples virtual envs support for IDAPython
by Javier Escalada Gómez

## How to install in IDA

Open IDA and paste the folloging code:

```python
import urllib2,os,hashlib
urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler()))
original_hash = "d7c05737619aa0ef86e962832d7812338b39465b088fd55f2c8d996e8e6d72b8"
env_code = urllib2.urlopen('https://raw.githubusercontent.com/Kerrigan29a/idapython_virtualenv/master/envs.py').read()
calculated_hash = hashlib.sha256(env_code).hexdigest()
idadir = get_user_idadir()
idapythonrc_code = "from envs import detect_env; detect_env()"
if calculated_hash == original_hash:
    open(os.path.join(idadir,'envs.py'),'wb').write(env_code)
    open(os.path.join(idadir,'idapythonrc.py'),'ab').write(idapythonrc_code)
    Warning('Please restart IDA to finish installation')
else:
    Warning('Error validating download (got {} instead of {}), please try manual install'.format(calculated_hash, original_hash))
```

then restart.

## Supported envs
- [Virtualenv](http://virtualenv.pypa.io/en/latest/)
- [Conda](http://conda.io/)

## How it works
This script try to detect automatically if the environment variables are defined. In this case it uses them to activate the Python virtual environment. If the variable is not defined you can call this functions manually:
- [activate_virtual_env](envs.py#L34)
- [activate_conda_env](envs.py#L56)
