from setuptools import setup

setup(
    name='cify',
    version='1.0',
    packages=['data', 'venv.lib.python3.5.site-packages.bs4', 'venv.lib.python3.5.site-packages.bs4.tests',
              'venv.lib.python3.5.site-packages.bs4.builder', 'venv.lib.python3.5.site-packages.dns',
              'venv.lib.python3.5.site-packages.dns.rdtypes', 'venv.lib.python3.5.site-packages.dns.rdtypes.IN',
              'venv.lib.python3.5.site-packages.dns.rdtypes.ANY', 'venv.lib.python3.5.site-packages.tld',
              'venv.lib.python3.5.site-packages.tld.sources', 'venv.lib.python3.5.site-packages.tld.commands',
              'venv.lib.python3.5.site-packages.idna', 'venv.lib.python3.5.site-packages.lxml',
              'venv.lib.python3.5.site-packages.lxml.html', 'venv.lib.python3.5.site-packages.lxml.includes',
              'venv.lib.python3.5.site-packages.lxml.isoschematron', 'venv.lib.python3.5.site-packages.past',
              'venv.lib.python3.5.site-packages.past.tests', 'venv.lib.python3.5.site-packages.past.types',
              'venv.lib.python3.5.site-packages.past.utils', 'venv.lib.python3.5.site-packages.past.builtins',
              'venv.lib.python3.5.site-packages.past.translation', 'venv.lib.python3.5.site-packages.whois',
              'venv.lib.python3.5.site-packages.future', 'venv.lib.python3.5.site-packages.future.moves',
              'venv.lib.python3.5.site-packages.future.moves.dbm', 'venv.lib.python3.5.site-packages.future.moves.html',
              'venv.lib.python3.5.site-packages.future.moves.http',
              'venv.lib.python3.5.site-packages.future.moves.test',
              'venv.lib.python3.5.site-packages.future.moves.urllib',
              'venv.lib.python3.5.site-packages.future.moves.xmlrpc',
              'venv.lib.python3.5.site-packages.future.moves.tkinter', 'venv.lib.python3.5.site-packages.future.tests',
              'venv.lib.python3.5.site-packages.future.types', 'venv.lib.python3.5.site-packages.future.utils',
              'venv.lib.python3.5.site-packages.future.builtins', 'venv.lib.python3.5.site-packages.future.backports',
              'venv.lib.python3.5.site-packages.future.backports.html',
              'venv.lib.python3.5.site-packages.future.backports.http',
              'venv.lib.python3.5.site-packages.future.backports.test',
              'venv.lib.python3.5.site-packages.future.backports.email',
              'venv.lib.python3.5.site-packages.future.backports.email.mime',
              'venv.lib.python3.5.site-packages.future.backports.urllib',
              'venv.lib.python3.5.site-packages.future.backports.xmlrpc',
              'venv.lib.python3.5.site-packages.future.standard_library', 'venv.lib.python3.5.site-packages.certifi',
              'venv.lib.python3.5.site-packages.chardet', 'venv.lib.python3.5.site-packages.chardet.cli',
              'venv.lib.python3.5.site-packages.libnmap', 'venv.lib.python3.5.site-packages.libnmap.objects',
              'venv.lib.python3.5.site-packages.libnmap.plugins', 'venv.lib.python3.5.site-packages.urllib3',
              'venv.lib.python3.5.site-packages.urllib3.util', 'venv.lib.python3.5.site-packages.urllib3.contrib',
              'venv.lib.python3.5.site-packages.urllib3.contrib._securetransport',
              'venv.lib.python3.5.site-packages.urllib3.packages',
              'venv.lib.python3.5.site-packages.urllib3.packages.backports',
              'venv.lib.python3.5.site-packages.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.5.site-packages.requests', 'venv.lib.python3.5.site-packages.libfuturize',
              'venv.lib.python3.5.site-packages.libfuturize.fixes', 'venv.lib.python3.5.site-packages.libpasteurize',
              'venv.lib.python3.5.site-packages.libpasteurize.fixes', 'venv.lib.python3.5.site-packages.requests_cache',
              'venv.lib.python3.5.site-packages.requests_cache.backends',
              'venv.lib.python3.5.site-packages.requests_cache.backends.storage',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.idna',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.pytoml',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.certifi',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.chardet',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.chardet.cli',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.distlib',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.distlib._backport',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.msgpack',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.urllib3',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.urllib3.util',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.urllib3.contrib',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.urllib3.contrib._securetransport',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.urllib3.packages',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.urllib3.packages.backports',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.colorama',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.html5lib',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.html5lib._trie',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.html5lib.filters',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.html5lib.treewalkers',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.html5lib.treeadapters',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.html5lib.treebuilders',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.lockfile',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.progress',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.requests',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.packaging',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.cachecontrol',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.cachecontrol.caches',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.webencodings',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._vendor.pkg_resources',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._internal',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._internal.req',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._internal.vcs',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._internal.utils',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._internal.models',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._internal.commands',
              'venv.lib.python3.5.site-packages.pip-10.0.1-py3.5.egg.pip._internal.operations', 'common', 'common.logs',
              'common.net', 'common.net.proxy', 'common.net.proxy.ruler', 'common.utils', 'common.moudle',
              'common.moudle.waf_plugins', 'common.threads', 'worker', 'plugins', 'plugins.cms', 'plugins.port'],
    url='',
    license='',
    author='zii',
    author_email='ziizhuwy@gmail.com',
    description='cify'
)
