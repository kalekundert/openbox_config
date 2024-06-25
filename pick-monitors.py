#!/usr/bin/env python

"""\
Usage:
    pick-monitors.py [-d]

Options:
    -d --dry-run
        Show the commands that would be run, but don't actually run them.
"""

# DP2 should be 2560x1440

import docopt
import re, subprocess, shlex
from dataclasses import dataclass

@dataclass
class Monitor:
    name: str
    connected: bool

def find_monitors():
    xrandr = subprocess.run(['xrandr'], capture_output=True, text=True)
    monitors = []

    for line in xrandr.stdout.splitlines():
        if m := re.search(r'([A-Z]+\d+) ((?:dis)?connected)\b', line):
            name, status = m.groups()
            monitor = Monitor(name, status == 'connected')
            monitors.append(monitor)

    return monitors

def toggle_monitors(monitors, dry_run=False):
    internal = []
    external = []
    off = []

    for monitor in monitors:
        if not monitor.connected:
            off.append(monitor)
        elif monitor.name.startswith('LVDS'):
            internal.append(monitor)
        else:
            external.append(monitor)

    if external:
        try:
            # When I turn off the internal displays and turn on the external 
            # displays in the same step, the external displays sometimes end up 
            # low-resolution.
            #
            # When I turn off the internal displays and turn on the external 
            # displays in different steps, the windows tend to move around.

            run_xrandr(
                    *display_args(external, True),
                    *display_args(internal + off, False),
                    dry_run=dry_run,
                    check=True,
            )
            # run_xrandr(
            #         *display_args(monitors, False),
            #         dry_run=dry_run,
            #         check=True,
            # )
            # run_xrandr(
            #         *display_args(external, True),
            #         dry_run=dry_run,
            #         check=True,
            # )
        except subprocess.CalledProcessError:
            pass
        else:
            return

    run_xrandr(
            *display_args(internal, True),
            *display_args(external + off, False),
            dry_run=dry_run,
    )

def run_xrandr(*args, dry_run, **kwargs):
    xrandr = ['xrandr', *args]
    print('++', shlex.join(xrandr))
    if not dry_run:
        return subprocess.run(xrandr, **kwargs)


def display_args(monitors, enable):
    args = []
    for monitor in monitors:
        args += ['--output', monitor.name, '--auto' if enable else '--off']
    return args


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    monitors = find_monitors()
    toggle_monitors(monitors, dry_run=args['--dry-run'])
