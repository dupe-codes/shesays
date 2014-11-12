shesays
=======

SheSays is an anonymous forum to rate and review tech companies based on women’s experiences. By focusing on these voices, we provide a service to those entering tech and use often overlooked stories to take inclusive workspaces from voluntary to essential.

## Dev Setup

To set up locally for development, follow these steps:

1. Git pull this repo
2. Install postgreSQL on your local machine (for OsX, refer to [this](http://blog.willj.net/2011/05/31/setting-up-postgresql-for-ruby-on-rails-development-on-os-x/) useful guide)
3. Create the postgreSQL user and databases expected for development:
    - `createuser shesays`
    - `createdb -Oshesays shesays_dev`
4. Install project requirements
    - `pip install -r requirements.txt`
5. Run the server to confirm everything is working.
6. Begin hacking!

## Cloud9 (Recommended)

To get setup on cloud9 http://c9.io and use sqlite:

1. Clone the shesays repo (Under my projects)
2. Open the workspace
3. `pip install -r requirements.txt`
4. `mkdir logs`
5. `mkdir shesays_platform/logs`
6. `python manage.py syncdb --settings=shesays_platform.settings.development`
7. `python manage.py runserver $IP:$PORT --settings=shesays_platform.settings.development`
8. Begin hacking!

For Celery/Email Sending
========================

1. Need to run celery with command: `celery -A shesays_platform worker -l info`
2. Configure email SMTP settings in `shesays_platform/settings/dev.py`
