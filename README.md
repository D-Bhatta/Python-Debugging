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

   7. breakpoints
      1. create breakpoints with `b` command
         1. `b` **file-name**`:`**line-number** `expression`
         2. `b` **file-name**`:`**function-name** `expression`

            ```python
            (Pdb) b util.get_path, filename.startswith('p')
            (Pdb) b util:14, head.startswith('p')
            ```

      2. type `c` to continue till breakpoint
      3. pdb continues program execution *until* breakpoint is reached

            ```python
            -> filename_path = util.get_path(filename)
            (Pdb) b util:14
            Breakpoint 1 at j:\education\code\python\python-debugging\python_debug\util.py:14
            (Pdb) c
            > j:\education\code\python\python-debugging\python_debug\util.py(14)get_path()
            -> return head
            (Pdb)
            ```

      4. type `b` to print a table of all breakpoints

            ```python
            (Pdb) b
            Num Type         Disp Enb   Where
            1   breakpoint   keep yes   at j:\education\code\python\python-debugging\python_debug\util.py:3
                    breakpoint already hit 1 time
            ```

      5. type `enable` **Num** to enable a breakpoint

            ```python
            (Pdb) b
            Num Type         Disp Enb   Where
            1   breakpoint   keep yes   at j:\education\code\python\python-debugging\python_debug\util.py:3
                    breakpoint already hit 1 time
            (Pdb) enable 1
            Enabled breakpoint 1 at j:\education\code\python\python-debugging\python_debug\util.py:3
            ```

      6. type `disable` **Num** to disable a breakpoint

            ```python
            (Pdb) b
            Num Type         Disp Enb   Where
            1   breakpoint   keep yes   at j:\education\code\python\python-debugging\python_debug\util.py:3
                    breakpoint already hit 1 time
            (Pdb) disable 1
            Disabled breakpoint 1 at j:\education\code\python\python-debugging\python_debug\util.py:3
            ```

      7. using an expression means the program breaks on a line only when the expression evaluates to true
   8. example_4

        ```python
        PS J:\Education\Code\Python\Python-Debugging> python python_debug\python_debug.py
        > j:\education\code\python\python-debugging\python_debug\python_debug.py(61)example_4()
        -> filename_path = util.get_path(filename)
        (Pdb) b util:14
        Breakpoint 1 at j:\education\code\python\python-debugging\python_debug\util.py:14
        (Pdb) c
        > j:\education\code\python\python-debugging\python_debug\util.py(14)get_path()
        -> return head
        (Pdb) p filename, head, tail
        ('python_debug\\python_debug.py', 'python_debug', 'python_debug.py')
        (Pdb) q
        ```

        ```python
        PS J:\Education\Code\Python\Python-Debugging> python python_debug\python_debug.py
        > j:\education\code\python\python-debugging\python_debug\python_debug.py(61)example_4()
        -> filename_path = util.get_path(filename)
        (Pdb) b util.get_path
        Breakpoint 1 at j:\education\code\python\python-debugging\python_debug\util.py:3
        (Pdb) c
        > j:\education\code\python\python-debugging\python_debug\util.py(11)get_path()
        -> if type(filename) != str:
        (Pdb) p filename
        'python_debug\\python_debug.py'
        (Pdb) b
        Num Type         Disp Enb   Where
        1   breakpoint   keep yes   at j:\education\code\python\python-debugging\python_debug\util.py:3
                breakpoint already hit 1 time
        (Pdb) disable 1
        Disabled breakpoint 1 at j:\education\code\python\python-debugging\python_debug\util.py:3
        (Pdb) enable 1
        Enabled breakpoint 1 at j:\education\code\python\python-debugging\python_debug\util.py:3
        (Pdb) q
        ```

        ```python
        PS J:\Education\Code\Python\Python-Debugging> python python_debug\python_debug.py
        > j:\education\code\python\python-debugging\python_debug\python_debug.py(61)example_4()
        -> filename_path = util.get_path(filename)
        (Pdb) b util.get_path, filename.startswith('p')
        Breakpoint 1 at j:\education\code\python\python-debugging\python_debug\util.py:3
        (Pdb) c
        > j:\education\code\python\python-debugging\python_debug\util.py(11)get_path()
        -> if type(filename) != str:
        (Pdb) a
        filename = 'python_debug\\python_debug.py'
        (Pdb) q
        ```

        ```python
        PS J:\Education\Code\Python\Python-Debugging> python python_debug\python_debug.py
        > j:\education\code\python\python-debugging\python_debug\python_debug.py(61)example_4()
        -> filename_path = util.get_path(filename)
        (Pdb) b util:14, head.startswith('p')
        Breakpoint 1 at j:\education\code\python\python-debugging\python_debug\util.py:14
        (Pdb) c
        > j:\education\code\python\python-debugging\python_debug\util.py(14)get_path()
        -> return head
        (Pdb) p head
        'python_debug'
        (Pdb) a
        filename = 'python_debug\\python_debug.py'
        (Pdb) q
        Traceback (most recent call last):
        File "python_debug\python_debug.py", line 64, in <module>
            example_4()
        File "python_debug\python_debug.py", line 61, in example_4
            filename_path = util.get_path(filename)
        File "J:\Education\Code\Python\Python-Debugging\python_debug\util.py", line 14, in get_path
            return head
        File "J:\Education\Code\Python\Python-Debugging\python_debug\util.py", line 14, in get_path
            return head
        File "C:\Program Files\Python37\lib\bdb.py", line 88, in trace_dispatch
            return self.dispatch_line(frame)
        File "C:\Program Files\Python37\lib\bdb.py", line 113, in dispatch_line
            if self.quitting: raise BdbQuit
        bdb.BdbQuit
        ```

   9. unt

       1. until command
       2. `unt` **line-number**
       3. `unt` command moves to a line with a higher number
       4. if no line number is specified then it moves to the very next greater line, stepping over other lines
       5. if a line number is specified then it behaves like `s` and moves to the next line with greater value than **line-number**

   10. example_5

        ```python
        PS J:\Education\Code\Python\Python-Debugging> python python_debug\python_debug.py
        > j:\education\code\python\python-debugging\python_debug\python_debug.py(73)get_path_fname()
        -> if type(fname) != str:
        (Pdb) ll
        64     def get_path_fname(fname):
        65         """
        66         Return the path of the file
        67         args:
        68             fname (str): name of the file
        69         returns:
        70             head (str): path to the file
        71         """
        72         breakpoint()
        73  ->     if type(fname) != str:
        74             raise TypeError
        75         head, tail = os.path.split(fname)  # pylint: disable=unused-variable
        76         for char in tail:
        77             pass
        78         return head
        (Pdb) unt
        > j:\education\code\python\python-debugging\python_debug\python_debug.py(75)get_path_fname()
        -> head, tail = os.path.split(fname)  # pylint: disable=unused-variable
        (Pdb)
        > j:\education\code\python\python-debugging\python_debug\python_debug.py(76)get_path_fname()
        -> for char in tail:
        (Pdb)
        > j:\education\code\python\python-debugging\python_debug\python_debug.py(77)get_path_fname()
        -> pass
        (Pdb)
        > j:\education\code\python\python-debugging\python_debug\python_debug.py(78)get_path_fname()
        -> return head
        (Pdb) p char, tail
        ('y', 'python_debug.py')
        (Pdb) q
        ```

   11. display expressions
       1. set display with `display` **expression**
       2. unset display with `undisplay` **expression**
       3. display automatically shows the value of an expression if it changes

            ```python
            PS J:\Education\Code\Python\Python-Debugging> python python_debug\python_debug.py
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(74)get_path_fname()
            -> if type(fname) != str:
            (Pdb) ll
            65     def get_path_fname(fname):
            66         """
            67         Return the path of the file
            68         args:
            69             fname (str): name of the file
            70         returns:
            71             head (str): path to the file
            72         """
            73         breakpoint()
            74  ->     if type(fname) != str:
            75             raise TypeError
            76         head, tail = os.path.split(fname)  # pylint: disable=unused-variable
            77         for char in tail:
            78             pass
            79         return head
            (Pdb) b 78
            Breakpoint 1 at j:\education\code\python\python-debugging\python_debug\python_debug.py:78
            (Pdb) c
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(78)get_path_fname()
            -> pass
            (Pdb) display char
            display char: 'p'
            (Pdb) c
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(78)get_path_fname()
            -> pass
            display char: 'y'  [old: 'p']
            (Pdb) c
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(78)get_path_fname()
            -> pass
            display char: 't'  [old: 'y']
            (Pdb) c
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(78)get_path_fname()
            -> pass
            display char: 'h'  [old: 't']
            (Pdb) c
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(78)get_path_fname()
            -> pass
            display char: 'o'  [old: 'h']
            (Pdb) q
            ```

       4. you can see all expressions with `display`

            ```python
            PS J:\Education\Code\Python\Python-Debugging> python python_debug\python_debug.py
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(74)get_path_fname()
            -> if type(fname) != str:
            (Pdb) ll
            65     def get_path_fname(fname):
            66         """
            67         Return the path of the file
            68         args:
            69             fname (str): name of the file
            70         returns:
            71             head (str): path to the file
            72         """
            73         breakpoint()
            74  ->     if type(fname) != str:
            75             raise TypeError
            76         head, tail = os.path.split(fname)  # pylint: disable=unused-variable
            77         for char in tail:
            78             pass
            79         return head
            (Pdb) b 78
            Breakpoint 1 at j:\education\code\python\python-debugging\python_debug\python_debug.py:78
            (Pdb) c
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(78)get_path_fname()
            -> pass
            (Pdb) display
            Currently displaying:
            (Pdb) display char
            display char: 'p'
            (Pdb) display fname
            display fname: 'python_debug\\python_debug.py'
            (Pdb) display head
            display head: 'python_debug'
            (Pdb) display tail
            display tail: 'python_debug.py'
            (Pdb) c
            > j:\education\code\python\python-debugging\python_debug\python_debug.py(78)get_path_fname()
            -> pass
            display char: 'y'  [old: 'p']
            (Pdb) display
            Currently displaying:
            char: 'y'
            fname: 'python_debug\\python_debug.py'
            head: 'python_debug'
            tail: 'python_debug.py'
            (Pdb) q
            ```

   12. Use the `w` command to know where you are
       1. `w` means where
       2. use up `u` or down `d` to move around the frames
       3. the most recent frame is at the bottom, start there and read from the bottom up
       4. A stack trace is just a list of all the frames that Python has created to keep track of function calls. A frame is a data structure Python creates when a function is called and deletes when it returns. The stack is simply an ordered list of frames or function calls at any point in time. The (function call) stack grows and shrinks throughout the life of an application as functions are called and then return. When printed, this ordered list of frames, the stack, is called a stack trace
       5. Think of the current frame as the current function where pdb has stopped execution. In other words, the current frame is where your application is currently paused and is used as the “frame” of reference for pdb commands like p (print). p and other commands will use the current frame for context when needed. In the case of p, the current frame will be used for looking up and printing variable references. When pdb prints a stack trace, an arrow > indicates the current frame.
       6. to move multiple frames specify the count variable(default 1):
          1. `u` 2

                ```python
                > j:\education\code\python\python-debugging\python_debug\python_debug.py(89)get_file_info()
                        -> file_path = fileutil.get_path(full_fname)
                        (Pdb) d
                        > j:\education\code\python\python-debugging\python_debug\fileutil.py(13)get_path()
                        -> if type(filename) != str:
                        (Pdb) u 2
                        > j:\education\code\python\python-debugging\python_debug\python_debug.py(94)example_6()
                        -> filename_path = get_file_info(filename)
                        (Pdb) q
                ```

          2. `d` 2
       7. example_6():

        ```python
        > j:\education\code\python\python-debugging\python_debug\fileutil.py(13)get_path()
        -> if type(filename) != str:
        (Pdb) w
        j:\education\code\python\python-debugging\python_debug\python_debug.py(97)<module>()
        -> example_6()
        j:\education\code\python\python-debugging\python_debug\python_debug.py(94)example_6()
        -> filename_path = get_file_info(filename)
        j:\education\code\python\python-debugging\python_debug\python_debug.py(89)get_file_info()
        -> file_path = fileutil.get_path(full_fname)
        > j:\education\code\python\python-debugging\python_debug\fileutil.py(13)get_path()
        -> if type(filename) != str:
        (Pdb) u
        > j:\education\code\python\python-debugging\python_debug\python_debug.py(89)get_file_info()
        -> file_path = fileutil.get_path(full_fname)
        (Pdb) d
        > j:\education\code\python\python-debugging\python_debug\fileutil.py(13)get_path()
        -> if type(filename) != str:
        (Pdb) u 2
        > j:\education\code\python\python-debugging\python_debug\python_debug.py(94)example_6()
        -> filename_path = get_file_info(filename)
        (Pdb) q
        ```

   13. '`h` is the help command

        1. use `h` **command**
        2. example: `h w`

   14.  
