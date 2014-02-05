Migration from sqlite+sentry 4 to postgresql+sentry 6
=====================================================

There seem to be two options:

1. With the old sentry, dump the sqlite database, switch the database
   settings to postgresql (needs psycopg2 in the eggs) and load the
   data in postgresql, then switch to newer sentry and run the
   upgrade.

2. First switch to the newer sentry, run the upgrade, dump the sqlite
   database, switch the database settings to postgresql, load the data
   in postgresql.

But: the order in which you dump tables is important, otherwise
loaddata will fail.  I have figured this out for the first option and
that strategy does not work for the second option.

So: we use the first option, though it means we need two buildout tags
(one that only adds the psycopg2 egg) and run bin/buildout twice.


Dump the sqlite database
------------------------

- Make backup of sqlite database:

  cp central_sentry.db central_sentry_orig.db

- Double check that the DATABASES in settings.py points to the
  central_centry.db sqlite database (or have this in settings_local.py
  and use that as option for --config).

- Run the upgrade and repair commands to make sure the database is good:

    bin/sentry --config=central_sentry/settings.py upgrade
    bin/sentry --config=central_sentry/settings.py repair

- First dump the data from the (django.contrib.)auth app, then the
  rest, otherwise loaddata will fail later on:

    bin/sentry --config=central_sentry/settings.py dumpdata auth > dumpdata-auth.json
    bin/sentry --config=central_sentry/settings.py dumpdata --exclude auth > dumpdata.json


Load the dumped data into postgres
----------------------------------

- Create a fresh postgres database and put the connection data into
  settings.py (or in settings_local.py and use that as --config
  option).

- Initialize the database, do not create superusers:

   bin/sentry --config=central_sentry/settings.py upgrade

- Remove the demo project that has just been created by the upgrade
  command:

    select * from sentry_project;
    delete from sentry_project;

- Load previous data:

    bin/sentry --config=central_sentry/settings.py loaddata dumpdata-auth.json
    bin/sentry --config=central_sentry/settings.py loaddata dumpdata.json
