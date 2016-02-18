#encoding:utf-8
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
 
DESCRIPTION = "this is a test package for packing python liberaries tutorial."
 
LONG_DESCRIPTION = read("README.rst")
 
KEYWORDS = "test mymusise python package"
 
AUTHOR = "Mymusise"
 
AUTHOR_EMAIL = "youremail@email.com"
 
URL = "http://blog.mymusise.com/"
 
VERSION = "0.0.1"
 
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
    zip_safe=True,
)
 