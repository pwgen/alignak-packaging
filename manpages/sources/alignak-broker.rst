==============
alignak-broker
==============

---------------------
Alignak broker daemon
---------------------

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

  **alignak-broker** [-dr] [-c *CONFIGFILE*] [--debugfile *DEBUGFILE*]

DESCRIPTION
===========

Alignak broker daemon.

The **alignak-broker**'s exports and manages data from schedulers (such as status).
The management itself is done by the broker modules.

Multiple modules can be enabled simultaneously

OPTIONS
=======

  -c INI-CONFIG-FILE, --config=INI-CONFIG-FILE  Daemon configuration file
  -d, --daemon                                  Run in daemon mode
  -r, --replace                                 Replace previous running arbiter
  -h, --help                                    Show this help message
  --debugfile=DEBUGFILE                         Enable debug logging to *DEBUGFILE*
