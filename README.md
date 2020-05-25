# Python-Debugging

Contains the code for the Python Debugging with PDB tutorial on [Python Debugging With Pdb](https://realpython.com/python-debugging-pdb/).

## Sections

1. Getting Started: Printing a Variable’s Value
2. Printing Expressions
3. Stepping Through Code
   1. Listing Source Code
4. Using Breakpoints
5. Continuing Execution
6. Displaying Expressions
7. Python Caller ID
8. Essential pdb Commands
9. Python Debugging With pdb: Conclusion

## Notes

1. Getting started
   1. start debugger with
      1. `import pdb; pdb.set_trace`
      2. `breakpoint()`
         1. breakpoint is more preferable since you can set PYTHONBREAKPOINT=0 and completely disable debugging
      3. `python -m pdb app.py arg1 arg2`
   2. press q to quit
   3. example_1()
      1. output:

         ```> j:\education\code\python\python-debugging\python_debug\python_debug.py(17)example_1()
         -> print(f'path = {filename}')
         (Pdb) p filename
         'python_debug.py'```

      2. `>` starts the 1st line and tells you which source file you’re in. After the filename, there is the current line number in parentheses.
      3. Next is the name of the function. In this example, since we’re not paused inside a function and at module level, we see `<module>()`.
      4. -> starts the 2nd line and is the current source line where Python is paused. This line hasn’t been executed yet. In this example, this is line 24 in example_1.py, from the > line above.
      5. (Pdb) is pdb’s prompt. It’s waiting for a command
   4. example_2()
      1. we can print expressions using the p command as well
         1. ll is longlist and prints the function source code

             ```python
             (Pdb) ll
                 28     def get_path(filename):
                 29         """
                 30         Return the path of the file
                 31         args:
                 32             filename (str): name of the file
                 33         returns:
                 34             head (str): path to the file
                 35         """
                 36         head, tail = os.path.split(filename)
                 37         breakpoint()
                 38  ->     return head
                 ```

         2. print multiple expressions using ,

            ```python
            (Pdb) p head, tail
            ('', 'python_debug.py')```

         3. concatenate strings and expressions using +

            ```python
            (Pdb) p 'filename' + filename
            'filenamepython_debug.py'
            ```

         4. use get_attr to view attributes such as `__doc__`

              ```python
              (Pdb) p getattr(get_path, '__doc__')
              '\n    Return the path of the file\n    args:\n        filename (str): name of the file\n    returns:\n        head (str): path to the file\n    '
              ```

         5. perform a short expression

            ```python
            (Pdb) pp [os.path.split(p)[1] for p in os.path.sys.path]
            ['python_debug', 'python38.zip', 'DLLs', 'lib', 'Python38', 'site-packages']
            ```

      2. the pp command can be used to preety print expressions
