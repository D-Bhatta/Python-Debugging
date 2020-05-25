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

   5. example_3
      1. output:

            ``` python
            PS J:\Education\Code\Python\Python-Debugging\python_debug> python python_debug.py
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(46)example_3()
            -> filename_path = get_path(filename)
            (Pdb) n
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(47)example_3()
            -> print(f'path = {filename_path}')
            ```

            ```python
            PS J:\Education\Code\Python\Python-Debugging\python_debug> python python_debug.py
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(46)example_3()
            -> filename_path = get_path(filename)
            (Pdb) s
            --Call--
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(28)get_path()
            -> def get_path(filename):
            (Pdb) n
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(36)get_path()
            -> head = os.path.split(filename)[0]
            (Pdb)
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(37)get_path()
            -> return head
            (Pdb)
            --Return--
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(37)get_path()->''
            -> return head
            (Pdb)
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(47)example_3()
            -> print(f'path = {filename_path}')
            (Pdb)
            path =
            --Return--
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(47)example_3()->None
            -> print(f'path = {filename_path}')
            ```

      2. n command
         1. next
         2. n command is used to stepover in local functions,
         3. wont' move into other function calls
         4. remains in the same function
         5. Continue execution until the next line in the current function is reached or it returns.

      3. s command
         1. step
         2. steps into foreign function from local function
         3. Execute the current line and stop at the first possible occasion (either in a function that is called or in the current function).
      4. Notes

            ``` Html
            The difference between n (next) and s (step) is where pdb stops.

            Use n (next) to continue execution until the next line and stay within the current function, i.e. not stop in a foreign function if one is called. Think of next as “staying local” or “step over”.

            Use s (step) to execute the current line and stop in a foreign function if one is called. Think of step as “step into”. If execution is stopped in another function, s will print --Call--.

            Both n and s will stop execution when the end of the current function is reached and print --Return-- along with the return value at the end of the next line after ->.

            With n (next), we stopped on line 15, the next line. We “stayed local” in <module>() and “stepped over” the call to get_path(). The function is <module>() since we’re currently at module level and not paused inside another function.

            With s (step), we stopped on line 6 in the function get_path() since it was called on line 14. Notice the line --Call-- after the s command.

            Conveniently, pdb remembers your last command. If you’re stepping through a lot of code, you can just press Enter to repeat the last command.
            Note the lines --Call-- and --Return--. This is pdb letting you know why execution was stopped. n (next) and s (step) will stop before a function returns. That’s why you see the --Return-- lines above.

            Also note ->'.' at the end of the line after the first --Return--. When pdb stops at the end of a function before it returns, it also prints the return value for you. In this example it’s '.'.
            ```

   6. List code on pdb
      1. using `ll` you can long list source code of current function
      2. using `l` (list) command you can list shorter code
         1. `l` prints `11` lines by default around the current line until EOF
         2. passing `.` to `l` like `l .` prints 11 lines or the previous listing
