Legacy database record creation tool.

Mock data generation tool for a project I'm working on.

This tool creates mock records for holdings, their owners and disease incidents for them, for you to use in the demonstration of your disease mangament tools.

To use, use the management extensions:

```
python manage.py create_farms <count> <distribution per parish>
python manage.py create_incidents <count>
```

Results are dumped to the sqlite database legacy_db.sqlite3, which you can then drop into your tool for testing / demoing.


