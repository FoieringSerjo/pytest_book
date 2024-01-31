# Debugging with pytest flags

### Flags for selecting which tests to run, in which order, and when to stop:
 
* `--lf` / `--last-failed`: Runs just the tests that failed last
* `--ff` / `--failed-first`: Runs all the tests, starting with the last failed
* `-x` / `--exitfirst`: Stops the tests session after the first failure
* `--maxfail=num`: Stops the tests after num failures
* `--nf` / `--new-first`: Runs all the tests, ordered by file modification time
* `--sw` / `--stepwise`: Stops the tests at the first failure. Starts the tests at the last failure next time
* `--sw-skip` / `--stepwise-skip`: Same as --sw, but skips the first failure

### Flags to control pytest output:
* `-v` / `--verbose`: Displays all the test names, passing or failing
* `--tb=[auto/long/short/line/native/no]`: Controls the traceback style
* `-l` / `--showlocals`: Displays local variables alongside the stacktrace

### Flags to start a command-line debugger:
* `--pdb`: Starts an interactive debugging session at the point of failure
* `--trace`: Starts the pdb source-code debugger immediately when running each test