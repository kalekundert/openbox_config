# Note that this script is not executed if OpenBox is run as part of a GNOME
# session.
#
# Launch a keyring to automatically unlock my SSH keys as necessary.

export $(gnome-keyring-daemon --start)
