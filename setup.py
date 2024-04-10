
#!/usr/bin/python
try: from setuptools import setup
except:
  print ('"setuptools" library is not found ! try installing . . .')
  import os
  os.system('pip install setuptools') # if not exists
  
finally: from setuptools import setup

setup(
    name='felfel-framework',
    version='1.0.1',
    author='https://github.com/Fel-Fel',
    author_email='felfel@onionmail.com',
    description='fucking py3 script for generating reverse shells easily and automating the boring stuff like '
                'setting up a listener & try to give shell from fucking systems. xd',
    social_media = "404 not found.",
    install_requires=['colorama',
                      'requests',
                      'ngrok',
                      '',
                      '',
                      '',
                      '',
                      '',
                      '',
                      '']
)
