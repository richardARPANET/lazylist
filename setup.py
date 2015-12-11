from distutils.core import setup

from lazylist import __version__ as version


def readme(filename):
    try:
        with open(filename) as f:
            return f.read()
    except IOError:
        pass


setup(
    name='lazylist',
    version=version,
    description='Proxy list to a list-returning function',
    long_description=readme('README.rst'),
    license='LGPLv3+',
    author='Hong Minhee',
    author_email='hongminhee' '@' 'member.fsf.org',
    url='https://github.com/dahlia/lazylist',
    py_modules=['lazylist'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved'
        ' :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
