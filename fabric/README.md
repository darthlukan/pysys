This is as basic a fabfile as it gets.

The idea is that for tasks that you commonly perform,
you can more easily script it.  Simply put all of
the things that you normally do into functions (that make sense)
and execute with '$ fab functionName:args'.

This is even more useful when you want to deploy using
git or another version control system.

For more in-depth examples, visit: 
http://docs.fabfile.org/en/1.4.0/index.html#documentation-index

NOTE: Fabric doesn't appear to like file names other than 'fabfile.py'
I tried to use 'fabfile_tutorial.py' and was greeted with an error.
