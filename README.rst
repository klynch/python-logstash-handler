logstash_handler: JSON logs for logstash
==========================================

This library is provided to allow standard python logging to stream JSON logs
to logstash.

Installing
----------
Pip:

    ``pip install logstash_handler``

Pypi:

   https://pypi.python.org/pypi/logstash_handler

Manual:

    ``python setup.py install``

Usage
-----

Json outputs are provided by the LogstashFormatter logging formatter.

::

    import logging
    from logstash_formatter import LogstashFormatter
    from logstash_handler import LogstashHandler

    logger = logging.getLogger()
    handler = LogstashHandler('localhost', 5000, ssl=False)
    formatter = LogstashFormatter()

    handler.setFormatter(formatter)
    logger.addHandler(handler)

The LogstashHandler takes the following named parameters:

* ``host``: host to connect to
* ``port``: host to connect to
* ``ssl``: boolean indicating if the stream should be encrypted. Default is True
* ``keyfile``: The path to the encrypting key
* ``certfile``: The path to the encrypting certificate
