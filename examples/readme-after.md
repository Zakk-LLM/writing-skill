# Queue Tools

Queue Tools is a command-line program that retries interrupted queue jobs.

## Install

Requires Python 3.11 or later.

```bash
python3 -m pip install queue-tools
```

## Start a worker

Run the worker from a directory that contains `queue.toml`:

```bash
queue-tools start
```

The command prints `worker ready` after it connects to the configured queue.
