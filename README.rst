========================
Socket Balancing Samples
========================

This repo holds a very basic sample how to balance TCP/IP sockets
with supervisord between multiple processes.

Supervisord supports socket management where it creates and binds socket
to the port. Then it forks some child processes and passes this server
socket with file descriptor `0`.

There's a mini script `http_server.py` which does the actual work.
As it is forked by supervisord, it's able to reuse the socket.

This is similar to how nginx does it's executable upgrading.
But instead all the hard work is done by supervisord.

Usage
=====

::

    make pyenv
    pyenv/bin/supervisord -c supervisord.conf


