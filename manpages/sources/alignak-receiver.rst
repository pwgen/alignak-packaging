================
alignak-receiver
================

-----------------------
Alignak receiver daemon
-----------------------

:Author:            Michael Leinartas,
                    Arthur Gautier,
                    David Hannequin,
                    Thibault Cohen
:Date:              2014-04-24
:Version:           2.0.1
:Manual section:    8
:Manual group:      Alignak commands


SYNOPSIS
========

  **alignak-receiver** [-dr] [-c *CONFIGFILE*] [--debugfile *DEBUGFILE*]

DESCRIPTION
===========

Alignak receiver daemon.

The **alignak-receiver** daemon manages passive information and serves as a buffer that
 will be read from by the alignak-arbiter and/or alignak-scheduler to dispatch data.

OPTIONS
=======

  -c INI-CONFIG-FILE, --config=INI-CONFIG-FILE  Daemon configuration file
  -d, --daemon                                  Run in daemon mode
  -r, --replace                                 Replace previous running arbiter
  -h, --help                                    Show this help message
  --debugfile=DEBUGFILE                         Enable debug logging to *DEBUGFILE*
