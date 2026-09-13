# parser: empty quoted key causes a panic

Version: 2.3.1
OS: Debian 13, x86-64

Save this input as `case.conf`:

```text
"" = 1
```

Run `parser case.conf`.

Actual result: the process exits with status 134 and prints `index out of bounds`.

Expected result: the process exits with status 2 and reports an empty key on line 1.
