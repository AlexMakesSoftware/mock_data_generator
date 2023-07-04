# README.md
Legacy database record creation tool (A mock data generation tool for a project I'm working on).

This tool creates mock records for holdings, their owners and disease incidents for them, for you to use in the demonstration of your disease mangament tools.

## Usage:

```
python manage.py create_farms <count> <distribution per parish>
python manage.py create_incidents <count>
```

Results are dumped to the sqlite database legacy_db.sqlite3, which you can then drop into your tool for testing / demoing.

The admin site on this database is configured to view and explore them.
