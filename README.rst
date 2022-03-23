Olive Proj

This project uses Docker Compose and make.

This project requires ![pip-tools](https://github.com/jazzband/pip-tools)

.. code-block:: bash

    $ source /path/to/venv/bin/activate
    (venv) $ python -m pip install pip-tools

If make and Docker Compose are available

.. code-block:: bash
    make run

If you're feeling adventurous, do it from scratch

.. code-block::bash
    pip-compile
    pip install -r requirements.txt
    python3 main.py -v DEBUG input output


