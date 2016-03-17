import codecs
import os
import sys
 
try:
    from setuptools import setup
except:
    from distutils.core import setup

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

NAME = "wechatOauth"

PACKAGES = ["wechatOauth",]
 
DESCRIPTION = "A python SDK that use to wechat oauth verification"
 
LONG_DESCRIPTION = read("README")
 
KEYWORDS = "wechat oauth python"
 
AUTHOR = "mymusise"
 
AUTHOR_EMAIL = "mymusise1@gmail.com"
 
URL = "https://github.com/mymusise/wechat-oauth"
 
VERSION = "0.0.6"
 
LICENSE = "MIT"
 
setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = PACKAGES,
    package_dir={'wechatOauth':'src'},
    include_package_data=True,
    zip_safe=True,
)
 