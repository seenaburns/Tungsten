.. Tungsten documentation master file, created by
   sphinx-quickstart on Thu Nov 22 11:56:42 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tungsten Documentation
======================

Installation
------------

::

	pip install tungsten

Tungsten has been tested on 2.x Python

Quickstart
----------

From here, operating Tungsten is as easy as creating a Tungsten client object (requires an appid) and running a query.

:: 

	import tungsten
    
    client = tungsten.Tungsten('appid')
    result = client.query('pi')

Additional query parameters (query parameter documentation on the `Wolfram Alpha API documentation <http://products.wolframalpha.com/api/documentation.html#8>`_) can also be passed to the query using a dictionary:

::

	params = {'format': ['plaintext', 'image', 'minput', 'moutput'],
		'scanner': 'numeric',
		'parsetimeout': 10}
	result = client.query('rref {{1,2},{3,4}}', params)

Query will always return a result object which has a few properties to report if the query was unsuccessful.

The Result object also stores a list of all the pods returned by the query. These pods are the individual result sections returned by Wolfram Alpha, seperated by type of response. For example, query('pi') returns seperate pods for the number line, decimal approximation and so on.

::

	result.success
	# True
	result.error
	# None

	result.pods
	# List of pods

Each Tungsten Pod object has a few properties to identify it (title, id, scanner) and supports any available format using another property, format.

::

	pod.title
	# Decimal approximation
	pod.id
	# DecimalApproximation
	pod.scanner
	# Numeric

The format property returns a dictionary of available formats as keys, key corresponding to a list of the format's values (format type documentation on `Wolfram Alpha API Documentation <http://products.wolframalpha.com/api/documentation.html#3>`_).

For example, pod.format['plaintext'] will return a list of every plaintext content in the pod.

::

	# List all the available formats
	pod.format.keys()
	
	# Get a list of the mathematica input format (if available)
	pod.format.get('minput', [])

There is special handling for the image to package all information.

::

	 img_list = pod.format['img']
	 img = img_list[0] # format still returns a list even when only 1 object is available
	 
	 # Available properties
	 img['url']
	 img['alt']
	 img['title']
	 img['width']
	 img['height']



Contribute
----------

Tungsten is hosted on `Github <https://github.com/seenaburns/Tungsten>`_, just fork the repo and start coding, there's plenty of room for development. 

