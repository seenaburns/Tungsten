Tungsten
--------

Tungsten is a dead simple Wolfram Alpha API wrapper built for python, with all the power and none of the hassle. Check it out:

::

    import tungsten

    client = tungsten.Tungsten('appid')
    result = client.query('pi')

    for pod in pods:
        print pod.scanner

Of course, that stuff is pretty simple. Tungsten can handle a lot more.

::

    # Query parameters
    params = {'format': ['plaintext', 'image', 'minput', 'moutput'],
              'scanner': 'numeric',
              'parsetimeout': 10}
    result = client.query('rref {{1,2},{3,4}}', params)

    # Various formats
    mathematica_input = result.pods[1].format['minput']
    image = result.pods[1].format['img']

    # Piping queries
    piped_result = client.query(mathematica_input)

BSD licensed. Hosted on `Github <https://github.com/seenaburns/Tungsten>`_ and available on PyPI. Documentation on `Read The Docs <https://tungsten.readthedocs.org/en/latest/>`_.

Installation: ::

    pip install tungsten

