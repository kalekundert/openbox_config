#!/usr/bin/env python

"""\
Usage:
    pick-monitors.py [-d]

Options:
    -d --dry-run
        Show the commands that would be run, but don't actually run them.
"""

import docopt
import re, subprocess, shlex

def find_monitors():
    xrandr = subprocess.run(['xrandr'], capture_output=True, text=True)
    monitors = []

    for line in xrandr.stdout.splitlines():
        if re.search(r'\bconnected\b', line):
            monitor = line.split()[0]
            monitors.append(monitor)

    return monitors

def toggle_monitors(monitors, dry_run=False):
    internal = []
    external = []

    for monitor in monitors:
        if monitor.startswith('LVDS'):
            internal.append(monitor)
        else:
            external.append(monitor)

    if external:
        # I don't really understand why, but this seems to be more robust when done 
        # in two steps rather than one...
        try:
            run_xrandr(
                    *display_args(monitors, False),
                    dry_run=dry_run,
                    check=True,
            )
            run_xrandr(
                    *display_args(external, True),
                    dry_run=dry_run,
                    check=True,
            )
        except subprocess.CalledProcessError:
            pass
        else:
            return

    run_xrandr(
            *display_args(internal, True),
            *display_args(external, False),
            dry_run=dry_run,
    )

def run_xrandr(*args, dry_run, **kwargs):
    xrandr = ['xrandr', *args]
    print('++', shlex.join(xrandr))
    if not dry_run:
        return subprocess.run(xrandr, **kwargs)

def display_args(monitors, value):
    args = []
    for monitor in monitors:
        args += ['--output', monitor, '--auto' if value else '--off']
    return args


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    monitors = find_monitors()
    toggle_monitors(monitors, dry_run=args['--dry-run'])
