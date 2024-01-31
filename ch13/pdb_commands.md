# Debugging with pdb

Where to get more help: 
* https://docs.python.org/3/library/pdb.html
* https://docs.python.org/3/library/pdb.html#debugger-commands


### Meta commands:
* `h(elp)`: Prints a list of commands
* `h(elp) command`: Prints help on a command
* `q(uit)`: Exits pdb

### Seeing where you are:
* `l(ist)`: Lists 11 lines around the current line. Using it again lists the next 11 lines, and so on.
* `l(ist) .`: The same as above, but with a dot. Lists 11 lines around the current line. Handy if you’ve use l(list) a few times and have lost your current position
* `l(ist) first, last`: Lists a specific set of lines
* `ll`: Lists all source code for the current function
* `w(here)`: Prints the stack trace

### Looking at values:
* `p(rint) expr`: Evaluates expr and prints the value
* `pp expr`: Same as p(rint) expr but uses pretty-print from the pprint module.

### Great for structures
* `a(rgs)`: Prints the argument list of the current function

### Execution commands:
* `s(tep)`: Executes the current line and steps to the next line in your source code even if it’s inside a function
* `n(ext)`: Executes the current line and steps to the next line in the current
function
* `r(eturn)`: Continues until the current function returns
* `c(ontinue)`: Continues until the next breakpoint. When used with --trace, continues until the start of the next test
* `unt(il) lineno`: Continues until the given line number