Uso
===
*Revisar*

.. _installation:

Installation
------------

To use LIDAO, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lidao

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lidao.get_random_ingredients()`` function:

.. autofunction:: lidao.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lidao.get_random_ingredients`
will raise an exception.

.. autoexception:: lidao.InvalidKindError

For example:

>>> import lidao
>>> lidao.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

