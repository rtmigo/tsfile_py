Python package for solving a specific task: reading the date stored in 
a `timestamp.txt`. 

## timestamp.txt

Sample content `my_project/timestamp.txt`:

``` text
2021-05-07 22:01:44 +03
```

For example, such file can be created before deploying the project with as command:
``` bash 
date +"%Y-%m-%d %H:%M:%S %Z" > /path/to/my_project/timestamp.txt
```

## TimestampFile object

When created, the `TimestampFile` object scans the parent directories. The 
search stops when the parent contains a `timestamp.txt`.

That is, you can create a `TimestampFile` in any module located in any 
subdirectory of `my_project`. For example, in `my_project/dir/subdir/module.py`:

``` python
from tsfile import TimestampFile

build_timestamp = TimestampFile()

print(build_timestamp.text)       # '2021-05-07 22:01:44 +03'
print(build_timestamp.time)       # datetime.datetime
print(build_timestamp.version)    # '21.253.835' (generated from time)
```
