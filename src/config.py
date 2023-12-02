import sys

is_development: bool = False

if getattr(sys, 'frozen', False):
    is_development = False
else:
    is_development = True


