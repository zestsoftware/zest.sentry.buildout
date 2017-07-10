About
-----

This buildout installs everything you need for running sentry locally, except
for the postgres database server. Use docker if you want to test locally.


Installing
----------

First create a python 2 virtualenv. Our preference is to install the virtualenv
locallin in the buildout by doing:

    /path/to/virtualenv -p /path/to/python2/bin .

Then run:

    bin/pip install --upgrade -r requirements.txt

To install al dependencies. We do a little trick her by installing the sentry
python modules and dependencies by pip first, because sentry does something
nasty in its setup.py that zc.buildout cannot handle.

Copy buildout.cfg.orig to buildout.cfg and modify the setting to you liking. By
default we extend on devel.cfg, but you can override settings by adding them to
the [conf] section, for example your database location or mailserver.

Now you can run buildout with

    bin/buildout

Buildout will download an install fresh supervisor, memcached and redis and
generate sentry configurations in <buildout-dir>/etc

To start up the sentry stack, run

    bin/supervisord
    
and monitor with:

    bin/supervisorctl status


Initializing sentry and upgrading
---------------------------------

The sentry web interface is a django app and needs to initialise the database
on first run and upgrade the database if you upgrade your sentry version.

To run the init/upgrade migrations, you should first start the sentry stack and
then on the commandline run:

SENTRY_CONF=/path/to/your/buildout/dir/etc bin/sentry upgrade

info: The SENTRY_CONF variable also put in the supervisord environment
variables so that bin/supervisord starts Sentry with access to the config files,
but with stand alone runs you need to pass this on the command line. 