.
├── assets
│   └── samples
│       └── README.md
├── data
│   ├── filament_catalog_filamentcolors.json
│   └── filamentcolors_state.json
├── debug
│   ├── height_layers.npy
│   ├── height_mm.npy
│   ├── height.png
│   ├── labels.png
│   ├── layer_plan.json
│   ├── layers_by_label.json
│   ├── palette_assigned.json
│   ├── palette_suggested.json
│   ├── palette.png
│   ├── preprocess.png
│   └── preview.png
├── examples
│   ├── input.png
│   └── README.md
├── filaments
│   └── default_catalog.json
├── imgenv
│   ├── bin
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── Activate.ps1
│   │   ├── f2py
│   │   ├── fastapi
│   │   ├── httpx
│   │   ├── numpy-config
│   │   ├── pip
│   │   ├── pip3
│   │   ├── pip3.13
│   │   ├── py.test
│   │   ├── pygmentize
│   │   ├── pytest
│   │   ├── python -> python3.13
│   │   ├── python3 -> python3.13
│   │   ├── python3.13 -> /Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13
│   │   └── uvicorn
│   ├── include
│   │   └── python3.13
│   ├── lib
│   │   └── python3.13
│   │       └── site-packages
│   │           ├── __pycache__
│   │           │   ├── py.cpython-313.pyc
│   │           │   └── typing_extensions.cpython-313.pyc
│   │           ├── _pytest
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── _argcomplete.cpython-313.pyc
│   │           │   │   ├── _version.cpython-313.pyc
│   │           │   │   ├── cacheprovider.cpython-313.pyc
│   │           │   │   ├── capture.cpython-313.pyc
│   │           │   │   ├── compat.cpython-313.pyc
│   │           │   │   ├── debugging.cpython-313.pyc
│   │           │   │   ├── deprecated.cpython-313.pyc
│   │           │   │   ├── doctest.cpython-313.pyc
│   │           │   │   ├── faulthandler.cpython-313.pyc
│   │           │   │   ├── fixtures.cpython-313.pyc
│   │           │   │   ├── freeze_support.cpython-313.pyc
│   │           │   │   ├── helpconfig.cpython-313.pyc
│   │           │   │   ├── hookspec.cpython-313.pyc
│   │           │   │   ├── junitxml.cpython-313.pyc
│   │           │   │   ├── legacypath.cpython-313.pyc
│   │           │   │   ├── logging.cpython-313.pyc
│   │           │   │   ├── main.cpython-313.pyc
│   │           │   │   ├── monkeypatch.cpython-313.pyc
│   │           │   │   ├── nodes.cpython-313.pyc
│   │           │   │   ├── outcomes.cpython-313.pyc
│   │           │   │   ├── pastebin.cpython-313.pyc
│   │           │   │   ├── pathlib.cpython-313.pyc
│   │           │   │   ├── pytester_assertions.cpython-313.pyc
│   │           │   │   ├── pytester.cpython-313.pyc
│   │           │   │   ├── python_api.cpython-313.pyc
│   │           │   │   ├── python.cpython-313.pyc
│   │           │   │   ├── raises.cpython-313.pyc
│   │           │   │   ├── recwarn.cpython-313.pyc
│   │           │   │   ├── reports.cpython-313.pyc
│   │           │   │   ├── runner.cpython-313.pyc
│   │           │   │   ├── scope.cpython-313.pyc
│   │           │   │   ├── setuponly.cpython-313.pyc
│   │           │   │   ├── setupplan.cpython-313.pyc
│   │           │   │   ├── skipping.cpython-313.pyc
│   │           │   │   ├── stash.cpython-313.pyc
│   │           │   │   ├── stepwise.cpython-313.pyc
│   │           │   │   ├── subtests.cpython-313.pyc
│   │           │   │   ├── terminal.cpython-313.pyc
│   │           │   │   ├── terminalprogress.cpython-313.pyc
│   │           │   │   ├── threadexception.cpython-313.pyc
│   │           │   │   ├── timing.cpython-313.pyc
│   │           │   │   ├── tmpdir.cpython-313.pyc
│   │           │   │   ├── tracemalloc.cpython-313.pyc
│   │           │   │   ├── unittest.cpython-313.pyc
│   │           │   │   ├── unraisableexception.cpython-313.pyc
│   │           │   │   ├── warning_types.cpython-313.pyc
│   │           │   │   └── warnings.cpython-313.pyc
│   │           │   ├── _code
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── code.cpython-313.pyc
│   │           │   │   │   └── source.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── code.py
│   │           │   │   └── source.py
│   │           │   ├── _io
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── pprint.cpython-313.pyc
│   │           │   │   │   ├── saferepr.cpython-313.pyc
│   │           │   │   │   ├── terminalwriter.cpython-313.pyc
│   │           │   │   │   └── wcwidth.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── pprint.py
│   │           │   │   ├── saferepr.py
│   │           │   │   ├── terminalwriter.py
│   │           │   │   └── wcwidth.py
│   │           │   ├── _py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── error.cpython-313.pyc
│   │           │   │   │   └── path.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── error.py
│   │           │   │   └── path.py
│   │           │   ├── assertion
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── rewrite.cpython-313.pyc
│   │           │   │   │   ├── truncate.cpython-313.pyc
│   │           │   │   │   └── util.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── rewrite.py
│   │           │   │   ├── truncate.py
│   │           │   │   └── util.py
│   │           │   ├── config
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── argparsing.cpython-313.pyc
│   │           │   │   │   ├── compat.cpython-313.pyc
│   │           │   │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   │   └── findpaths.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── argparsing.py
│   │           │   │   ├── compat.py
│   │           │   │   ├── exceptions.py
│   │           │   │   └── findpaths.py
│   │           │   ├── mark
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── expression.cpython-313.pyc
│   │           │   │   │   └── structures.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── expression.py
│   │           │   │   └── structures.py
│   │           │   ├── __init__.py
│   │           │   ├── _argcomplete.py
│   │           │   ├── _version.py
│   │           │   ├── cacheprovider.py
│   │           │   ├── capture.py
│   │           │   ├── compat.py
│   │           │   ├── debugging.py
│   │           │   ├── deprecated.py
│   │           │   ├── doctest.py
│   │           │   ├── faulthandler.py
│   │           │   ├── fixtures.py
│   │           │   ├── freeze_support.py
│   │           │   ├── helpconfig.py
│   │           │   ├── hookspec.py
│   │           │   ├── junitxml.py
│   │           │   ├── legacypath.py
│   │           │   ├── logging.py
│   │           │   ├── main.py
│   │           │   ├── monkeypatch.py
│   │           │   ├── nodes.py
│   │           │   ├── outcomes.py
│   │           │   ├── pastebin.py
│   │           │   ├── pathlib.py
│   │           │   ├── py.typed
│   │           │   ├── pytester_assertions.py
│   │           │   ├── pytester.py
│   │           │   ├── python_api.py
│   │           │   ├── python.py
│   │           │   ├── raises.py
│   │           │   ├── recwarn.py
│   │           │   ├── reports.py
│   │           │   ├── runner.py
│   │           │   ├── scope.py
│   │           │   ├── setuponly.py
│   │           │   ├── setupplan.py
│   │           │   ├── skipping.py
│   │           │   ├── stash.py
│   │           │   ├── stepwise.py
│   │           │   ├── subtests.py
│   │           │   ├── terminal.py
│   │           │   ├── terminalprogress.py
│   │           │   ├── threadexception.py
│   │           │   ├── timing.py
│   │           │   ├── tmpdir.py
│   │           │   ├── tracemalloc.py
│   │           │   ├── unittest.py
│   │           │   ├── unraisableexception.py
│   │           │   ├── warning_types.py
│   │           │   └── warnings.py
│   │           ├── annotated_doc
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   └── main.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── main.py
│   │           │   └── py.typed
│   │           ├── annotated_doc-0.0.4.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── annotated_types
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   └── test_cases.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── py.typed
│   │           │   └── test_cases.py
│   │           ├── annotated_types-0.7.0.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── anyio
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313-pytest-9.0.2.pyc
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── from_thread.cpython-313-pytest-9.0.2.pyc
│   │           │   │   ├── from_thread.cpython-313.pyc
│   │           │   │   ├── functools.cpython-313.pyc
│   │           │   │   ├── lowlevel.cpython-313-pytest-9.0.2.pyc
│   │           │   │   ├── lowlevel.cpython-313.pyc
│   │           │   │   ├── pytest_plugin.cpython-313-pytest-9.0.2.pyc
│   │           │   │   ├── pytest_plugin.cpython-313.pyc
│   │           │   │   ├── to_interpreter.cpython-313.pyc
│   │           │   │   ├── to_process.cpython-313.pyc
│   │           │   │   ├── to_thread.cpython-313-pytest-9.0.2.pyc
│   │           │   │   └── to_thread.cpython-313.pyc
│   │           │   ├── _backends
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _asyncio.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _asyncio.cpython-313.pyc
│   │           │   │   │   ├── _trio.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   └── _trio.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _asyncio.py
│   │           │   │   └── _trio.py
│   │           │   ├── _core
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _asyncio_selector_thread.cpython-313.pyc
│   │           │   │   │   ├── _contextmanagers.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _contextmanagers.cpython-313.pyc
│   │           │   │   │   ├── _eventloop.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _eventloop.cpython-313.pyc
│   │           │   │   │   ├── _exceptions.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _exceptions.cpython-313.pyc
│   │           │   │   │   ├── _fileio.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _fileio.cpython-313.pyc
│   │           │   │   │   ├── _resources.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _resources.cpython-313.pyc
│   │           │   │   │   ├── _signals.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _signals.cpython-313.pyc
│   │           │   │   │   ├── _sockets.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _sockets.cpython-313.pyc
│   │           │   │   │   ├── _streams.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _streams.cpython-313.pyc
│   │           │   │   │   ├── _subprocesses.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _subprocesses.cpython-313.pyc
│   │           │   │   │   ├── _synchronization.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _synchronization.cpython-313.pyc
│   │           │   │   │   ├── _tasks.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _tasks.cpython-313.pyc
│   │           │   │   │   ├── _tempfile.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _tempfile.cpython-313.pyc
│   │           │   │   │   ├── _testing.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _testing.cpython-313.pyc
│   │           │   │   │   ├── _typedattr.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   └── _typedattr.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _asyncio_selector_thread.py
│   │           │   │   ├── _contextmanagers.py
│   │           │   │   ├── _eventloop.py
│   │           │   │   ├── _exceptions.py
│   │           │   │   ├── _fileio.py
│   │           │   │   ├── _resources.py
│   │           │   │   ├── _signals.py
│   │           │   │   ├── _sockets.py
│   │           │   │   ├── _streams.py
│   │           │   │   ├── _subprocesses.py
│   │           │   │   ├── _synchronization.py
│   │           │   │   ├── _tasks.py
│   │           │   │   ├── _tempfile.py
│   │           │   │   ├── _testing.py
│   │           │   │   └── _typedattr.py
│   │           │   ├── abc
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _eventloop.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _eventloop.cpython-313.pyc
│   │           │   │   │   ├── _resources.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _resources.cpython-313.pyc
│   │           │   │   │   ├── _sockets.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _sockets.cpython-313.pyc
│   │           │   │   │   ├── _streams.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _streams.cpython-313.pyc
│   │           │   │   │   ├── _subprocesses.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _subprocesses.cpython-313.pyc
│   │           │   │   │   ├── _tasks.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── _tasks.cpython-313.pyc
│   │           │   │   │   ├── _testing.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   └── _testing.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _eventloop.py
│   │           │   │   ├── _resources.py
│   │           │   │   ├── _sockets.py
│   │           │   │   ├── _streams.py
│   │           │   │   ├── _subprocesses.py
│   │           │   │   ├── _tasks.py
│   │           │   │   └── _testing.py
│   │           │   ├── streams
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── buffered.cpython-313.pyc
│   │           │   │   │   ├── file.cpython-313.pyc
│   │           │   │   │   ├── memory.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── memory.cpython-313.pyc
│   │           │   │   │   ├── stapled.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   ├── stapled.cpython-313.pyc
│   │           │   │   │   ├── text.cpython-313.pyc
│   │           │   │   │   ├── tls.cpython-313-pytest-9.0.2.pyc
│   │           │   │   │   └── tls.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── buffered.py
│   │           │   │   ├── file.py
│   │           │   │   ├── memory.py
│   │           │   │   ├── stapled.py
│   │           │   │   ├── text.py
│   │           │   │   └── tls.py
│   │           │   ├── __init__.py
│   │           │   ├── from_thread.py
│   │           │   ├── functools.py
│   │           │   ├── lowlevel.py
│   │           │   ├── py.typed
│   │           │   ├── pytest_plugin.py
│   │           │   ├── to_interpreter.py
│   │           │   ├── to_process.py
│   │           │   └── to_thread.py
│   │           ├── anyio-4.12.0.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── certifi
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── __main__.cpython-313.pyc
│   │           │   │   └── core.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── cacert.pem
│   │           │   ├── core.py
│   │           │   └── py.typed
│   │           ├── certifi-2025.11.12.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── click
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── _compat.cpython-313.pyc
│   │           │   │   ├── _termui_impl.cpython-313.pyc
│   │           │   │   ├── _textwrap.cpython-313.pyc
│   │           │   │   ├── _utils.cpython-313.pyc
│   │           │   │   ├── _winconsole.cpython-313.pyc
│   │           │   │   ├── core.cpython-313.pyc
│   │           │   │   ├── decorators.cpython-313.pyc
│   │           │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   ├── formatting.cpython-313.pyc
│   │           │   │   ├── globals.cpython-313.pyc
│   │           │   │   ├── parser.cpython-313.pyc
│   │           │   │   ├── shell_completion.cpython-313.pyc
│   │           │   │   ├── termui.cpython-313.pyc
│   │           │   │   ├── testing.cpython-313.pyc
│   │           │   │   ├── types.cpython-313.pyc
│   │           │   │   └── utils.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── _compat.py
│   │           │   ├── _termui_impl.py
│   │           │   ├── _textwrap.py
│   │           │   ├── _utils.py
│   │           │   ├── _winconsole.py
│   │           │   ├── core.py
│   │           │   ├── decorators.py
│   │           │   ├── exceptions.py
│   │           │   ├── formatting.py
│   │           │   ├── globals.py
│   │           │   ├── parser.py
│   │           │   ├── py.typed
│   │           │   ├── shell_completion.py
│   │           │   ├── termui.py
│   │           │   ├── testing.py
│   │           │   ├── types.py
│   │           │   └── utils.py
│   │           ├── click-8.3.1.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── fastapi
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── __main__.cpython-313.pyc
│   │           │   │   ├── applications.cpython-313.pyc
│   │           │   │   ├── background.cpython-313.pyc
│   │           │   │   ├── cli.cpython-313.pyc
│   │           │   │   ├── concurrency.cpython-313.pyc
│   │           │   │   ├── datastructures.cpython-313.pyc
│   │           │   │   ├── encoders.cpython-313.pyc
│   │           │   │   ├── exception_handlers.cpython-313.pyc
│   │           │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   ├── logger.cpython-313.pyc
│   │           │   │   ├── param_functions.cpython-313.pyc
│   │           │   │   ├── params.cpython-313.pyc
│   │           │   │   ├── requests.cpython-313.pyc
│   │           │   │   ├── responses.cpython-313.pyc
│   │           │   │   ├── routing.cpython-313.pyc
│   │           │   │   ├── staticfiles.cpython-313.pyc
│   │           │   │   ├── temp_pydantic_v1_params.cpython-313.pyc
│   │           │   │   ├── templating.cpython-313.pyc
│   │           │   │   ├── testclient.cpython-313.pyc
│   │           │   │   ├── types.cpython-313.pyc
│   │           │   │   ├── utils.cpython-313.pyc
│   │           │   │   └── websockets.cpython-313.pyc
│   │           │   ├── _compat
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── main.cpython-313.pyc
│   │           │   │   │   ├── may_v1.cpython-313.pyc
│   │           │   │   │   ├── model_field.cpython-313.pyc
│   │           │   │   │   ├── shared.cpython-313.pyc
│   │           │   │   │   ├── v1.cpython-313.pyc
│   │           │   │   │   └── v2.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── main.py
│   │           │   │   ├── may_v1.py
│   │           │   │   ├── model_field.py
│   │           │   │   ├── shared.py
│   │           │   │   ├── v1.py
│   │           │   │   └── v2.py
│   │           │   ├── dependencies
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── models.cpython-313.pyc
│   │           │   │   │   └── utils.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── models.py
│   │           │   │   └── utils.py
│   │           │   ├── middleware
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── asyncexitstack.cpython-313.pyc
│   │           │   │   │   ├── cors.cpython-313.pyc
│   │           │   │   │   ├── gzip.cpython-313.pyc
│   │           │   │   │   ├── httpsredirect.cpython-313.pyc
│   │           │   │   │   ├── trustedhost.cpython-313.pyc
│   │           │   │   │   └── wsgi.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── asyncexitstack.py
│   │           │   │   ├── cors.py
│   │           │   │   ├── gzip.py
│   │           │   │   ├── httpsredirect.py
│   │           │   │   ├── trustedhost.py
│   │           │   │   └── wsgi.py
│   │           │   ├── openapi
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── constants.cpython-313.pyc
│   │           │   │   │   ├── docs.cpython-313.pyc
│   │           │   │   │   ├── models.cpython-313.pyc
│   │           │   │   │   └── utils.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── constants.py
│   │           │   │   ├── docs.py
│   │           │   │   ├── models.py
│   │           │   │   └── utils.py
│   │           │   ├── security
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── api_key.cpython-313.pyc
│   │           │   │   │   ├── base.cpython-313.pyc
│   │           │   │   │   ├── http.cpython-313.pyc
│   │           │   │   │   ├── oauth2.cpython-313.pyc
│   │           │   │   │   ├── open_id_connect_url.cpython-313.pyc
│   │           │   │   │   └── utils.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── api_key.py
│   │           │   │   ├── base.py
│   │           │   │   ├── http.py
│   │           │   │   ├── oauth2.py
│   │           │   │   ├── open_id_connect_url.py
│   │           │   │   └── utils.py
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── applications.py
│   │           │   ├── background.py
│   │           │   ├── cli.py
│   │           │   ├── concurrency.py
│   │           │   ├── datastructures.py
│   │           │   ├── encoders.py
│   │           │   ├── exception_handlers.py
│   │           │   ├── exceptions.py
│   │           │   ├── logger.py
│   │           │   ├── param_functions.py
│   │           │   ├── params.py
│   │           │   ├── py.typed
│   │           │   ├── requests.py
│   │           │   ├── responses.py
│   │           │   ├── routing.py
│   │           │   ├── staticfiles.py
│   │           │   ├── temp_pydantic_v1_params.py
│   │           │   ├── templating.py
│   │           │   ├── testclient.py
│   │           │   ├── types.py
│   │           │   ├── utils.py
│   │           │   └── websockets.py
│   │           ├── fastapi-0.127.0.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── h11
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── _abnf.cpython-313.pyc
│   │           │   │   ├── _connection.cpython-313.pyc
│   │           │   │   ├── _events.cpython-313.pyc
│   │           │   │   ├── _headers.cpython-313.pyc
│   │           │   │   ├── _readers.cpython-313.pyc
│   │           │   │   ├── _receivebuffer.cpython-313.pyc
│   │           │   │   ├── _state.cpython-313.pyc
│   │           │   │   ├── _util.cpython-313.pyc
│   │           │   │   ├── _version.cpython-313.pyc
│   │           │   │   └── _writers.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── _abnf.py
│   │           │   ├── _connection.py
│   │           │   ├── _events.py
│   │           │   ├── _headers.py
│   │           │   ├── _readers.py
│   │           │   ├── _receivebuffer.py
│   │           │   ├── _state.py
│   │           │   ├── _util.py
│   │           │   ├── _version.py
│   │           │   ├── _writers.py
│   │           │   └── py.typed
│   │           ├── h11-0.16.0.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── httpcore
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── _api.cpython-313.pyc
│   │           │   │   ├── _exceptions.cpython-313.pyc
│   │           │   │   ├── _models.cpython-313.pyc
│   │           │   │   ├── _ssl.cpython-313.pyc
│   │           │   │   ├── _synchronization.cpython-313.pyc
│   │           │   │   ├── _trace.cpython-313.pyc
│   │           │   │   └── _utils.cpython-313.pyc
│   │           │   ├── _async
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── connection_pool.cpython-313.pyc
│   │           │   │   │   ├── connection.cpython-313.pyc
│   │           │   │   │   ├── http_proxy.cpython-313.pyc
│   │           │   │   │   ├── http11.cpython-313.pyc
│   │           │   │   │   ├── http2.cpython-313.pyc
│   │           │   │   │   ├── interfaces.cpython-313.pyc
│   │           │   │   │   └── socks_proxy.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── connection_pool.py
│   │           │   │   ├── connection.py
│   │           │   │   ├── http_proxy.py
│   │           │   │   ├── http11.py
│   │           │   │   ├── http2.py
│   │           │   │   ├── interfaces.py
│   │           │   │   └── socks_proxy.py
│   │           │   ├── _backends
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── anyio.cpython-313.pyc
│   │           │   │   │   ├── auto.cpython-313.pyc
│   │           │   │   │   ├── base.cpython-313.pyc
│   │           │   │   │   ├── mock.cpython-313.pyc
│   │           │   │   │   ├── sync.cpython-313.pyc
│   │           │   │   │   └── trio.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── anyio.py
│   │           │   │   ├── auto.py
│   │           │   │   ├── base.py
│   │           │   │   ├── mock.py
│   │           │   │   ├── sync.py
│   │           │   │   └── trio.py
│   │           │   ├── _sync
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── connection_pool.cpython-313.pyc
│   │           │   │   │   ├── connection.cpython-313.pyc
│   │           │   │   │   ├── http_proxy.cpython-313.pyc
│   │           │   │   │   ├── http11.cpython-313.pyc
│   │           │   │   │   ├── http2.cpython-313.pyc
│   │           │   │   │   ├── interfaces.cpython-313.pyc
│   │           │   │   │   └── socks_proxy.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── connection_pool.py
│   │           │   │   ├── connection.py
│   │           │   │   ├── http_proxy.py
│   │           │   │   ├── http11.py
│   │           │   │   ├── http2.py
│   │           │   │   ├── interfaces.py
│   │           │   │   └── socks_proxy.py
│   │           │   ├── __init__.py
│   │           │   ├── _api.py
│   │           │   ├── _exceptions.py
│   │           │   ├── _models.py
│   │           │   ├── _ssl.py
│   │           │   ├── _synchronization.py
│   │           │   ├── _trace.py
│   │           │   ├── _utils.py
│   │           │   └── py.typed
│   │           ├── httpcore-1.0.9.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE.md
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── httpx
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── __version__.cpython-313.pyc
│   │           │   │   ├── _api.cpython-313.pyc
│   │           │   │   ├── _auth.cpython-313.pyc
│   │           │   │   ├── _client.cpython-313.pyc
│   │           │   │   ├── _config.cpython-313.pyc
│   │           │   │   ├── _content.cpython-313.pyc
│   │           │   │   ├── _decoders.cpython-313.pyc
│   │           │   │   ├── _exceptions.cpython-313.pyc
│   │           │   │   ├── _main.cpython-313.pyc
│   │           │   │   ├── _models.cpython-313.pyc
│   │           │   │   ├── _multipart.cpython-313.pyc
│   │           │   │   ├── _status_codes.cpython-313.pyc
│   │           │   │   ├── _types.cpython-313.pyc
│   │           │   │   ├── _urlparse.cpython-313.pyc
│   │           │   │   ├── _urls.cpython-313.pyc
│   │           │   │   └── _utils.cpython-313.pyc
│   │           │   ├── _transports
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── asgi.cpython-313.pyc
│   │           │   │   │   ├── base.cpython-313.pyc
│   │           │   │   │   ├── default.cpython-313.pyc
│   │           │   │   │   ├── mock.cpython-313.pyc
│   │           │   │   │   └── wsgi.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── asgi.py
│   │           │   │   ├── base.py
│   │           │   │   ├── default.py
│   │           │   │   ├── mock.py
│   │           │   │   └── wsgi.py
│   │           │   ├── __init__.py
│   │           │   ├── __version__.py
│   │           │   ├── _api.py
│   │           │   ├── _auth.py
│   │           │   ├── _client.py
│   │           │   ├── _config.py
│   │           │   ├── _content.py
│   │           │   ├── _decoders.py
│   │           │   ├── _exceptions.py
│   │           │   ├── _main.py
│   │           │   ├── _models.py
│   │           │   ├── _multipart.py
│   │           │   ├── _status_codes.py
│   │           │   ├── _types.py
│   │           │   ├── _urlparse.py
│   │           │   ├── _urls.py
│   │           │   ├── _utils.py
│   │           │   └── py.typed
│   │           ├── httpx-0.28.1.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE.md
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── idna
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── codec.cpython-313.pyc
│   │           │   │   ├── compat.cpython-313.pyc
│   │           │   │   ├── core.cpython-313.pyc
│   │           │   │   ├── idnadata.cpython-313.pyc
│   │           │   │   ├── intranges.cpython-313.pyc
│   │           │   │   ├── package_data.cpython-313.pyc
│   │           │   │   └── uts46data.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── codec.py
│   │           │   ├── compat.py
│   │           │   ├── core.py
│   │           │   ├── idnadata.py
│   │           │   ├── intranges.py
│   │           │   ├── package_data.py
│   │           │   ├── py.typed
│   │           │   └── uts46data.py
│   │           ├── idna-3.11.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE.md
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── image_to_3d_relief-1.0.0.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── direct_url.json
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── iniconfig
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── _parse.cpython-313.pyc
│   │           │   │   ├── _version.cpython-313.pyc
│   │           │   │   └── exceptions.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── _parse.py
│   │           │   ├── _version.py
│   │           │   ├── exceptions.py
│   │           │   └── py.typed
│   │           ├── iniconfig-2.3.0.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── multipart
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── decoders.cpython-313.pyc
│   │           │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   └── multipart.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── decoders.py
│   │           │   ├── exceptions.py
│   │           │   └── multipart.py
│   │           ├── numpy
│   │           │   ├── __pycache__
│   │           │   │   ├── __config__.cpython-313.pyc
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── _array_api_info.cpython-313.pyc
│   │           │   │   ├── _configtool.cpython-313.pyc
│   │           │   │   ├── _distributor_init.cpython-313.pyc
│   │           │   │   ├── _expired_attrs_2_0.cpython-313.pyc
│   │           │   │   ├── _globals.cpython-313.pyc
│   │           │   │   ├── _pytesttester.cpython-313.pyc
│   │           │   │   ├── conftest.cpython-313.pyc
│   │           │   │   ├── dtypes.cpython-313.pyc
│   │           │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   ├── matlib.cpython-313.pyc
│   │           │   │   └── version.cpython-313.pyc
│   │           │   ├── _core
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _add_newdocs_scalars.cpython-313.pyc
│   │           │   │   │   ├── _add_newdocs.cpython-313.pyc
│   │           │   │   │   ├── _asarray.cpython-313.pyc
│   │           │   │   │   ├── _dtype_ctypes.cpython-313.pyc
│   │           │   │   │   ├── _dtype.cpython-313.pyc
│   │           │   │   │   ├── _exceptions.cpython-313.pyc
│   │           │   │   │   ├── _internal.cpython-313.pyc
│   │           │   │   │   ├── _methods.cpython-313.pyc
│   │           │   │   │   ├── _string_helpers.cpython-313.pyc
│   │           │   │   │   ├── _type_aliases.cpython-313.pyc
│   │           │   │   │   ├── _ufunc_config.cpython-313.pyc
│   │           │   │   │   ├── arrayprint.cpython-313.pyc
│   │           │   │   │   ├── cversions.cpython-313.pyc
│   │           │   │   │   ├── defchararray.cpython-313.pyc
│   │           │   │   │   ├── einsumfunc.cpython-313.pyc
│   │           │   │   │   ├── fromnumeric.cpython-313.pyc
│   │           │   │   │   ├── function_base.cpython-313.pyc
│   │           │   │   │   ├── getlimits.cpython-313.pyc
│   │           │   │   │   ├── memmap.cpython-313.pyc
│   │           │   │   │   ├── multiarray.cpython-313.pyc
│   │           │   │   │   ├── numeric.cpython-313.pyc
│   │           │   │   │   ├── numerictypes.cpython-313.pyc
│   │           │   │   │   ├── overrides.cpython-313.pyc
│   │           │   │   │   ├── printoptions.cpython-313.pyc
│   │           │   │   │   ├── records.cpython-313.pyc
│   │           │   │   │   ├── shape_base.cpython-313.pyc
│   │           │   │   │   ├── strings.cpython-313.pyc
│   │           │   │   │   └── umath.cpython-313.pyc
│   │           │   │   ├── include
│   │           │   │   │   └── numpy
│   │           │   │   │       ├── random
│   │           │   │   │       │   ├── bitgen.h
│   │           │   │   │       │   ├── distributions.h
│   │           │   │   │       │   ├── libdivide.h
│   │           │   │   │       │   └── LICENSE.txt
│   │           │   │   │       ├── __multiarray_api.c
│   │           │   │   │       ├── __multiarray_api.h
│   │           │   │   │       ├── __ufunc_api.c
│   │           │   │   │       ├── __ufunc_api.h
│   │           │   │   │       ├── _neighborhood_iterator_imp.h
│   │           │   │   │       ├── _numpyconfig.h
│   │           │   │   │       ├── _public_dtype_api_table.h
│   │           │   │   │       ├── arrayobject.h
│   │           │   │   │       ├── arrayscalars.h
│   │           │   │   │       ├── dtype_api.h
│   │           │   │   │       ├── halffloat.h
│   │           │   │   │       ├── ndarrayobject.h
│   │           │   │   │       ├── ndarraytypes.h
│   │           │   │   │       ├── npy_2_compat.h
│   │           │   │   │       ├── npy_2_complexcompat.h
│   │           │   │   │       ├── npy_3kcompat.h
│   │           │   │   │       ├── npy_common.h
│   │           │   │   │       ├── npy_cpu.h
│   │           │   │   │       ├── npy_endian.h
│   │           │   │   │       ├── npy_math.h
│   │           │   │   │       ├── npy_no_deprecated_api.h
│   │           │   │   │       ├── npy_os.h
│   │           │   │   │       ├── numpyconfig.h
│   │           │   │   │       ├── ufuncobject.h
│   │           │   │   │       └── utils.h
│   │           │   │   ├── lib
│   │           │   │   │   ├── npy-pkg-config
│   │           │   │   │   │   ├── mlib.ini
│   │           │   │   │   │   └── npymath.ini
│   │           │   │   │   ├── pkgconfig
│   │           │   │   │   │   └── numpy.pc
│   │           │   │   │   └── libnpymath.a
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── _locales.cpython-313.pyc
│   │           │   │   │   │   ├── _natype.cpython-313.pyc
│   │           │   │   │   │   ├── test__exceptions.cpython-313.pyc
│   │           │   │   │   │   ├── test_abc.cpython-313.pyc
│   │           │   │   │   │   ├── test_api.cpython-313.pyc
│   │           │   │   │   │   ├── test_argparse.cpython-313.pyc
│   │           │   │   │   │   ├── test_array_api_info.cpython-313.pyc
│   │           │   │   │   │   ├── test_array_coercion.cpython-313.pyc
│   │           │   │   │   │   ├── test_array_interface.cpython-313.pyc
│   │           │   │   │   │   ├── test_arraymethod.cpython-313.pyc
│   │           │   │   │   │   ├── test_arrayobject.cpython-313.pyc
│   │           │   │   │   │   ├── test_arrayprint.cpython-313.pyc
│   │           │   │   │   │   ├── test_casting_floatingpoint_errors.cpython-313.pyc
│   │           │   │   │   │   ├── test_casting_unittests.cpython-313.pyc
│   │           │   │   │   │   ├── test_conversion_utils.cpython-313.pyc
│   │           │   │   │   │   ├── test_cpu_dispatcher.cpython-313.pyc
│   │           │   │   │   │   ├── test_cpu_features.cpython-313.pyc
│   │           │   │   │   │   ├── test_custom_dtypes.cpython-313.pyc
│   │           │   │   │   │   ├── test_cython.cpython-313.pyc
│   │           │   │   │   │   ├── test_datetime.cpython-313.pyc
│   │           │   │   │   │   ├── test_defchararray.cpython-313.pyc
│   │           │   │   │   │   ├── test_deprecations.cpython-313.pyc
│   │           │   │   │   │   ├── test_dlpack.cpython-313.pyc
│   │           │   │   │   │   ├── test_dtype.cpython-313.pyc
│   │           │   │   │   │   ├── test_einsum.cpython-313.pyc
│   │           │   │   │   │   ├── test_errstate.cpython-313.pyc
│   │           │   │   │   │   ├── test_extint128.cpython-313.pyc
│   │           │   │   │   │   ├── test_finfo.cpython-313.pyc
│   │           │   │   │   │   ├── test_function_base.cpython-313.pyc
│   │           │   │   │   │   ├── test_getlimits.cpython-313.pyc
│   │           │   │   │   │   ├── test_half.cpython-313.pyc
│   │           │   │   │   │   ├── test_hashtable.cpython-313.pyc
│   │           │   │   │   │   ├── test_indexerrors.cpython-313.pyc
│   │           │   │   │   │   ├── test_indexing.cpython-313.pyc
│   │           │   │   │   │   ├── test_item_selection.cpython-313.pyc
│   │           │   │   │   │   ├── test_limited_api.cpython-313.pyc
│   │           │   │   │   │   ├── test_longdouble.cpython-313.pyc
│   │           │   │   │   │   ├── test_mem_overlap.cpython-313.pyc
│   │           │   │   │   │   ├── test_mem_policy.cpython-313.pyc
│   │           │   │   │   │   ├── test_memmap.cpython-313.pyc
│   │           │   │   │   │   ├── test_multiarray.cpython-313.pyc
│   │           │   │   │   │   ├── test_multiprocessing.cpython-313.pyc
│   │           │   │   │   │   ├── test_multithreading.cpython-313.pyc
│   │           │   │   │   │   ├── test_nditer.cpython-313.pyc
│   │           │   │   │   │   ├── test_nep50_promotions.cpython-313.pyc
│   │           │   │   │   │   ├── test_numeric.cpython-313.pyc
│   │           │   │   │   │   ├── test_numerictypes.cpython-313.pyc
│   │           │   │   │   │   ├── test_overrides.cpython-313.pyc
│   │           │   │   │   │   ├── test_print.cpython-313.pyc
│   │           │   │   │   │   ├── test_protocols.cpython-313.pyc
│   │           │   │   │   │   ├── test_records.cpython-313.pyc
│   │           │   │   │   │   ├── test_regression.cpython-313.pyc
│   │           │   │   │   │   ├── test_scalar_ctors.cpython-313.pyc
│   │           │   │   │   │   ├── test_scalar_methods.cpython-313.pyc
│   │           │   │   │   │   ├── test_scalarbuffer.cpython-313.pyc
│   │           │   │   │   │   ├── test_scalarinherit.cpython-313.pyc
│   │           │   │   │   │   ├── test_scalarmath.cpython-313.pyc
│   │           │   │   │   │   ├── test_scalarprint.cpython-313.pyc
│   │           │   │   │   │   ├── test_shape_base.cpython-313.pyc
│   │           │   │   │   │   ├── test_simd_module.cpython-313.pyc
│   │           │   │   │   │   ├── test_simd.cpython-313.pyc
│   │           │   │   │   │   ├── test_stringdtype.cpython-313.pyc
│   │           │   │   │   │   ├── test_strings.cpython-313.pyc
│   │           │   │   │   │   ├── test_ufunc.cpython-313.pyc
│   │           │   │   │   │   ├── test_umath_accuracy.cpython-313.pyc
│   │           │   │   │   │   ├── test_umath_complex.cpython-313.pyc
│   │           │   │   │   │   ├── test_umath.cpython-313.pyc
│   │           │   │   │   │   └── test_unicode.cpython-313.pyc
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── astype_copy.pkl
│   │           │   │   │   │   ├── generate_umath_validation_data.cpp
│   │           │   │   │   │   ├── recarray_from_file.fits
│   │           │   │   │   │   ├── umath-validation-set-arccos.csv
│   │           │   │   │   │   ├── umath-validation-set-arccosh.csv
│   │           │   │   │   │   ├── umath-validation-set-arcsin.csv
│   │           │   │   │   │   ├── umath-validation-set-arcsinh.csv
│   │           │   │   │   │   ├── umath-validation-set-arctan.csv
│   │           │   │   │   │   ├── umath-validation-set-arctanh.csv
│   │           │   │   │   │   ├── umath-validation-set-cbrt.csv
│   │           │   │   │   │   ├── umath-validation-set-cos.csv
│   │           │   │   │   │   ├── umath-validation-set-cosh.csv
│   │           │   │   │   │   ├── umath-validation-set-exp.csv
│   │           │   │   │   │   ├── umath-validation-set-exp2.csv
│   │           │   │   │   │   ├── umath-validation-set-expm1.csv
│   │           │   │   │   │   ├── umath-validation-set-log.csv
│   │           │   │   │   │   ├── umath-validation-set-log10.csv
│   │           │   │   │   │   ├── umath-validation-set-log1p.csv
│   │           │   │   │   │   ├── umath-validation-set-log2.csv
│   │           │   │   │   │   ├── umath-validation-set-README.txt
│   │           │   │   │   │   ├── umath-validation-set-sin.csv
│   │           │   │   │   │   ├── umath-validation-set-sinh.csv
│   │           │   │   │   │   ├── umath-validation-set-tan.csv
│   │           │   │   │   │   └── umath-validation-set-tanh.csv
│   │           │   │   │   ├── examples
│   │           │   │   │   │   ├── cython
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   └── setup.cpython-313.pyc
│   │           │   │   │   │   │   ├── checks.pyx
│   │           │   │   │   │   │   ├── meson.build
│   │           │   │   │   │   │   └── setup.py
│   │           │   │   │   │   └── limited_api
│   │           │   │   │   │       ├── __pycache__
│   │           │   │   │   │       │   └── setup.cpython-313.pyc
│   │           │   │   │   │       ├── limited_api_latest.c
│   │           │   │   │   │       ├── limited_api1.c
│   │           │   │   │   │       ├── limited_api2.pyx
│   │           │   │   │   │       ├── meson.build
│   │           │   │   │   │       └── setup.py
│   │           │   │   │   ├── _locales.py
│   │           │   │   │   ├── _natype.py
│   │           │   │   │   ├── test__exceptions.py
│   │           │   │   │   ├── test_abc.py
│   │           │   │   │   ├── test_api.py
│   │           │   │   │   ├── test_argparse.py
│   │           │   │   │   ├── test_array_api_info.py
│   │           │   │   │   ├── test_array_coercion.py
│   │           │   │   │   ├── test_array_interface.py
│   │           │   │   │   ├── test_arraymethod.py
│   │           │   │   │   ├── test_arrayobject.py
│   │           │   │   │   ├── test_arrayprint.py
│   │           │   │   │   ├── test_casting_floatingpoint_errors.py
│   │           │   │   │   ├── test_casting_unittests.py
│   │           │   │   │   ├── test_conversion_utils.py
│   │           │   │   │   ├── test_cpu_dispatcher.py
│   │           │   │   │   ├── test_cpu_features.py
│   │           │   │   │   ├── test_custom_dtypes.py
│   │           │   │   │   ├── test_cython.py
│   │           │   │   │   ├── test_datetime.py
│   │           │   │   │   ├── test_defchararray.py
│   │           │   │   │   ├── test_deprecations.py
│   │           │   │   │   ├── test_dlpack.py
│   │           │   │   │   ├── test_dtype.py
│   │           │   │   │   ├── test_einsum.py
│   │           │   │   │   ├── test_errstate.py
│   │           │   │   │   ├── test_extint128.py
│   │           │   │   │   ├── test_finfo.py
│   │           │   │   │   ├── test_function_base.py
│   │           │   │   │   ├── test_getlimits.py
│   │           │   │   │   ├── test_half.py
│   │           │   │   │   ├── test_hashtable.py
│   │           │   │   │   ├── test_indexerrors.py
│   │           │   │   │   ├── test_indexing.py
│   │           │   │   │   ├── test_item_selection.py
│   │           │   │   │   ├── test_limited_api.py
│   │           │   │   │   ├── test_longdouble.py
│   │           │   │   │   ├── test_mem_overlap.py
│   │           │   │   │   ├── test_mem_policy.py
│   │           │   │   │   ├── test_memmap.py
│   │           │   │   │   ├── test_multiarray.py
│   │           │   │   │   ├── test_multiprocessing.py
│   │           │   │   │   ├── test_multithreading.py
│   │           │   │   │   ├── test_nditer.py
│   │           │   │   │   ├── test_nep50_promotions.py
│   │           │   │   │   ├── test_numeric.py
│   │           │   │   │   ├── test_numerictypes.py
│   │           │   │   │   ├── test_overrides.py
│   │           │   │   │   ├── test_print.py
│   │           │   │   │   ├── test_protocols.py
│   │           │   │   │   ├── test_records.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test_scalar_ctors.py
│   │           │   │   │   ├── test_scalar_methods.py
│   │           │   │   │   ├── test_scalarbuffer.py
│   │           │   │   │   ├── test_scalarinherit.py
│   │           │   │   │   ├── test_scalarmath.py
│   │           │   │   │   ├── test_scalarprint.py
│   │           │   │   │   ├── test_shape_base.py
│   │           │   │   │   ├── test_simd_module.py
│   │           │   │   │   ├── test_simd.py
│   │           │   │   │   ├── test_stringdtype.py
│   │           │   │   │   ├── test_strings.py
│   │           │   │   │   ├── test_ufunc.py
│   │           │   │   │   ├── test_umath_accuracy.py
│   │           │   │   │   ├── test_umath_complex.py
│   │           │   │   │   ├── test_umath.py
│   │           │   │   │   └── test_unicode.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _add_newdocs_scalars.py
│   │           │   │   ├── _add_newdocs_scalars.pyi
│   │           │   │   ├── _add_newdocs.py
│   │           │   │   ├── _add_newdocs.pyi
│   │           │   │   ├── _asarray.py
│   │           │   │   ├── _asarray.pyi
│   │           │   │   ├── _dtype_ctypes.py
│   │           │   │   ├── _dtype_ctypes.pyi
│   │           │   │   ├── _dtype.py
│   │           │   │   ├── _dtype.pyi
│   │           │   │   ├── _exceptions.py
│   │           │   │   ├── _exceptions.pyi
│   │           │   │   ├── _internal.py
│   │           │   │   ├── _internal.pyi
│   │           │   │   ├── _methods.py
│   │           │   │   ├── _methods.pyi
│   │           │   │   ├── _multiarray_tests.cpython-313-darwin.so
│   │           │   │   ├── _multiarray_umath.cpython-313-darwin.so
│   │           │   │   ├── _operand_flag_tests.cpython-313-darwin.so
│   │           │   │   ├── _rational_tests.cpython-313-darwin.so
│   │           │   │   ├── _simd.cpython-313-darwin.so
│   │           │   │   ├── _simd.pyi
│   │           │   │   ├── _string_helpers.py
│   │           │   │   ├── _string_helpers.pyi
│   │           │   │   ├── _struct_ufunc_tests.cpython-313-darwin.so
│   │           │   │   ├── _type_aliases.py
│   │           │   │   ├── _type_aliases.pyi
│   │           │   │   ├── _ufunc_config.py
│   │           │   │   ├── _ufunc_config.pyi
│   │           │   │   ├── _umath_tests.cpython-313-darwin.so
│   │           │   │   ├── _umath_tests.pyi
│   │           │   │   ├── arrayprint.py
│   │           │   │   ├── arrayprint.pyi
│   │           │   │   ├── cversions.py
│   │           │   │   ├── defchararray.py
│   │           │   │   ├── defchararray.pyi
│   │           │   │   ├── einsumfunc.py
│   │           │   │   ├── einsumfunc.pyi
│   │           │   │   ├── fromnumeric.py
│   │           │   │   ├── fromnumeric.pyi
│   │           │   │   ├── function_base.py
│   │           │   │   ├── function_base.pyi
│   │           │   │   ├── getlimits.py
│   │           │   │   ├── getlimits.pyi
│   │           │   │   ├── memmap.py
│   │           │   │   ├── memmap.pyi
│   │           │   │   ├── multiarray.py
│   │           │   │   ├── multiarray.pyi
│   │           │   │   ├── numeric.py
│   │           │   │   ├── numeric.pyi
│   │           │   │   ├── numerictypes.py
│   │           │   │   ├── numerictypes.pyi
│   │           │   │   ├── overrides.py
│   │           │   │   ├── overrides.pyi
│   │           │   │   ├── printoptions.py
│   │           │   │   ├── printoptions.pyi
│   │           │   │   ├── records.py
│   │           │   │   ├── records.pyi
│   │           │   │   ├── shape_base.py
│   │           │   │   ├── shape_base.pyi
│   │           │   │   ├── strings.py
│   │           │   │   ├── strings.pyi
│   │           │   │   ├── umath.py
│   │           │   │   └── umath.pyi
│   │           │   ├── _pyinstaller
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   └── hook-numpy.cpython-313.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── pyinstaller-smoke.cpython-313.pyc
│   │           │   │   │   │   └── test_pyinstaller.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── pyinstaller-smoke.py
│   │           │   │   │   └── test_pyinstaller.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── hook-numpy.py
│   │           │   │   └── hook-numpy.pyi
│   │           │   ├── _typing
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _add_docstring.cpython-313.pyc
│   │           │   │   │   ├── _array_like.cpython-313.pyc
│   │           │   │   │   ├── _char_codes.cpython-313.pyc
│   │           │   │   │   ├── _dtype_like.cpython-313.pyc
│   │           │   │   │   ├── _extended_precision.cpython-313.pyc
│   │           │   │   │   ├── _nbit_base.cpython-313.pyc
│   │           │   │   │   ├── _nbit.cpython-313.pyc
│   │           │   │   │   ├── _nested_sequence.cpython-313.pyc
│   │           │   │   │   ├── _scalars.cpython-313.pyc
│   │           │   │   │   ├── _shape.cpython-313.pyc
│   │           │   │   │   └── _ufunc.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _add_docstring.py
│   │           │   │   ├── _array_like.py
│   │           │   │   ├── _char_codes.py
│   │           │   │   ├── _dtype_like.py
│   │           │   │   ├── _extended_precision.py
│   │           │   │   ├── _nbit_base.py
│   │           │   │   ├── _nbit_base.pyi
│   │           │   │   ├── _nbit.py
│   │           │   │   ├── _nested_sequence.py
│   │           │   │   ├── _scalars.py
│   │           │   │   ├── _shape.py
│   │           │   │   ├── _ufunc.py
│   │           │   │   └── _ufunc.pyi
│   │           │   ├── _utils
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _convertions.cpython-313.pyc
│   │           │   │   │   ├── _inspect.cpython-313.pyc
│   │           │   │   │   └── _pep440.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _convertions.py
│   │           │   │   ├── _convertions.pyi
│   │           │   │   ├── _inspect.py
│   │           │   │   ├── _inspect.pyi
│   │           │   │   ├── _pep440.py
│   │           │   │   └── _pep440.pyi
│   │           │   ├── char
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   └── __init__.pyi
│   │           │   ├── core
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _dtype_ctypes.cpython-313.pyc
│   │           │   │   │   ├── _dtype.cpython-313.pyc
│   │           │   │   │   ├── _internal.cpython-313.pyc
│   │           │   │   │   ├── _multiarray_umath.cpython-313.pyc
│   │           │   │   │   ├── _utils.cpython-313.pyc
│   │           │   │   │   ├── arrayprint.cpython-313.pyc
│   │           │   │   │   ├── defchararray.cpython-313.pyc
│   │           │   │   │   ├── einsumfunc.cpython-313.pyc
│   │           │   │   │   ├── fromnumeric.cpython-313.pyc
│   │           │   │   │   ├── function_base.cpython-313.pyc
│   │           │   │   │   ├── getlimits.cpython-313.pyc
│   │           │   │   │   ├── multiarray.cpython-313.pyc
│   │           │   │   │   ├── numeric.cpython-313.pyc
│   │           │   │   │   ├── numerictypes.cpython-313.pyc
│   │           │   │   │   ├── overrides.cpython-313.pyc
│   │           │   │   │   ├── records.cpython-313.pyc
│   │           │   │   │   ├── shape_base.cpython-313.pyc
│   │           │   │   │   └── umath.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _dtype_ctypes.py
│   │           │   │   ├── _dtype_ctypes.pyi
│   │           │   │   ├── _dtype.py
│   │           │   │   ├── _dtype.pyi
│   │           │   │   ├── _internal.py
│   │           │   │   ├── _multiarray_umath.py
│   │           │   │   ├── _utils.py
│   │           │   │   ├── arrayprint.py
│   │           │   │   ├── defchararray.py
│   │           │   │   ├── einsumfunc.py
│   │           │   │   ├── fromnumeric.py
│   │           │   │   ├── function_base.py
│   │           │   │   ├── getlimits.py
│   │           │   │   ├── multiarray.py
│   │           │   │   ├── numeric.py
│   │           │   │   ├── numerictypes.py
│   │           │   │   ├── overrides.py
│   │           │   │   ├── overrides.pyi
│   │           │   │   ├── records.py
│   │           │   │   ├── shape_base.py
│   │           │   │   └── umath.py
│   │           │   ├── ctypeslib
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   └── _ctypeslib.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _ctypeslib.py
│   │           │   │   └── _ctypeslib.pyi
│   │           │   ├── doc
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── ufuncs.cpython-313.pyc
│   │           │   │   └── ufuncs.py
│   │           │   ├── f2py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── __main__.cpython-313.pyc
│   │           │   │   │   ├── __version__.cpython-313.pyc
│   │           │   │   │   ├── _isocbind.cpython-313.pyc
│   │           │   │   │   ├── _src_pyf.cpython-313.pyc
│   │           │   │   │   ├── auxfuncs.cpython-313.pyc
│   │           │   │   │   ├── capi_maps.cpython-313.pyc
│   │           │   │   │   ├── cb_rules.cpython-313.pyc
│   │           │   │   │   ├── cfuncs.cpython-313.pyc
│   │           │   │   │   ├── common_rules.cpython-313.pyc
│   │           │   │   │   ├── crackfortran.cpython-313.pyc
│   │           │   │   │   ├── diagnose.cpython-313.pyc
│   │           │   │   │   ├── f2py2e.cpython-313.pyc
│   │           │   │   │   ├── f90mod_rules.cpython-313.pyc
│   │           │   │   │   ├── func2subr.cpython-313.pyc
│   │           │   │   │   ├── rules.cpython-313.pyc
│   │           │   │   │   ├── symbolic.cpython-313.pyc
│   │           │   │   │   └── use_rules.cpython-313.pyc
│   │           │   │   ├── _backends
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── _backend.cpython-313.pyc
│   │           │   │   │   │   ├── _distutils.cpython-313.pyc
│   │           │   │   │   │   └── _meson.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __init__.pyi
│   │           │   │   │   ├── _backend.py
│   │           │   │   │   ├── _backend.pyi
│   │           │   │   │   ├── _distutils.py
│   │           │   │   │   ├── _distutils.pyi
│   │           │   │   │   ├── _meson.py
│   │           │   │   │   ├── _meson.pyi
│   │           │   │   │   └── meson.build.template
│   │           │   │   ├── src
│   │           │   │   │   ├── fortranobject.c
│   │           │   │   │   └── fortranobject.h
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── test_abstract_interface.cpython-313.pyc
│   │           │   │   │   │   ├── test_array_from_pyobj.cpython-313.pyc
│   │           │   │   │   │   ├── test_assumed_shape.cpython-313.pyc
│   │           │   │   │   │   ├── test_block_docstring.cpython-313.pyc
│   │           │   │   │   │   ├── test_callback.cpython-313.pyc
│   │           │   │   │   │   ├── test_character.cpython-313.pyc
│   │           │   │   │   │   ├── test_common.cpython-313.pyc
│   │           │   │   │   │   ├── test_crackfortran.cpython-313.pyc
│   │           │   │   │   │   ├── test_data.cpython-313.pyc
│   │           │   │   │   │   ├── test_docs.cpython-313.pyc
│   │           │   │   │   │   ├── test_f2cmap.cpython-313.pyc
│   │           │   │   │   │   ├── test_f2py2e.cpython-313.pyc
│   │           │   │   │   │   ├── test_isoc.cpython-313.pyc
│   │           │   │   │   │   ├── test_kind.cpython-313.pyc
│   │           │   │   │   │   ├── test_mixed.cpython-313.pyc
│   │           │   │   │   │   ├── test_modules.cpython-313.pyc
│   │           │   │   │   │   ├── test_parameter.cpython-313.pyc
│   │           │   │   │   │   ├── test_pyf_src.cpython-313.pyc
│   │           │   │   │   │   ├── test_quoted_character.cpython-313.pyc
│   │           │   │   │   │   ├── test_regression.cpython-313.pyc
│   │           │   │   │   │   ├── test_return_character.cpython-313.pyc
│   │           │   │   │   │   ├── test_return_complex.cpython-313.pyc
│   │           │   │   │   │   ├── test_return_integer.cpython-313.pyc
│   │           │   │   │   │   ├── test_return_logical.cpython-313.pyc
│   │           │   │   │   │   ├── test_return_real.cpython-313.pyc
│   │           │   │   │   │   ├── test_routines.cpython-313.pyc
│   │           │   │   │   │   ├── test_semicolon_split.cpython-313.pyc
│   │           │   │   │   │   ├── test_size.cpython-313.pyc
│   │           │   │   │   │   ├── test_string.cpython-313.pyc
│   │           │   │   │   │   ├── test_symbolic.cpython-313.pyc
│   │           │   │   │   │   ├── test_value_attrspec.cpython-313.pyc
│   │           │   │   │   │   └── util.cpython-313.pyc
│   │           │   │   │   ├── src
│   │           │   │   │   │   ├── abstract_interface
│   │           │   │   │   │   │   ├── foo.f90
│   │           │   │   │   │   │   └── gh18403_mod.f90
│   │           │   │   │   │   ├── array_from_pyobj
│   │           │   │   │   │   │   └── wrapmodule.c
│   │           │   │   │   │   ├── assumed_shape
│   │           │   │   │   │   │   ├── foo_free.f90
│   │           │   │   │   │   │   ├── foo_mod.f90
│   │           │   │   │   │   │   ├── foo_use.f90
│   │           │   │   │   │   │   └── precision.f90
│   │           │   │   │   │   ├── block_docstring
│   │           │   │   │   │   │   └── foo.f
│   │           │   │   │   │   ├── callback
│   │           │   │   │   │   │   ├── foo.f
│   │           │   │   │   │   │   ├── gh17797.f90
│   │           │   │   │   │   │   ├── gh18335.f90
│   │           │   │   │   │   │   ├── gh25211.f
│   │           │   │   │   │   │   ├── gh25211.pyf
│   │           │   │   │   │   │   └── gh26681.f90
│   │           │   │   │   │   ├── cli
│   │           │   │   │   │   │   ├── gh_22819.pyf
│   │           │   │   │   │   │   ├── hi77.f
│   │           │   │   │   │   │   └── hiworld.f90
│   │           │   │   │   │   ├── common
│   │           │   │   │   │   │   ├── block.f
│   │           │   │   │   │   │   └── gh19161.f90
│   │           │   │   │   │   ├── crackfortran
│   │           │   │   │   │   │   ├── accesstype.f90
│   │           │   │   │   │   │   ├── common_with_division.f
│   │           │   │   │   │   │   ├── data_common.f
│   │           │   │   │   │   │   ├── data_multiplier.f
│   │           │   │   │   │   │   ├── data_stmts.f90
│   │           │   │   │   │   │   ├── data_with_comments.f
│   │           │   │   │   │   │   ├── foo_deps.f90
│   │           │   │   │   │   │   ├── gh15035.f
│   │           │   │   │   │   │   ├── gh17859.f
│   │           │   │   │   │   │   ├── gh22648.pyf
│   │           │   │   │   │   │   ├── gh23533.f
│   │           │   │   │   │   │   ├── gh23598.f90
│   │           │   │   │   │   │   ├── gh23598Warn.f90
│   │           │   │   │   │   │   ├── gh23879.f90
│   │           │   │   │   │   │   ├── gh27697.f90
│   │           │   │   │   │   │   ├── gh2848.f90
│   │           │   │   │   │   │   ├── operators.f90
│   │           │   │   │   │   │   ├── privatemod.f90
│   │           │   │   │   │   │   ├── publicmod.f90
│   │           │   │   │   │   │   ├── pubprivmod.f90
│   │           │   │   │   │   │   └── unicode_comment.f90
│   │           │   │   │   │   ├── f2cmap
│   │           │   │   │   │   │   └── isoFortranEnvMap.f90
│   │           │   │   │   │   ├── isocintrin
│   │           │   │   │   │   │   └── isoCtests.f90
│   │           │   │   │   │   ├── kind
│   │           │   │   │   │   │   └── foo.f90
│   │           │   │   │   │   ├── mixed
│   │           │   │   │   │   │   ├── foo_fixed.f90
│   │           │   │   │   │   │   ├── foo_free.f90
│   │           │   │   │   │   │   └── foo.f
│   │           │   │   │   │   ├── modules
│   │           │   │   │   │   │   ├── gh25337
│   │           │   │   │   │   │   │   ├── data.f90
│   │           │   │   │   │   │   │   └── use_data.f90
│   │           │   │   │   │   │   ├── gh26920
│   │           │   │   │   │   │   │   ├── two_mods_with_no_public_entities.f90
│   │           │   │   │   │   │   │   └── two_mods_with_one_public_routine.f90
│   │           │   │   │   │   │   ├── module_data_docstring.f90
│   │           │   │   │   │   │   └── use_modules.f90
│   │           │   │   │   │   ├── negative_bounds
│   │           │   │   │   │   │   └── issue_20853.f90
│   │           │   │   │   │   ├── parameter
│   │           │   │   │   │   │   ├── constant_array.f90
│   │           │   │   │   │   │   ├── constant_both.f90
│   │           │   │   │   │   │   ├── constant_compound.f90
│   │           │   │   │   │   │   ├── constant_integer.f90
│   │           │   │   │   │   │   ├── constant_non_compound.f90
│   │           │   │   │   │   │   └── constant_real.f90
│   │           │   │   │   │   ├── quoted_character
│   │           │   │   │   │   │   └── foo.f
│   │           │   │   │   │   ├── regression
│   │           │   │   │   │   │   ├── AB.inc
│   │           │   │   │   │   │   ├── assignOnlyModule.f90
│   │           │   │   │   │   │   ├── datonly.f90
│   │           │   │   │   │   │   ├── f77comments.f
│   │           │   │   │   │   │   ├── f77fixedform.f95
│   │           │   │   │   │   │   ├── f90continuation.f90
│   │           │   │   │   │   │   ├── incfile.f90
│   │           │   │   │   │   │   ├── inout.f90
│   │           │   │   │   │   │   ├── lower_f2py_fortran.f90
│   │           │   │   │   │   │   └── mod_derived_types.f90
│   │           │   │   │   │   ├── return_character
│   │           │   │   │   │   │   ├── foo77.f
│   │           │   │   │   │   │   └── foo90.f90
│   │           │   │   │   │   ├── return_complex
│   │           │   │   │   │   │   ├── foo77.f
│   │           │   │   │   │   │   └── foo90.f90
│   │           │   │   │   │   ├── return_integer
│   │           │   │   │   │   │   ├── foo77.f
│   │           │   │   │   │   │   └── foo90.f90
│   │           │   │   │   │   ├── return_logical
│   │           │   │   │   │   │   ├── foo77.f
│   │           │   │   │   │   │   └── foo90.f90
│   │           │   │   │   │   ├── return_real
│   │           │   │   │   │   │   ├── foo77.f
│   │           │   │   │   │   │   └── foo90.f90
│   │           │   │   │   │   ├── routines
│   │           │   │   │   │   │   ├── funcfortranname.f
│   │           │   │   │   │   │   ├── funcfortranname.pyf
│   │           │   │   │   │   │   ├── subrout.f
│   │           │   │   │   │   │   └── subrout.pyf
│   │           │   │   │   │   ├── size
│   │           │   │   │   │   │   └── foo.f90
│   │           │   │   │   │   ├── string
│   │           │   │   │   │   │   ├── char.f90
│   │           │   │   │   │   │   ├── fixed_string.f90
│   │           │   │   │   │   │   ├── gh24008.f
│   │           │   │   │   │   │   ├── gh24662.f90
│   │           │   │   │   │   │   ├── gh25286_bc.pyf
│   │           │   │   │   │   │   ├── gh25286.f90
│   │           │   │   │   │   │   ├── gh25286.pyf
│   │           │   │   │   │   │   ├── scalar_string.f90
│   │           │   │   │   │   │   └── string.f
│   │           │   │   │   │   └── value_attrspec
│   │           │   │   │   │       └── gh21665.f90
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_abstract_interface.py
│   │           │   │   │   ├── test_array_from_pyobj.py
│   │           │   │   │   ├── test_assumed_shape.py
│   │           │   │   │   ├── test_block_docstring.py
│   │           │   │   │   ├── test_callback.py
│   │           │   │   │   ├── test_character.py
│   │           │   │   │   ├── test_common.py
│   │           │   │   │   ├── test_crackfortran.py
│   │           │   │   │   ├── test_data.py
│   │           │   │   │   ├── test_docs.py
│   │           │   │   │   ├── test_f2cmap.py
│   │           │   │   │   ├── test_f2py2e.py
│   │           │   │   │   ├── test_isoc.py
│   │           │   │   │   ├── test_kind.py
│   │           │   │   │   ├── test_mixed.py
│   │           │   │   │   ├── test_modules.py
│   │           │   │   │   ├── test_parameter.py
│   │           │   │   │   ├── test_pyf_src.py
│   │           │   │   │   ├── test_quoted_character.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test_return_character.py
│   │           │   │   │   ├── test_return_complex.py
│   │           │   │   │   ├── test_return_integer.py
│   │           │   │   │   ├── test_return_logical.py
│   │           │   │   │   ├── test_return_real.py
│   │           │   │   │   ├── test_routines.py
│   │           │   │   │   ├── test_semicolon_split.py
│   │           │   │   │   ├── test_size.py
│   │           │   │   │   ├── test_string.py
│   │           │   │   │   ├── test_symbolic.py
│   │           │   │   │   ├── test_value_attrspec.py
│   │           │   │   │   └── util.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── __main__.py
│   │           │   │   ├── __version__.py
│   │           │   │   ├── __version__.pyi
│   │           │   │   ├── _isocbind.py
│   │           │   │   ├── _isocbind.pyi
│   │           │   │   ├── _src_pyf.py
│   │           │   │   ├── _src_pyf.pyi
│   │           │   │   ├── auxfuncs.py
│   │           │   │   ├── auxfuncs.pyi
│   │           │   │   ├── capi_maps.py
│   │           │   │   ├── capi_maps.pyi
│   │           │   │   ├── cb_rules.py
│   │           │   │   ├── cb_rules.pyi
│   │           │   │   ├── cfuncs.py
│   │           │   │   ├── cfuncs.pyi
│   │           │   │   ├── common_rules.py
│   │           │   │   ├── common_rules.pyi
│   │           │   │   ├── crackfortran.py
│   │           │   │   ├── crackfortran.pyi
│   │           │   │   ├── diagnose.py
│   │           │   │   ├── diagnose.pyi
│   │           │   │   ├── f2py2e.py
│   │           │   │   ├── f2py2e.pyi
│   │           │   │   ├── f90mod_rules.py
│   │           │   │   ├── f90mod_rules.pyi
│   │           │   │   ├── func2subr.py
│   │           │   │   ├── func2subr.pyi
│   │           │   │   ├── rules.py
│   │           │   │   ├── rules.pyi
│   │           │   │   ├── setup.cfg
│   │           │   │   ├── symbolic.py
│   │           │   │   ├── symbolic.pyi
│   │           │   │   ├── use_rules.py
│   │           │   │   └── use_rules.pyi
│   │           │   ├── fft
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _helper.cpython-313.pyc
│   │           │   │   │   └── _pocketfft.cpython-313.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── test_helper.cpython-313.pyc
│   │           │   │   │   │   └── test_pocketfft.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_helper.py
│   │           │   │   │   └── test_pocketfft.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _helper.py
│   │           │   │   ├── _helper.pyi
│   │           │   │   ├── _pocketfft_umath.cpython-313-darwin.so
│   │           │   │   ├── _pocketfft.py
│   │           │   │   └── _pocketfft.pyi
│   │           │   ├── lib
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _array_utils_impl.cpython-313.pyc
│   │           │   │   │   ├── _arraypad_impl.cpython-313.pyc
│   │           │   │   │   ├── _arraysetops_impl.cpython-313.pyc
│   │           │   │   │   ├── _arrayterator_impl.cpython-313.pyc
│   │           │   │   │   ├── _datasource.cpython-313.pyc
│   │           │   │   │   ├── _format_impl.cpython-313.pyc
│   │           │   │   │   ├── _function_base_impl.cpython-313.pyc
│   │           │   │   │   ├── _histograms_impl.cpython-313.pyc
│   │           │   │   │   ├── _index_tricks_impl.cpython-313.pyc
│   │           │   │   │   ├── _iotools.cpython-313.pyc
│   │           │   │   │   ├── _nanfunctions_impl.cpython-313.pyc
│   │           │   │   │   ├── _npyio_impl.cpython-313.pyc
│   │           │   │   │   ├── _polynomial_impl.cpython-313.pyc
│   │           │   │   │   ├── _scimath_impl.cpython-313.pyc
│   │           │   │   │   ├── _shape_base_impl.cpython-313.pyc
│   │           │   │   │   ├── _stride_tricks_impl.cpython-313.pyc
│   │           │   │   │   ├── _twodim_base_impl.cpython-313.pyc
│   │           │   │   │   ├── _type_check_impl.cpython-313.pyc
│   │           │   │   │   ├── _ufunclike_impl.cpython-313.pyc
│   │           │   │   │   ├── _user_array_impl.cpython-313.pyc
│   │           │   │   │   ├── _utils_impl.cpython-313.pyc
│   │           │   │   │   ├── _version.cpython-313.pyc
│   │           │   │   │   ├── array_utils.cpython-313.pyc
│   │           │   │   │   ├── format.cpython-313.pyc
│   │           │   │   │   ├── introspect.cpython-313.pyc
│   │           │   │   │   ├── mixins.cpython-313.pyc
│   │           │   │   │   ├── npyio.cpython-313.pyc
│   │           │   │   │   ├── recfunctions.cpython-313.pyc
│   │           │   │   │   ├── scimath.cpython-313.pyc
│   │           │   │   │   ├── stride_tricks.cpython-313.pyc
│   │           │   │   │   └── user_array.cpython-313.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── test__datasource.cpython-313.pyc
│   │           │   │   │   │   ├── test__iotools.cpython-313.pyc
│   │           │   │   │   │   ├── test__version.cpython-313.pyc
│   │           │   │   │   │   ├── test_array_utils.cpython-313.pyc
│   │           │   │   │   │   ├── test_arraypad.cpython-313.pyc
│   │           │   │   │   │   ├── test_arraysetops.cpython-313.pyc
│   │           │   │   │   │   ├── test_arrayterator.cpython-313.pyc
│   │           │   │   │   │   ├── test_format.cpython-313.pyc
│   │           │   │   │   │   ├── test_function_base.cpython-313.pyc
│   │           │   │   │   │   ├── test_histograms.cpython-313.pyc
│   │           │   │   │   │   ├── test_index_tricks.cpython-313.pyc
│   │           │   │   │   │   ├── test_io.cpython-313.pyc
│   │           │   │   │   │   ├── test_loadtxt.cpython-313.pyc
│   │           │   │   │   │   ├── test_mixins.cpython-313.pyc
│   │           │   │   │   │   ├── test_nanfunctions.cpython-313.pyc
│   │           │   │   │   │   ├── test_packbits.cpython-313.pyc
│   │           │   │   │   │   ├── test_polynomial.cpython-313.pyc
│   │           │   │   │   │   ├── test_recfunctions.cpython-313.pyc
│   │           │   │   │   │   ├── test_regression.cpython-313.pyc
│   │           │   │   │   │   ├── test_shape_base.cpython-313.pyc
│   │           │   │   │   │   ├── test_stride_tricks.cpython-313.pyc
│   │           │   │   │   │   ├── test_twodim_base.cpython-313.pyc
│   │           │   │   │   │   ├── test_type_check.cpython-313.pyc
│   │           │   │   │   │   ├── test_ufunclike.cpython-313.pyc
│   │           │   │   │   │   └── test_utils.cpython-313.pyc
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── py2-np0-objarr.npy
│   │           │   │   │   │   ├── py2-objarr.npy
│   │           │   │   │   │   ├── py2-objarr.npz
│   │           │   │   │   │   ├── py3-objarr.npy
│   │           │   │   │   │   ├── py3-objarr.npz
│   │           │   │   │   │   ├── python3.npy
│   │           │   │   │   │   └── win64python2.npy
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test__datasource.py
│   │           │   │   │   ├── test__iotools.py
│   │           │   │   │   ├── test__version.py
│   │           │   │   │   ├── test_array_utils.py
│   │           │   │   │   ├── test_arraypad.py
│   │           │   │   │   ├── test_arraysetops.py
│   │           │   │   │   ├── test_arrayterator.py
│   │           │   │   │   ├── test_format.py
│   │           │   │   │   ├── test_function_base.py
│   │           │   │   │   ├── test_histograms.py
│   │           │   │   │   ├── test_index_tricks.py
│   │           │   │   │   ├── test_io.py
│   │           │   │   │   ├── test_loadtxt.py
│   │           │   │   │   ├── test_mixins.py
│   │           │   │   │   ├── test_nanfunctions.py
│   │           │   │   │   ├── test_packbits.py
│   │           │   │   │   ├── test_polynomial.py
│   │           │   │   │   ├── test_recfunctions.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test_shape_base.py
│   │           │   │   │   ├── test_stride_tricks.py
│   │           │   │   │   ├── test_twodim_base.py
│   │           │   │   │   ├── test_type_check.py
│   │           │   │   │   ├── test_ufunclike.py
│   │           │   │   │   └── test_utils.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _array_utils_impl.py
│   │           │   │   ├── _array_utils_impl.pyi
│   │           │   │   ├── _arraypad_impl.py
│   │           │   │   ├── _arraypad_impl.pyi
│   │           │   │   ├── _arraysetops_impl.py
│   │           │   │   ├── _arraysetops_impl.pyi
│   │           │   │   ├── _arrayterator_impl.py
│   │           │   │   ├── _arrayterator_impl.pyi
│   │           │   │   ├── _datasource.py
│   │           │   │   ├── _datasource.pyi
│   │           │   │   ├── _format_impl.py
│   │           │   │   ├── _format_impl.pyi
│   │           │   │   ├── _function_base_impl.py
│   │           │   │   ├── _function_base_impl.pyi
│   │           │   │   ├── _histograms_impl.py
│   │           │   │   ├── _histograms_impl.pyi
│   │           │   │   ├── _index_tricks_impl.py
│   │           │   │   ├── _index_tricks_impl.pyi
│   │           │   │   ├── _iotools.py
│   │           │   │   ├── _iotools.pyi
│   │           │   │   ├── _nanfunctions_impl.py
│   │           │   │   ├── _nanfunctions_impl.pyi
│   │           │   │   ├── _npyio_impl.py
│   │           │   │   ├── _npyio_impl.pyi
│   │           │   │   ├── _polynomial_impl.py
│   │           │   │   ├── _polynomial_impl.pyi
│   │           │   │   ├── _scimath_impl.py
│   │           │   │   ├── _scimath_impl.pyi
│   │           │   │   ├── _shape_base_impl.py
│   │           │   │   ├── _shape_base_impl.pyi
│   │           │   │   ├── _stride_tricks_impl.py
│   │           │   │   ├── _stride_tricks_impl.pyi
│   │           │   │   ├── _twodim_base_impl.py
│   │           │   │   ├── _twodim_base_impl.pyi
│   │           │   │   ├── _type_check_impl.py
│   │           │   │   ├── _type_check_impl.pyi
│   │           │   │   ├── _ufunclike_impl.py
│   │           │   │   ├── _ufunclike_impl.pyi
│   │           │   │   ├── _user_array_impl.py
│   │           │   │   ├── _user_array_impl.pyi
│   │           │   │   ├── _utils_impl.py
│   │           │   │   ├── _utils_impl.pyi
│   │           │   │   ├── _version.py
│   │           │   │   ├── _version.pyi
│   │           │   │   ├── array_utils.py
│   │           │   │   ├── array_utils.pyi
│   │           │   │   ├── format.py
│   │           │   │   ├── format.pyi
│   │           │   │   ├── introspect.py
│   │           │   │   ├── introspect.pyi
│   │           │   │   ├── mixins.py
│   │           │   │   ├── mixins.pyi
│   │           │   │   ├── npyio.py
│   │           │   │   ├── npyio.pyi
│   │           │   │   ├── recfunctions.py
│   │           │   │   ├── recfunctions.pyi
│   │           │   │   ├── scimath.py
│   │           │   │   ├── scimath.pyi
│   │           │   │   ├── stride_tricks.py
│   │           │   │   ├── stride_tricks.pyi
│   │           │   │   ├── user_array.py
│   │           │   │   └── user_array.pyi
│   │           │   ├── linalg
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   └── _linalg.cpython-313.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── test_deprecations.cpython-313.pyc
│   │           │   │   │   │   ├── test_linalg.cpython-313.pyc
│   │           │   │   │   │   └── test_regression.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_deprecations.py
│   │           │   │   │   ├── test_linalg.py
│   │           │   │   │   └── test_regression.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _linalg.py
│   │           │   │   ├── _linalg.pyi
│   │           │   │   ├── _umath_linalg.cpython-313-darwin.so
│   │           │   │   ├── _umath_linalg.pyi
│   │           │   │   ├── lapack_lite.cpython-313-darwin.so
│   │           │   │   └── lapack_lite.pyi
│   │           │   ├── ma
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── core.cpython-313.pyc
│   │           │   │   │   ├── extras.cpython-313.pyc
│   │           │   │   │   ├── mrecords.cpython-313.pyc
│   │           │   │   │   └── testutils.cpython-313.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── test_arrayobject.cpython-313.pyc
│   │           │   │   │   │   ├── test_core.cpython-313.pyc
│   │           │   │   │   │   ├── test_deprecations.cpython-313.pyc
│   │           │   │   │   │   ├── test_extras.cpython-313.pyc
│   │           │   │   │   │   ├── test_mrecords.cpython-313.pyc
│   │           │   │   │   │   ├── test_old_ma.cpython-313.pyc
│   │           │   │   │   │   ├── test_regression.cpython-313.pyc
│   │           │   │   │   │   └── test_subclassing.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_arrayobject.py
│   │           │   │   │   ├── test_core.py
│   │           │   │   │   ├── test_deprecations.py
│   │           │   │   │   ├── test_extras.py
│   │           │   │   │   ├── test_mrecords.py
│   │           │   │   │   ├── test_old_ma.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   └── test_subclassing.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── API_CHANGES.txt
│   │           │   │   ├── core.py
│   │           │   │   ├── core.pyi
│   │           │   │   ├── extras.py
│   │           │   │   ├── extras.pyi
│   │           │   │   ├── LICENSE
│   │           │   │   ├── mrecords.py
│   │           │   │   ├── mrecords.pyi
│   │           │   │   ├── README.rst
│   │           │   │   ├── testutils.py
│   │           │   │   └── testutils.pyi
│   │           │   ├── matrixlib
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   └── defmatrix.cpython-313.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── test_defmatrix.cpython-313.pyc
│   │           │   │   │   │   ├── test_interaction.cpython-313.pyc
│   │           │   │   │   │   ├── test_masked_matrix.cpython-313.pyc
│   │           │   │   │   │   ├── test_matrix_linalg.cpython-313.pyc
│   │           │   │   │   │   ├── test_multiarray.cpython-313.pyc
│   │           │   │   │   │   ├── test_numeric.cpython-313.pyc
│   │           │   │   │   │   └── test_regression.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_defmatrix.py
│   │           │   │   │   ├── test_interaction.py
│   │           │   │   │   ├── test_masked_matrix.py
│   │           │   │   │   ├── test_matrix_linalg.py
│   │           │   │   │   ├── test_multiarray.py
│   │           │   │   │   ├── test_numeric.py
│   │           │   │   │   └── test_regression.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── defmatrix.py
│   │           │   │   └── defmatrix.pyi
│   │           │   ├── polynomial
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _polybase.cpython-313.pyc
│   │           │   │   │   ├── chebyshev.cpython-313.pyc
│   │           │   │   │   ├── hermite_e.cpython-313.pyc
│   │           │   │   │   ├── hermite.cpython-313.pyc
│   │           │   │   │   ├── laguerre.cpython-313.pyc
│   │           │   │   │   ├── legendre.cpython-313.pyc
│   │           │   │   │   ├── polynomial.cpython-313.pyc
│   │           │   │   │   └── polyutils.cpython-313.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── test_chebyshev.cpython-313.pyc
│   │           │   │   │   │   ├── test_classes.cpython-313.pyc
│   │           │   │   │   │   ├── test_hermite_e.cpython-313.pyc
│   │           │   │   │   │   ├── test_hermite.cpython-313.pyc
│   │           │   │   │   │   ├── test_laguerre.cpython-313.pyc
│   │           │   │   │   │   ├── test_legendre.cpython-313.pyc
│   │           │   │   │   │   ├── test_polynomial.cpython-313.pyc
│   │           │   │   │   │   ├── test_polyutils.cpython-313.pyc
│   │           │   │   │   │   ├── test_printing.cpython-313.pyc
│   │           │   │   │   │   └── test_symbol.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_chebyshev.py
│   │           │   │   │   ├── test_classes.py
│   │           │   │   │   ├── test_hermite_e.py
│   │           │   │   │   ├── test_hermite.py
│   │           │   │   │   ├── test_laguerre.py
│   │           │   │   │   ├── test_legendre.py
│   │           │   │   │   ├── test_polynomial.py
│   │           │   │   │   ├── test_polyutils.py
│   │           │   │   │   ├── test_printing.py
│   │           │   │   │   └── test_symbol.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _polybase.py
│   │           │   │   ├── _polybase.pyi
│   │           │   │   ├── _polytypes.pyi
│   │           │   │   ├── chebyshev.py
│   │           │   │   ├── chebyshev.pyi
│   │           │   │   ├── hermite_e.py
│   │           │   │   ├── hermite_e.pyi
│   │           │   │   ├── hermite.py
│   │           │   │   ├── hermite.pyi
│   │           │   │   ├── laguerre.py
│   │           │   │   ├── laguerre.pyi
│   │           │   │   ├── legendre.py
│   │           │   │   ├── legendre.pyi
│   │           │   │   ├── polynomial.py
│   │           │   │   ├── polynomial.pyi
│   │           │   │   ├── polyutils.py
│   │           │   │   └── polyutils.pyi
│   │           │   ├── random
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   └── _pickle.cpython-313.pyc
│   │           │   │   ├── _examples
│   │           │   │   │   ├── cffi
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── extending.cpython-313.pyc
│   │           │   │   │   │   │   └── parse.cpython-313.pyc
│   │           │   │   │   │   ├── extending.py
│   │           │   │   │   │   └── parse.py
│   │           │   │   │   ├── cython
│   │           │   │   │   │   ├── extending_distributions.pyx
│   │           │   │   │   │   ├── extending.pyx
│   │           │   │   │   │   └── meson.build
│   │           │   │   │   └── numba
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── extending_distributions.cpython-313.pyc
│   │           │   │   │       │   └── extending.cpython-313.pyc
│   │           │   │   │       ├── extending_distributions.py
│   │           │   │   │       └── extending.py
│   │           │   │   ├── lib
│   │           │   │   │   └── libnpyrandom.a
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── test_direct.cpython-313.pyc
│   │           │   │   │   │   ├── test_extending.cpython-313.pyc
│   │           │   │   │   │   ├── test_generator_mt19937_regressions.cpython-313.pyc
│   │           │   │   │   │   ├── test_generator_mt19937.cpython-313.pyc
│   │           │   │   │   │   ├── test_random.cpython-313.pyc
│   │           │   │   │   │   ├── test_randomstate_regression.cpython-313.pyc
│   │           │   │   │   │   ├── test_randomstate.cpython-313.pyc
│   │           │   │   │   │   ├── test_regression.cpython-313.pyc
│   │           │   │   │   │   ├── test_seed_sequence.cpython-313.pyc
│   │           │   │   │   │   └── test_smoke.cpython-313.pyc
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   └── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── generator_pcg64_np121.pkl.gz
│   │           │   │   │   │   ├── generator_pcg64_np126.pkl.gz
│   │           │   │   │   │   ├── mt19937-testset-1.csv
│   │           │   │   │   │   ├── mt19937-testset-2.csv
│   │           │   │   │   │   ├── pcg64-testset-1.csv
│   │           │   │   │   │   ├── pcg64-testset-2.csv
│   │           │   │   │   │   ├── pcg64dxsm-testset-1.csv
│   │           │   │   │   │   ├── pcg64dxsm-testset-2.csv
│   │           │   │   │   │   ├── philox-testset-1.csv
│   │           │   │   │   │   ├── philox-testset-2.csv
│   │           │   │   │   │   ├── sfc64_np126.pkl.gz
│   │           │   │   │   │   ├── sfc64-testset-1.csv
│   │           │   │   │   │   └── sfc64-testset-2.csv
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_direct.py
│   │           │   │   │   ├── test_extending.py
│   │           │   │   │   ├── test_generator_mt19937_regressions.py
│   │           │   │   │   ├── test_generator_mt19937.py
│   │           │   │   │   ├── test_random.py
│   │           │   │   │   ├── test_randomstate_regression.py
│   │           │   │   │   ├── test_randomstate.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test_seed_sequence.py
│   │           │   │   │   └── test_smoke.py
│   │           │   │   ├── __init__.pxd
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _bounded_integers.cpython-313-darwin.so
│   │           │   │   ├── _bounded_integers.pxd
│   │           │   │   ├── _bounded_integers.pyi
│   │           │   │   ├── _common.cpython-313-darwin.so
│   │           │   │   ├── _common.pxd
│   │           │   │   ├── _common.pyi
│   │           │   │   ├── _generator.cpython-313-darwin.so
│   │           │   │   ├── _generator.pyi
│   │           │   │   ├── _mt19937.cpython-313-darwin.so
│   │           │   │   ├── _mt19937.pyi
│   │           │   │   ├── _pcg64.cpython-313-darwin.so
│   │           │   │   ├── _pcg64.pyi
│   │           │   │   ├── _philox.cpython-313-darwin.so
│   │           │   │   ├── _philox.pyi
│   │           │   │   ├── _pickle.py
│   │           │   │   ├── _pickle.pyi
│   │           │   │   ├── _sfc64.cpython-313-darwin.so
│   │           │   │   ├── _sfc64.pyi
│   │           │   │   ├── bit_generator.cpython-313-darwin.so
│   │           │   │   ├── bit_generator.pxd
│   │           │   │   ├── bit_generator.pyi
│   │           │   │   ├── c_distributions.pxd
│   │           │   │   ├── LICENSE.md
│   │           │   │   ├── mtrand.cpython-313-darwin.so
│   │           │   │   └── mtrand.pyi
│   │           │   ├── rec
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   └── __init__.pyi
│   │           │   ├── strings
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   └── __init__.pyi
│   │           │   ├── testing
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── overrides.cpython-313.pyc
│   │           │   │   │   └── print_coercion_tables.cpython-313.pyc
│   │           │   │   ├── _private
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── extbuild.cpython-313.pyc
│   │           │   │   │   │   └── utils.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __init__.pyi
│   │           │   │   │   ├── extbuild.py
│   │           │   │   │   ├── extbuild.pyi
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── utils.pyi
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   └── test_utils.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── test_utils.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── overrides.py
│   │           │   │   ├── overrides.pyi
│   │           │   │   ├── print_coercion_tables.py
│   │           │   │   └── print_coercion_tables.pyi
│   │           │   ├── tests
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── test__all__.cpython-313.pyc
│   │           │   │   │   ├── test_configtool.cpython-313.pyc
│   │           │   │   │   ├── test_ctypeslib.cpython-313.pyc
│   │           │   │   │   ├── test_lazyloading.cpython-313.pyc
│   │           │   │   │   ├── test_matlib.cpython-313.pyc
│   │           │   │   │   ├── test_numpy_config.cpython-313.pyc
│   │           │   │   │   ├── test_numpy_version.cpython-313.pyc
│   │           │   │   │   ├── test_public_api.cpython-313.pyc
│   │           │   │   │   ├── test_reloading.cpython-313.pyc
│   │           │   │   │   ├── test_scripts.cpython-313.pyc
│   │           │   │   │   └── test_warnings.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── test__all__.py
│   │           │   │   ├── test_configtool.py
│   │           │   │   ├── test_ctypeslib.py
│   │           │   │   ├── test_lazyloading.py
│   │           │   │   ├── test_matlib.py
│   │           │   │   ├── test_numpy_config.py
│   │           │   │   ├── test_numpy_version.py
│   │           │   │   ├── test_public_api.py
│   │           │   │   ├── test_reloading.py
│   │           │   │   ├── test_scripts.py
│   │           │   │   └── test_warnings.py
│   │           │   ├── typing
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   └── mypy_plugin.cpython-313.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── test_isfile.cpython-313.pyc
│   │           │   │   │   │   ├── test_runtime.cpython-313.pyc
│   │           │   │   │   │   └── test_typing.cpython-313.pyc
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── fail
│   │           │   │   │   │   │   ├── arithmetic.pyi
│   │           │   │   │   │   │   ├── array_constructors.pyi
│   │           │   │   │   │   │   ├── array_like.pyi
│   │           │   │   │   │   │   ├── array_pad.pyi
│   │           │   │   │   │   │   ├── arrayprint.pyi
│   │           │   │   │   │   │   ├── arrayterator.pyi
│   │           │   │   │   │   │   ├── bitwise_ops.pyi
│   │           │   │   │   │   │   ├── char.pyi
│   │           │   │   │   │   │   ├── chararray.pyi
│   │           │   │   │   │   │   ├── comparisons.pyi
│   │           │   │   │   │   │   ├── constants.pyi
│   │           │   │   │   │   │   ├── datasource.pyi
│   │           │   │   │   │   │   ├── dtype.pyi
│   │           │   │   │   │   │   ├── einsumfunc.pyi
│   │           │   │   │   │   │   ├── flatiter.pyi
│   │           │   │   │   │   │   ├── fromnumeric.pyi
│   │           │   │   │   │   │   ├── histograms.pyi
│   │           │   │   │   │   │   ├── index_tricks.pyi
│   │           │   │   │   │   │   ├── lib_function_base.pyi
│   │           │   │   │   │   │   ├── lib_polynomial.pyi
│   │           │   │   │   │   │   ├── lib_utils.pyi
│   │           │   │   │   │   │   ├── lib_version.pyi
│   │           │   │   │   │   │   ├── linalg.pyi
│   │           │   │   │   │   │   ├── ma.pyi
│   │           │   │   │   │   │   ├── memmap.pyi
│   │           │   │   │   │   │   ├── modules.pyi
│   │           │   │   │   │   │   ├── multiarray.pyi
│   │           │   │   │   │   │   ├── ndarray_misc.pyi
│   │           │   │   │   │   │   ├── ndarray.pyi
│   │           │   │   │   │   │   ├── nditer.pyi
│   │           │   │   │   │   │   ├── nested_sequence.pyi
│   │           │   │   │   │   │   ├── npyio.pyi
│   │           │   │   │   │   │   ├── numerictypes.pyi
│   │           │   │   │   │   │   ├── random.pyi
│   │           │   │   │   │   │   ├── rec.pyi
│   │           │   │   │   │   │   ├── scalars.pyi
│   │           │   │   │   │   │   ├── shape_base.pyi
│   │           │   │   │   │   │   ├── shape.pyi
│   │           │   │   │   │   │   ├── stride_tricks.pyi
│   │           │   │   │   │   │   ├── strings.pyi
│   │           │   │   │   │   │   ├── testing.pyi
│   │           │   │   │   │   │   ├── twodim_base.pyi
│   │           │   │   │   │   │   ├── type_check.pyi
│   │           │   │   │   │   │   ├── ufunc_config.pyi
│   │           │   │   │   │   │   ├── ufunclike.pyi
│   │           │   │   │   │   │   ├── ufuncs.pyi
│   │           │   │   │   │   │   └── warnings_and_errors.pyi
│   │           │   │   │   │   ├── misc
│   │           │   │   │   │   │   └── extended_precision.pyi
│   │           │   │   │   │   ├── pass
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── arithmetic.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── array_constructors.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── array_like.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── arrayprint.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── arrayterator.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── bitwise_ops.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── comparisons.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── dtype.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── einsumfunc.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── flatiter.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── fromnumeric.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── index_tricks.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── lib_user_array.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── lib_utils.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── lib_version.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── literal.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── ma.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── mod.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── modules.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── multiarray.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── ndarray_conversion.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── ndarray_misc.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── ndarray_shape_manipulation.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── nditer.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── numeric.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── numerictypes.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── random.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── recfunctions.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── scalars.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── shape.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── simple.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── ufunc_config.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── ufunclike.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── ufuncs.cpython-313.pyc
│   │           │   │   │   │   │   │   └── warnings_and_errors.cpython-313.pyc
│   │           │   │   │   │   │   ├── arithmetic.py
│   │           │   │   │   │   │   ├── array_constructors.py
│   │           │   │   │   │   │   ├── array_like.py
│   │           │   │   │   │   │   ├── arrayprint.py
│   │           │   │   │   │   │   ├── arrayterator.py
│   │           │   │   │   │   │   ├── bitwise_ops.py
│   │           │   │   │   │   │   ├── comparisons.py
│   │           │   │   │   │   │   ├── dtype.py
│   │           │   │   │   │   │   ├── einsumfunc.py
│   │           │   │   │   │   │   ├── flatiter.py
│   │           │   │   │   │   │   ├── fromnumeric.py
│   │           │   │   │   │   │   ├── index_tricks.py
│   │           │   │   │   │   │   ├── lib_user_array.py
│   │           │   │   │   │   │   ├── lib_utils.py
│   │           │   │   │   │   │   ├── lib_version.py
│   │           │   │   │   │   │   ├── literal.py
│   │           │   │   │   │   │   ├── ma.py
│   │           │   │   │   │   │   ├── mod.py
│   │           │   │   │   │   │   ├── modules.py
│   │           │   │   │   │   │   ├── multiarray.py
│   │           │   │   │   │   │   ├── ndarray_conversion.py
│   │           │   │   │   │   │   ├── ndarray_misc.py
│   │           │   │   │   │   │   ├── ndarray_shape_manipulation.py
│   │           │   │   │   │   │   ├── nditer.py
│   │           │   │   │   │   │   ├── numeric.py
│   │           │   │   │   │   │   ├── numerictypes.py
│   │           │   │   │   │   │   ├── random.py
│   │           │   │   │   │   │   ├── recfunctions.py
│   │           │   │   │   │   │   ├── scalars.py
│   │           │   │   │   │   │   ├── shape.py
│   │           │   │   │   │   │   ├── simple.py
│   │           │   │   │   │   │   ├── ufunc_config.py
│   │           │   │   │   │   │   ├── ufunclike.py
│   │           │   │   │   │   │   ├── ufuncs.py
│   │           │   │   │   │   │   └── warnings_and_errors.py
│   │           │   │   │   │   ├── reveal
│   │           │   │   │   │   │   ├── arithmetic.pyi
│   │           │   │   │   │   │   ├── array_api_info.pyi
│   │           │   │   │   │   │   ├── array_constructors.pyi
│   │           │   │   │   │   │   ├── arraypad.pyi
│   │           │   │   │   │   │   ├── arrayprint.pyi
│   │           │   │   │   │   │   ├── arraysetops.pyi
│   │           │   │   │   │   │   ├── arrayterator.pyi
│   │           │   │   │   │   │   ├── bitwise_ops.pyi
│   │           │   │   │   │   │   ├── char.pyi
│   │           │   │   │   │   │   ├── chararray.pyi
│   │           │   │   │   │   │   ├── comparisons.pyi
│   │           │   │   │   │   │   ├── constants.pyi
│   │           │   │   │   │   │   ├── ctypeslib.pyi
│   │           │   │   │   │   │   ├── datasource.pyi
│   │           │   │   │   │   │   ├── dtype.pyi
│   │           │   │   │   │   │   ├── einsumfunc.pyi
│   │           │   │   │   │   │   ├── emath.pyi
│   │           │   │   │   │   │   ├── fft.pyi
│   │           │   │   │   │   │   ├── flatiter.pyi
│   │           │   │   │   │   │   ├── fromnumeric.pyi
│   │           │   │   │   │   │   ├── getlimits.pyi
│   │           │   │   │   │   │   ├── histograms.pyi
│   │           │   │   │   │   │   ├── index_tricks.pyi
│   │           │   │   │   │   │   ├── lib_function_base.pyi
│   │           │   │   │   │   │   ├── lib_polynomial.pyi
│   │           │   │   │   │   │   ├── lib_utils.pyi
│   │           │   │   │   │   │   ├── lib_version.pyi
│   │           │   │   │   │   │   ├── linalg.pyi
│   │           │   │   │   │   │   ├── ma.pyi
│   │           │   │   │   │   │   ├── matrix.pyi
│   │           │   │   │   │   │   ├── memmap.pyi
│   │           │   │   │   │   │   ├── mod.pyi
│   │           │   │   │   │   │   ├── modules.pyi
│   │           │   │   │   │   │   ├── multiarray.pyi
│   │           │   │   │   │   │   ├── nbit_base_example.pyi
│   │           │   │   │   │   │   ├── ndarray_assignability.pyi
│   │           │   │   │   │   │   ├── ndarray_conversion.pyi
│   │           │   │   │   │   │   ├── ndarray_misc.pyi
│   │           │   │   │   │   │   ├── ndarray_shape_manipulation.pyi
│   │           │   │   │   │   │   ├── nditer.pyi
│   │           │   │   │   │   │   ├── nested_sequence.pyi
│   │           │   │   │   │   │   ├── npyio.pyi
│   │           │   │   │   │   │   ├── numeric.pyi
│   │           │   │   │   │   │   ├── numerictypes.pyi
│   │           │   │   │   │   │   ├── polynomial_polybase.pyi
│   │           │   │   │   │   │   ├── polynomial_polyutils.pyi
│   │           │   │   │   │   │   ├── polynomial_series.pyi
│   │           │   │   │   │   │   ├── random.pyi
│   │           │   │   │   │   │   ├── rec.pyi
│   │           │   │   │   │   │   ├── scalars.pyi
│   │           │   │   │   │   │   ├── shape_base.pyi
│   │           │   │   │   │   │   ├── shape.pyi
│   │           │   │   │   │   │   ├── stride_tricks.pyi
│   │           │   │   │   │   │   ├── strings.pyi
│   │           │   │   │   │   │   ├── testing.pyi
│   │           │   │   │   │   │   ├── twodim_base.pyi
│   │           │   │   │   │   │   ├── type_check.pyi
│   │           │   │   │   │   │   ├── ufunc_config.pyi
│   │           │   │   │   │   │   ├── ufunclike.pyi
│   │           │   │   │   │   │   ├── ufuncs.pyi
│   │           │   │   │   │   │   └── warnings_and_errors.pyi
│   │           │   │   │   │   └── mypy.ini
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_isfile.py
│   │           │   │   │   ├── test_runtime.py
│   │           │   │   │   └── test_typing.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   └── mypy_plugin.py
│   │           │   ├── __config__.py
│   │           │   ├── __config__.pyi
│   │           │   ├── __init__.cython-30.pxd
│   │           │   ├── __init__.pxd
│   │           │   ├── __init__.py
│   │           │   ├── __init__.pyi
│   │           │   ├── _array_api_info.py
│   │           │   ├── _array_api_info.pyi
│   │           │   ├── _configtool.py
│   │           │   ├── _configtool.pyi
│   │           │   ├── _distributor_init.py
│   │           │   ├── _distributor_init.pyi
│   │           │   ├── _expired_attrs_2_0.py
│   │           │   ├── _expired_attrs_2_0.pyi
│   │           │   ├── _globals.py
│   │           │   ├── _globals.pyi
│   │           │   ├── _pytesttester.py
│   │           │   ├── _pytesttester.pyi
│   │           │   ├── conftest.py
│   │           │   ├── dtypes.py
│   │           │   ├── dtypes.pyi
│   │           │   ├── exceptions.py
│   │           │   ├── exceptions.pyi
│   │           │   ├── matlib.py
│   │           │   ├── matlib.pyi
│   │           │   ├── py.typed
│   │           │   ├── version.py
│   │           │   └── version.pyi
│   │           ├── numpy-2.4.0.dist-info
│   │           │   ├── licenses
│   │           │   │   ├── numpy
│   │           │   │   │   ├── _core
│   │           │   │   │   │   ├── include
│   │           │   │   │   │   │   └── numpy
│   │           │   │   │   │   │       └── libdivide
│   │           │   │   │   │   │           └── LICENSE.txt
│   │           │   │   │   │   └── src
│   │           │   │   │   │       ├── common
│   │           │   │   │   │       │   └── pythoncapi-compat
│   │           │   │   │   │       │       └── COPYING
│   │           │   │   │   │       ├── highway
│   │           │   │   │   │       │   └── LICENSE
│   │           │   │   │   │       ├── multiarray
│   │           │   │   │   │       │   └── dragon4_LICENSE.txt
│   │           │   │   │   │       ├── npysort
│   │           │   │   │   │       │   └── x86-simd-sort
│   │           │   │   │   │       │       └── LICENSE.md
│   │           │   │   │   │       └── umath
│   │           │   │   │   │           └── svml
│   │           │   │   │   │               └── LICENSE
│   │           │   │   │   ├── fft
│   │           │   │   │   │   └── pocketfft
│   │           │   │   │   │       └── LICENSE.md
│   │           │   │   │   ├── linalg
│   │           │   │   │   │   └── lapack_lite
│   │           │   │   │   │       └── LICENSE.txt
│   │           │   │   │   ├── ma
│   │           │   │   │   │   └── LICENSE
│   │           │   │   │   └── random
│   │           │   │   │       ├── src
│   │           │   │   │       │   ├── distributions
│   │           │   │   │       │   │   └── LICENSE.md
│   │           │   │   │       │   ├── mt19937
│   │           │   │   │       │   │   └── LICENSE.md
│   │           │   │   │       │   ├── pcg64
│   │           │   │   │       │   │   └── LICENSE.md
│   │           │   │   │       │   ├── philox
│   │           │   │   │       │   │   └── LICENSE.md
│   │           │   │   │       │   ├── sfc64
│   │           │   │   │       │   │   └── LICENSE.md
│   │           │   │   │       │   └── splitmix64
│   │           │   │   │       │       └── LICENSE.md
│   │           │   │   │       └── LICENSE.md
│   │           │   │   └── LICENSE.txt
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   └── WHEEL
│   │           ├── packaging
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── _elffile.cpython-313.pyc
│   │           │   │   ├── _manylinux.cpython-313.pyc
│   │           │   │   ├── _musllinux.cpython-313.pyc
│   │           │   │   ├── _parser.cpython-313.pyc
│   │           │   │   ├── _structures.cpython-313.pyc
│   │           │   │   ├── _tokenizer.cpython-313.pyc
│   │           │   │   ├── markers.cpython-313.pyc
│   │           │   │   ├── metadata.cpython-313.pyc
│   │           │   │   ├── requirements.cpython-313.pyc
│   │           │   │   ├── specifiers.cpython-313.pyc
│   │           │   │   ├── tags.cpython-313.pyc
│   │           │   │   ├── utils.cpython-313.pyc
│   │           │   │   └── version.cpython-313.pyc
│   │           │   ├── licenses
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   └── _spdx.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   └── _spdx.py
│   │           │   ├── __init__.py
│   │           │   ├── _elffile.py
│   │           │   ├── _manylinux.py
│   │           │   ├── _musllinux.py
│   │           │   ├── _parser.py
│   │           │   ├── _structures.py
│   │           │   ├── _tokenizer.py
│   │           │   ├── markers.py
│   │           │   ├── metadata.py
│   │           │   ├── py.typed
│   │           │   ├── requirements.py
│   │           │   ├── specifiers.py
│   │           │   ├── tags.py
│   │           │   ├── utils.py
│   │           │   └── version.py
│   │           ├── packaging-25.0.dist-info
│   │           │   ├── licenses
│   │           │   │   ├── LICENSE
│   │           │   │   ├── LICENSE.APACHE
│   │           │   │   └── LICENSE.BSD
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── PIL
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── __main__.cpython-313.pyc
│   │           │   │   ├── _binary.cpython-313.pyc
│   │           │   │   ├── _deprecate.cpython-313.pyc
│   │           │   │   ├── _tkinter_finder.cpython-313.pyc
│   │           │   │   ├── _typing.cpython-313.pyc
│   │           │   │   ├── _util.cpython-313.pyc
│   │           │   │   ├── _version.cpython-313.pyc
│   │           │   │   ├── AvifImagePlugin.cpython-313.pyc
│   │           │   │   ├── BdfFontFile.cpython-313.pyc
│   │           │   │   ├── BlpImagePlugin.cpython-313.pyc
│   │           │   │   ├── BmpImagePlugin.cpython-313.pyc
│   │           │   │   ├── BufrStubImagePlugin.cpython-313.pyc
│   │           │   │   ├── ContainerIO.cpython-313.pyc
│   │           │   │   ├── CurImagePlugin.cpython-313.pyc
│   │           │   │   ├── DcxImagePlugin.cpython-313.pyc
│   │           │   │   ├── DdsImagePlugin.cpython-313.pyc
│   │           │   │   ├── EpsImagePlugin.cpython-313.pyc
│   │           │   │   ├── ExifTags.cpython-313.pyc
│   │           │   │   ├── features.cpython-313.pyc
│   │           │   │   ├── FitsImagePlugin.cpython-313.pyc
│   │           │   │   ├── FliImagePlugin.cpython-313.pyc
│   │           │   │   ├── FontFile.cpython-313.pyc
│   │           │   │   ├── FpxImagePlugin.cpython-313.pyc
│   │           │   │   ├── FtexImagePlugin.cpython-313.pyc
│   │           │   │   ├── GbrImagePlugin.cpython-313.pyc
│   │           │   │   ├── GdImageFile.cpython-313.pyc
│   │           │   │   ├── GifImagePlugin.cpython-313.pyc
│   │           │   │   ├── GimpGradientFile.cpython-313.pyc
│   │           │   │   ├── GimpPaletteFile.cpython-313.pyc
│   │           │   │   ├── GribStubImagePlugin.cpython-313.pyc
│   │           │   │   ├── Hdf5StubImagePlugin.cpython-313.pyc
│   │           │   │   ├── IcnsImagePlugin.cpython-313.pyc
│   │           │   │   ├── IcoImagePlugin.cpython-313.pyc
│   │           │   │   ├── Image.cpython-313.pyc
│   │           │   │   ├── ImageChops.cpython-313.pyc
│   │           │   │   ├── ImageCms.cpython-313.pyc
│   │           │   │   ├── ImageColor.cpython-313.pyc
│   │           │   │   ├── ImageDraw.cpython-313.pyc
│   │           │   │   ├── ImageDraw2.cpython-313.pyc
│   │           │   │   ├── ImageEnhance.cpython-313.pyc
│   │           │   │   ├── ImageFile.cpython-313.pyc
│   │           │   │   ├── ImageFilter.cpython-313.pyc
│   │           │   │   ├── ImageFont.cpython-313.pyc
│   │           │   │   ├── ImageGrab.cpython-313.pyc
│   │           │   │   ├── ImageMath.cpython-313.pyc
│   │           │   │   ├── ImageMode.cpython-313.pyc
│   │           │   │   ├── ImageMorph.cpython-313.pyc
│   │           │   │   ├── ImageOps.cpython-313.pyc
│   │           │   │   ├── ImagePalette.cpython-313.pyc
│   │           │   │   ├── ImagePath.cpython-313.pyc
│   │           │   │   ├── ImageQt.cpython-313.pyc
│   │           │   │   ├── ImageSequence.cpython-313.pyc
│   │           │   │   ├── ImageShow.cpython-313.pyc
│   │           │   │   ├── ImageStat.cpython-313.pyc
│   │           │   │   ├── ImageText.cpython-313.pyc
│   │           │   │   ├── ImageTk.cpython-313.pyc
│   │           │   │   ├── ImageTransform.cpython-313.pyc
│   │           │   │   ├── ImageWin.cpython-313.pyc
│   │           │   │   ├── ImImagePlugin.cpython-313.pyc
│   │           │   │   ├── ImtImagePlugin.cpython-313.pyc
│   │           │   │   ├── IptcImagePlugin.cpython-313.pyc
│   │           │   │   ├── Jpeg2KImagePlugin.cpython-313.pyc
│   │           │   │   ├── JpegImagePlugin.cpython-313.pyc
│   │           │   │   ├── JpegPresets.cpython-313.pyc
│   │           │   │   ├── McIdasImagePlugin.cpython-313.pyc
│   │           │   │   ├── MicImagePlugin.cpython-313.pyc
│   │           │   │   ├── MpegImagePlugin.cpython-313.pyc
│   │           │   │   ├── MpoImagePlugin.cpython-313.pyc
│   │           │   │   ├── MspImagePlugin.cpython-313.pyc
│   │           │   │   ├── PaletteFile.cpython-313.pyc
│   │           │   │   ├── PalmImagePlugin.cpython-313.pyc
│   │           │   │   ├── PcdImagePlugin.cpython-313.pyc
│   │           │   │   ├── PcfFontFile.cpython-313.pyc
│   │           │   │   ├── PcxImagePlugin.cpython-313.pyc
│   │           │   │   ├── PdfImagePlugin.cpython-313.pyc
│   │           │   │   ├── PdfParser.cpython-313.pyc
│   │           │   │   ├── PixarImagePlugin.cpython-313.pyc
│   │           │   │   ├── PngImagePlugin.cpython-313.pyc
│   │           │   │   ├── PpmImagePlugin.cpython-313.pyc
│   │           │   │   ├── PsdImagePlugin.cpython-313.pyc
│   │           │   │   ├── PSDraw.cpython-313.pyc
│   │           │   │   ├── QoiImagePlugin.cpython-313.pyc
│   │           │   │   ├── report.cpython-313.pyc
│   │           │   │   ├── SgiImagePlugin.cpython-313.pyc
│   │           │   │   ├── SpiderImagePlugin.cpython-313.pyc
│   │           │   │   ├── SunImagePlugin.cpython-313.pyc
│   │           │   │   ├── TarIO.cpython-313.pyc
│   │           │   │   ├── TgaImagePlugin.cpython-313.pyc
│   │           │   │   ├── TiffImagePlugin.cpython-313.pyc
│   │           │   │   ├── TiffTags.cpython-313.pyc
│   │           │   │   ├── WalImageFile.cpython-313.pyc
│   │           │   │   ├── WebPImagePlugin.cpython-313.pyc
│   │           │   │   ├── WmfImagePlugin.cpython-313.pyc
│   │           │   │   ├── XbmImagePlugin.cpython-313.pyc
│   │           │   │   ├── XpmImagePlugin.cpython-313.pyc
│   │           │   │   └── XVThumbImagePlugin.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── _avif.cpython-313-darwin.so
│   │           │   ├── _avif.pyi
│   │           │   ├── _binary.py
│   │           │   ├── _deprecate.py
│   │           │   ├── _imaging.cpython-313-darwin.so
│   │           │   ├── _imaging.pyi
│   │           │   ├── _imagingcms.cpython-313-darwin.so
│   │           │   ├── _imagingcms.pyi
│   │           │   ├── _imagingft.cpython-313-darwin.so
│   │           │   ├── _imagingft.pyi
│   │           │   ├── _imagingmath.cpython-313-darwin.so
│   │           │   ├── _imagingmath.pyi
│   │           │   ├── _imagingmorph.cpython-313-darwin.so
│   │           │   ├── _imagingmorph.pyi
│   │           │   ├── _imagingtk.cpython-313-darwin.so
│   │           │   ├── _imagingtk.pyi
│   │           │   ├── _tkinter_finder.py
│   │           │   ├── _typing.py
│   │           │   ├── _util.py
│   │           │   ├── _version.py
│   │           │   ├── _webp.cpython-313-darwin.so
│   │           │   ├── _webp.pyi
│   │           │   ├── AvifImagePlugin.py
│   │           │   ├── BdfFontFile.py
│   │           │   ├── BlpImagePlugin.py
│   │           │   ├── BmpImagePlugin.py
│   │           │   ├── BufrStubImagePlugin.py
│   │           │   ├── ContainerIO.py
│   │           │   ├── CurImagePlugin.py
│   │           │   ├── DcxImagePlugin.py
│   │           │   ├── DdsImagePlugin.py
│   │           │   ├── EpsImagePlugin.py
│   │           │   ├── ExifTags.py
│   │           │   ├── features.py
│   │           │   ├── FitsImagePlugin.py
│   │           │   ├── FliImagePlugin.py
│   │           │   ├── FontFile.py
│   │           │   ├── FpxImagePlugin.py
│   │           │   ├── FtexImagePlugin.py
│   │           │   ├── GbrImagePlugin.py
│   │           │   ├── GdImageFile.py
│   │           │   ├── GifImagePlugin.py
│   │           │   ├── GimpGradientFile.py
│   │           │   ├── GimpPaletteFile.py
│   │           │   ├── GribStubImagePlugin.py
│   │           │   ├── Hdf5StubImagePlugin.py
│   │           │   ├── IcnsImagePlugin.py
│   │           │   ├── IcoImagePlugin.py
│   │           │   ├── Image.py
│   │           │   ├── ImageChops.py
│   │           │   ├── ImageCms.py
│   │           │   ├── ImageColor.py
│   │           │   ├── ImageDraw.py
│   │           │   ├── ImageDraw2.py
│   │           │   ├── ImageEnhance.py
│   │           │   ├── ImageFile.py
│   │           │   ├── ImageFilter.py
│   │           │   ├── ImageFont.py
│   │           │   ├── ImageGrab.py
│   │           │   ├── ImageMath.py
│   │           │   ├── ImageMode.py
│   │           │   ├── ImageMorph.py
│   │           │   ├── ImageOps.py
│   │           │   ├── ImagePalette.py
│   │           │   ├── ImagePath.py
│   │           │   ├── ImageQt.py
│   │           │   ├── ImageSequence.py
│   │           │   ├── ImageShow.py
│   │           │   ├── ImageStat.py
│   │           │   ├── ImageText.py
│   │           │   ├── ImageTk.py
│   │           │   ├── ImageTransform.py
│   │           │   ├── ImageWin.py
│   │           │   ├── ImImagePlugin.py
│   │           │   ├── ImtImagePlugin.py
│   │           │   ├── IptcImagePlugin.py
│   │           │   ├── Jpeg2KImagePlugin.py
│   │           │   ├── JpegImagePlugin.py
│   │           │   ├── JpegPresets.py
│   │           │   ├── McIdasImagePlugin.py
│   │           │   ├── MicImagePlugin.py
│   │           │   ├── MpegImagePlugin.py
│   │           │   ├── MpoImagePlugin.py
│   │           │   ├── MspImagePlugin.py
│   │           │   ├── PaletteFile.py
│   │           │   ├── PalmImagePlugin.py
│   │           │   ├── PcdImagePlugin.py
│   │           │   ├── PcfFontFile.py
│   │           │   ├── PcxImagePlugin.py
│   │           │   ├── PdfImagePlugin.py
│   │           │   ├── PdfParser.py
│   │           │   ├── PixarImagePlugin.py
│   │           │   ├── PngImagePlugin.py
│   │           │   ├── PpmImagePlugin.py
│   │           │   ├── PsdImagePlugin.py
│   │           │   ├── PSDraw.py
│   │           │   ├── py.typed
│   │           │   ├── QoiImagePlugin.py
│   │           │   ├── report.py
│   │           │   ├── SgiImagePlugin.py
│   │           │   ├── SpiderImagePlugin.py
│   │           │   ├── SunImagePlugin.py
│   │           │   ├── TarIO.py
│   │           │   ├── TgaImagePlugin.py
│   │           │   ├── TiffImagePlugin.py
│   │           │   ├── TiffTags.py
│   │           │   ├── WalImageFile.py
│   │           │   ├── WebPImagePlugin.py
│   │           │   ├── WmfImagePlugin.py
│   │           │   ├── XbmImagePlugin.py
│   │           │   ├── XpmImagePlugin.py
│   │           │   └── XVThumbImagePlugin.py
│   │           ├── pillow-12.0.0.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── top_level.txt
│   │           │   ├── WHEEL
│   │           │   └── zip-safe
│   │           ├── pip
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── __main__.cpython-313.pyc
│   │           │   │   └── __pip-runner__.cpython-313.pyc
│   │           │   ├── _internal
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── build_env.cpython-313.pyc
│   │           │   │   │   ├── cache.cpython-313.pyc
│   │           │   │   │   ├── configuration.cpython-313.pyc
│   │           │   │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   │   ├── main.cpython-313.pyc
│   │           │   │   │   ├── pyproject.cpython-313.pyc
│   │           │   │   │   ├── self_outdated_check.cpython-313.pyc
│   │           │   │   │   └── wheel_builder.cpython-313.pyc
│   │           │   │   ├── cli
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── autocompletion.cpython-313.pyc
│   │           │   │   │   │   ├── base_command.cpython-313.pyc
│   │           │   │   │   │   ├── cmdoptions.cpython-313.pyc
│   │           │   │   │   │   ├── command_context.cpython-313.pyc
│   │           │   │   │   │   ├── index_command.cpython-313.pyc
│   │           │   │   │   │   ├── main_parser.cpython-313.pyc
│   │           │   │   │   │   ├── main.cpython-313.pyc
│   │           │   │   │   │   ├── parser.cpython-313.pyc
│   │           │   │   │   │   ├── progress_bars.cpython-313.pyc
│   │           │   │   │   │   ├── req_command.cpython-313.pyc
│   │           │   │   │   │   ├── spinners.cpython-313.pyc
│   │           │   │   │   │   └── status_codes.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── autocompletion.py
│   │           │   │   │   ├── base_command.py
│   │           │   │   │   ├── cmdoptions.py
│   │           │   │   │   ├── command_context.py
│   │           │   │   │   ├── index_command.py
│   │           │   │   │   ├── main_parser.py
│   │           │   │   │   ├── main.py
│   │           │   │   │   ├── parser.py
│   │           │   │   │   ├── progress_bars.py
│   │           │   │   │   ├── req_command.py
│   │           │   │   │   ├── spinners.py
│   │           │   │   │   └── status_codes.py
│   │           │   │   ├── commands
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── cache.cpython-313.pyc
│   │           │   │   │   │   ├── check.cpython-313.pyc
│   │           │   │   │   │   ├── completion.cpython-313.pyc
│   │           │   │   │   │   ├── configuration.cpython-313.pyc
│   │           │   │   │   │   ├── debug.cpython-313.pyc
│   │           │   │   │   │   ├── download.cpython-313.pyc
│   │           │   │   │   │   ├── freeze.cpython-313.pyc
│   │           │   │   │   │   ├── hash.cpython-313.pyc
│   │           │   │   │   │   ├── help.cpython-313.pyc
│   │           │   │   │   │   ├── index.cpython-313.pyc
│   │           │   │   │   │   ├── inspect.cpython-313.pyc
│   │           │   │   │   │   ├── install.cpython-313.pyc
│   │           │   │   │   │   ├── list.cpython-313.pyc
│   │           │   │   │   │   ├── lock.cpython-313.pyc
│   │           │   │   │   │   ├── search.cpython-313.pyc
│   │           │   │   │   │   ├── show.cpython-313.pyc
│   │           │   │   │   │   ├── uninstall.cpython-313.pyc
│   │           │   │   │   │   └── wheel.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── cache.py
│   │           │   │   │   ├── check.py
│   │           │   │   │   ├── completion.py
│   │           │   │   │   ├── configuration.py
│   │           │   │   │   ├── debug.py
│   │           │   │   │   ├── download.py
│   │           │   │   │   ├── freeze.py
│   │           │   │   │   ├── hash.py
│   │           │   │   │   ├── help.py
│   │           │   │   │   ├── index.py
│   │           │   │   │   ├── inspect.py
│   │           │   │   │   ├── install.py
│   │           │   │   │   ├── list.py
│   │           │   │   │   ├── lock.py
│   │           │   │   │   ├── search.py
│   │           │   │   │   ├── show.py
│   │           │   │   │   ├── uninstall.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── distributions
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── base.cpython-313.pyc
│   │           │   │   │   │   ├── installed.cpython-313.pyc
│   │           │   │   │   │   ├── sdist.cpython-313.pyc
│   │           │   │   │   │   └── wheel.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── installed.py
│   │           │   │   │   ├── sdist.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── index
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── collector.cpython-313.pyc
│   │           │   │   │   │   ├── package_finder.cpython-313.pyc
│   │           │   │   │   │   └── sources.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── collector.py
│   │           │   │   │   ├── package_finder.py
│   │           │   │   │   └── sources.py
│   │           │   │   ├── locations
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── _distutils.cpython-313.pyc
│   │           │   │   │   │   ├── _sysconfig.cpython-313.pyc
│   │           │   │   │   │   └── base.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _distutils.py
│   │           │   │   │   ├── _sysconfig.py
│   │           │   │   │   └── base.py
│   │           │   │   ├── metadata
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── _json.cpython-313.pyc
│   │           │   │   │   │   ├── base.cpython-313.pyc
│   │           │   │   │   │   └── pkg_resources.cpython-313.pyc
│   │           │   │   │   ├── importlib
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   ├── _compat.cpython-313.pyc
│   │           │   │   │   │   │   ├── _dists.cpython-313.pyc
│   │           │   │   │   │   │   └── _envs.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── _compat.py
│   │           │   │   │   │   ├── _dists.py
│   │           │   │   │   │   └── _envs.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _json.py
│   │           │   │   │   ├── base.py
│   │           │   │   │   └── pkg_resources.py
│   │           │   │   ├── models
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── candidate.cpython-313.pyc
│   │           │   │   │   │   ├── direct_url.cpython-313.pyc
│   │           │   │   │   │   ├── format_control.cpython-313.pyc
│   │           │   │   │   │   ├── index.cpython-313.pyc
│   │           │   │   │   │   ├── installation_report.cpython-313.pyc
│   │           │   │   │   │   ├── link.cpython-313.pyc
│   │           │   │   │   │   ├── pylock.cpython-313.pyc
│   │           │   │   │   │   ├── scheme.cpython-313.pyc
│   │           │   │   │   │   ├── search_scope.cpython-313.pyc
│   │           │   │   │   │   ├── selection_prefs.cpython-313.pyc
│   │           │   │   │   │   ├── target_python.cpython-313.pyc
│   │           │   │   │   │   └── wheel.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── candidate.py
│   │           │   │   │   ├── direct_url.py
│   │           │   │   │   ├── format_control.py
│   │           │   │   │   ├── index.py
│   │           │   │   │   ├── installation_report.py
│   │           │   │   │   ├── link.py
│   │           │   │   │   ├── pylock.py
│   │           │   │   │   ├── scheme.py
│   │           │   │   │   ├── search_scope.py
│   │           │   │   │   ├── selection_prefs.py
│   │           │   │   │   ├── target_python.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── network
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── auth.cpython-313.pyc
│   │           │   │   │   │   ├── cache.cpython-313.pyc
│   │           │   │   │   │   ├── download.cpython-313.pyc
│   │           │   │   │   │   ├── lazy_wheel.cpython-313.pyc
│   │           │   │   │   │   ├── session.cpython-313.pyc
│   │           │   │   │   │   ├── utils.cpython-313.pyc
│   │           │   │   │   │   └── xmlrpc.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── auth.py
│   │           │   │   │   ├── cache.py
│   │           │   │   │   ├── download.py
│   │           │   │   │   ├── lazy_wheel.py
│   │           │   │   │   ├── session.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── xmlrpc.py
│   │           │   │   ├── operations
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── check.cpython-313.pyc
│   │           │   │   │   │   ├── freeze.cpython-313.pyc
│   │           │   │   │   │   └── prepare.cpython-313.pyc
│   │           │   │   │   ├── build
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   ├── build_tracker.cpython-313.pyc
│   │           │   │   │   │   │   ├── metadata_editable.cpython-313.pyc
│   │           │   │   │   │   │   ├── metadata.cpython-313.pyc
│   │           │   │   │   │   │   ├── wheel_editable.cpython-313.pyc
│   │           │   │   │   │   │   └── wheel.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── build_tracker.py
│   │           │   │   │   │   ├── metadata_editable.py
│   │           │   │   │   │   ├── metadata.py
│   │           │   │   │   │   ├── wheel_editable.py
│   │           │   │   │   │   └── wheel.py
│   │           │   │   │   ├── install
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   └── wheel.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── wheel.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── check.py
│   │           │   │   │   ├── freeze.py
│   │           │   │   │   └── prepare.py
│   │           │   │   ├── req
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── constructors.cpython-313.pyc
│   │           │   │   │   │   ├── req_dependency_group.cpython-313.pyc
│   │           │   │   │   │   ├── req_file.cpython-313.pyc
│   │           │   │   │   │   ├── req_install.cpython-313.pyc
│   │           │   │   │   │   ├── req_set.cpython-313.pyc
│   │           │   │   │   │   └── req_uninstall.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── constructors.py
│   │           │   │   │   ├── req_dependency_group.py
│   │           │   │   │   ├── req_file.py
│   │           │   │   │   ├── req_install.py
│   │           │   │   │   ├── req_set.py
│   │           │   │   │   └── req_uninstall.py
│   │           │   │   ├── resolution
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   └── base.cpython-313.pyc
│   │           │   │   │   ├── legacy
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   └── resolver.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── resolver.py
│   │           │   │   │   ├── resolvelib
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   ├── base.cpython-313.pyc
│   │           │   │   │   │   │   ├── candidates.cpython-313.pyc
│   │           │   │   │   │   │   ├── factory.cpython-313.pyc
│   │           │   │   │   │   │   ├── found_candidates.cpython-313.pyc
│   │           │   │   │   │   │   ├── provider.cpython-313.pyc
│   │           │   │   │   │   │   ├── reporter.cpython-313.pyc
│   │           │   │   │   │   │   ├── requirements.cpython-313.pyc
│   │           │   │   │   │   │   └── resolver.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── base.py
│   │           │   │   │   │   ├── candidates.py
│   │           │   │   │   │   ├── factory.py
│   │           │   │   │   │   ├── found_candidates.py
│   │           │   │   │   │   ├── provider.py
│   │           │   │   │   │   ├── reporter.py
│   │           │   │   │   │   ├── requirements.py
│   │           │   │   │   │   └── resolver.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── base.py
│   │           │   │   ├── utils
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── _jaraco_text.cpython-313.pyc
│   │           │   │   │   │   ├── _log.cpython-313.pyc
│   │           │   │   │   │   ├── appdirs.cpython-313.pyc
│   │           │   │   │   │   ├── compat.cpython-313.pyc
│   │           │   │   │   │   ├── compatibility_tags.cpython-313.pyc
│   │           │   │   │   │   ├── datetime.cpython-313.pyc
│   │           │   │   │   │   ├── deprecation.cpython-313.pyc
│   │           │   │   │   │   ├── direct_url_helpers.cpython-313.pyc
│   │           │   │   │   │   ├── egg_link.cpython-313.pyc
│   │           │   │   │   │   ├── entrypoints.cpython-313.pyc
│   │           │   │   │   │   ├── filesystem.cpython-313.pyc
│   │           │   │   │   │   ├── filetypes.cpython-313.pyc
│   │           │   │   │   │   ├── glibc.cpython-313.pyc
│   │           │   │   │   │   ├── hashes.cpython-313.pyc
│   │           │   │   │   │   ├── logging.cpython-313.pyc
│   │           │   │   │   │   ├── misc.cpython-313.pyc
│   │           │   │   │   │   ├── packaging.cpython-313.pyc
│   │           │   │   │   │   ├── retry.cpython-313.pyc
│   │           │   │   │   │   ├── subprocess.cpython-313.pyc
│   │           │   │   │   │   ├── temp_dir.cpython-313.pyc
│   │           │   │   │   │   ├── unpacking.cpython-313.pyc
│   │           │   │   │   │   ├── urls.cpython-313.pyc
│   │           │   │   │   │   ├── virtualenv.cpython-313.pyc
│   │           │   │   │   │   └── wheel.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _jaraco_text.py
│   │           │   │   │   ├── _log.py
│   │           │   │   │   ├── appdirs.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── compatibility_tags.py
│   │           │   │   │   ├── datetime.py
│   │           │   │   │   ├── deprecation.py
│   │           │   │   │   ├── direct_url_helpers.py
│   │           │   │   │   ├── egg_link.py
│   │           │   │   │   ├── entrypoints.py
│   │           │   │   │   ├── filesystem.py
│   │           │   │   │   ├── filetypes.py
│   │           │   │   │   ├── glibc.py
│   │           │   │   │   ├── hashes.py
│   │           │   │   │   ├── logging.py
│   │           │   │   │   ├── misc.py
│   │           │   │   │   ├── packaging.py
│   │           │   │   │   ├── retry.py
│   │           │   │   │   ├── subprocess.py
│   │           │   │   │   ├── temp_dir.py
│   │           │   │   │   ├── unpacking.py
│   │           │   │   │   ├── urls.py
│   │           │   │   │   ├── virtualenv.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── vcs
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── bazaar.cpython-313.pyc
│   │           │   │   │   │   ├── git.cpython-313.pyc
│   │           │   │   │   │   ├── mercurial.cpython-313.pyc
│   │           │   │   │   │   ├── subversion.cpython-313.pyc
│   │           │   │   │   │   └── versioncontrol.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── bazaar.py
│   │           │   │   │   ├── git.py
│   │           │   │   │   ├── mercurial.py
│   │           │   │   │   ├── subversion.py
│   │           │   │   │   └── versioncontrol.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── build_env.py
│   │           │   │   ├── cache.py
│   │           │   │   ├── configuration.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── main.py
│   │           │   │   ├── pyproject.py
│   │           │   │   ├── self_outdated_check.py
│   │           │   │   └── wheel_builder.py
│   │           │   ├── _vendor
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-313.pyc
│   │           │   │   ├── cachecontrol
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── _cmd.cpython-313.pyc
│   │           │   │   │   │   ├── adapter.cpython-313.pyc
│   │           │   │   │   │   ├── cache.cpython-313.pyc
│   │           │   │   │   │   ├── controller.cpython-313.pyc
│   │           │   │   │   │   ├── filewrapper.cpython-313.pyc
│   │           │   │   │   │   ├── heuristics.cpython-313.pyc
│   │           │   │   │   │   ├── serialize.cpython-313.pyc
│   │           │   │   │   │   └── wrapper.cpython-313.pyc
│   │           │   │   │   ├── caches
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   ├── file_cache.cpython-313.pyc
│   │           │   │   │   │   │   └── redis_cache.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── file_cache.py
│   │           │   │   │   │   └── redis_cache.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _cmd.py
│   │           │   │   │   ├── adapter.py
│   │           │   │   │   ├── cache.py
│   │           │   │   │   ├── controller.py
│   │           │   │   │   ├── filewrapper.py
│   │           │   │   │   ├── heuristics.py
│   │           │   │   │   ├── LICENSE.txt
│   │           │   │   │   ├── py.typed
│   │           │   │   │   ├── serialize.py
│   │           │   │   │   └── wrapper.py
│   │           │   │   ├── certifi
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── __main__.cpython-313.pyc
│   │           │   │   │   │   └── core.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __main__.py
│   │           │   │   │   ├── cacert.pem
│   │           │   │   │   ├── core.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   └── py.typed
│   │           │   │   ├── dependency_groups
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── __main__.cpython-313.pyc
│   │           │   │   │   │   ├── _implementation.cpython-313.pyc
│   │           │   │   │   │   ├── _lint_dependency_groups.cpython-313.pyc
│   │           │   │   │   │   ├── _pip_wrapper.cpython-313.pyc
│   │           │   │   │   │   └── _toml_compat.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __main__.py
│   │           │   │   │   ├── _implementation.py
│   │           │   │   │   ├── _lint_dependency_groups.py
│   │           │   │   │   ├── _pip_wrapper.py
│   │           │   │   │   ├── _toml_compat.py
│   │           │   │   │   ├── LICENSE.txt
│   │           │   │   │   └── py.typed
│   │           │   │   ├── distlib
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── compat.cpython-313.pyc
│   │           │   │   │   │   ├── resources.cpython-313.pyc
│   │           │   │   │   │   ├── scripts.cpython-313.pyc
│   │           │   │   │   │   └── util.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── LICENSE.txt
│   │           │   │   │   ├── resources.py
│   │           │   │   │   ├── scripts.py
│   │           │   │   │   ├── t32.exe
│   │           │   │   │   ├── t64-arm.exe
│   │           │   │   │   ├── t64.exe
│   │           │   │   │   ├── util.py
│   │           │   │   │   ├── w32.exe
│   │           │   │   │   ├── w64-arm.exe
│   │           │   │   │   └── w64.exe
│   │           │   │   ├── distro
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── __main__.cpython-313.pyc
│   │           │   │   │   │   └── distro.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __main__.py
│   │           │   │   │   ├── distro.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   └── py.typed
│   │           │   │   ├── idna
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── codec.cpython-313.pyc
│   │           │   │   │   │   ├── compat.cpython-313.pyc
│   │           │   │   │   │   ├── core.cpython-313.pyc
│   │           │   │   │   │   ├── idnadata.cpython-313.pyc
│   │           │   │   │   │   ├── intranges.cpython-313.pyc
│   │           │   │   │   │   ├── package_data.cpython-313.pyc
│   │           │   │   │   │   └── uts46data.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── codec.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── core.py
│   │           │   │   │   ├── idnadata.py
│   │           │   │   │   ├── intranges.py
│   │           │   │   │   ├── LICENSE.md
│   │           │   │   │   ├── package_data.py
│   │           │   │   │   ├── py.typed
│   │           │   │   │   └── uts46data.py
│   │           │   │   ├── msgpack
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   │   │   ├── ext.cpython-313.pyc
│   │           │   │   │   │   └── fallback.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── COPYING
│   │           │   │   │   ├── exceptions.py
│   │           │   │   │   ├── ext.py
│   │           │   │   │   └── fallback.py
│   │           │   │   ├── packaging
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── _elffile.cpython-313.pyc
│   │           │   │   │   │   ├── _manylinux.cpython-313.pyc
│   │           │   │   │   │   ├── _musllinux.cpython-313.pyc
│   │           │   │   │   │   ├── _parser.cpython-313.pyc
│   │           │   │   │   │   ├── _structures.cpython-313.pyc
│   │           │   │   │   │   ├── _tokenizer.cpython-313.pyc
│   │           │   │   │   │   ├── markers.cpython-313.pyc
│   │           │   │   │   │   ├── metadata.cpython-313.pyc
│   │           │   │   │   │   ├── requirements.cpython-313.pyc
│   │           │   │   │   │   ├── specifiers.cpython-313.pyc
│   │           │   │   │   │   ├── tags.cpython-313.pyc
│   │           │   │   │   │   ├── utils.cpython-313.pyc
│   │           │   │   │   │   └── version.cpython-313.pyc
│   │           │   │   │   ├── licenses
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   └── _spdx.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── _spdx.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _elffile.py
│   │           │   │   │   ├── _manylinux.py
│   │           │   │   │   ├── _musllinux.py
│   │           │   │   │   ├── _parser.py
│   │           │   │   │   ├── _structures.py
│   │           │   │   │   ├── _tokenizer.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   ├── LICENSE.APACHE
│   │           │   │   │   ├── LICENSE.BSD
│   │           │   │   │   ├── markers.py
│   │           │   │   │   ├── metadata.py
│   │           │   │   │   ├── py.typed
│   │           │   │   │   ├── requirements.py
│   │           │   │   │   ├── specifiers.py
│   │           │   │   │   ├── tags.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── version.py
│   │           │   │   ├── pkg_resources
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   └── __init__.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── LICENSE
│   │           │   │   ├── platformdirs
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── __main__.cpython-313.pyc
│   │           │   │   │   │   ├── android.cpython-313.pyc
│   │           │   │   │   │   ├── api.cpython-313.pyc
│   │           │   │   │   │   ├── macos.cpython-313.pyc
│   │           │   │   │   │   ├── unix.cpython-313.pyc
│   │           │   │   │   │   ├── version.cpython-313.pyc
│   │           │   │   │   │   └── windows.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __main__.py
│   │           │   │   │   ├── android.py
│   │           │   │   │   ├── api.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   ├── macos.py
│   │           │   │   │   ├── py.typed
│   │           │   │   │   ├── unix.py
│   │           │   │   │   ├── version.py
│   │           │   │   │   └── windows.py
│   │           │   │   ├── pygments
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── __main__.cpython-313.pyc
│   │           │   │   │   │   ├── console.cpython-313.pyc
│   │           │   │   │   │   ├── filter.cpython-313.pyc
│   │           │   │   │   │   ├── formatter.cpython-313.pyc
│   │           │   │   │   │   ├── lexer.cpython-313.pyc
│   │           │   │   │   │   ├── modeline.cpython-313.pyc
│   │           │   │   │   │   ├── plugin.cpython-313.pyc
│   │           │   │   │   │   ├── regexopt.cpython-313.pyc
│   │           │   │   │   │   ├── scanner.cpython-313.pyc
│   │           │   │   │   │   ├── sphinxext.cpython-313.pyc
│   │           │   │   │   │   ├── style.cpython-313.pyc
│   │           │   │   │   │   ├── token.cpython-313.pyc
│   │           │   │   │   │   ├── unistring.cpython-313.pyc
│   │           │   │   │   │   └── util.cpython-313.pyc
│   │           │   │   │   ├── filters
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   └── __init__.cpython-313.pyc
│   │           │   │   │   │   └── __init__.py
│   │           │   │   │   ├── formatters
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   └── _mapping.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── _mapping.py
│   │           │   │   │   ├── lexers
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   ├── _mapping.cpython-313.pyc
│   │           │   │   │   │   │   └── python.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── _mapping.py
│   │           │   │   │   │   └── python.py
│   │           │   │   │   ├── styles
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   └── _mapping.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── _mapping.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __main__.py
│   │           │   │   │   ├── console.py
│   │           │   │   │   ├── filter.py
│   │           │   │   │   ├── formatter.py
│   │           │   │   │   ├── lexer.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   ├── modeline.py
│   │           │   │   │   ├── plugin.py
│   │           │   │   │   ├── regexopt.py
│   │           │   │   │   ├── scanner.py
│   │           │   │   │   ├── sphinxext.py
│   │           │   │   │   ├── style.py
│   │           │   │   │   ├── token.py
│   │           │   │   │   ├── unistring.py
│   │           │   │   │   └── util.py
│   │           │   │   ├── pyproject_hooks
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   └── _impl.cpython-313.pyc
│   │           │   │   │   ├── _in_process
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   └── _in_process.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── _in_process.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _impl.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   └── py.typed
│   │           │   │   ├── requests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── __version__.cpython-313.pyc
│   │           │   │   │   │   ├── _internal_utils.cpython-313.pyc
│   │           │   │   │   │   ├── adapters.cpython-313.pyc
│   │           │   │   │   │   ├── api.cpython-313.pyc
│   │           │   │   │   │   ├── auth.cpython-313.pyc
│   │           │   │   │   │   ├── certs.cpython-313.pyc
│   │           │   │   │   │   ├── compat.cpython-313.pyc
│   │           │   │   │   │   ├── cookies.cpython-313.pyc
│   │           │   │   │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   │   │   ├── help.cpython-313.pyc
│   │           │   │   │   │   ├── hooks.cpython-313.pyc
│   │           │   │   │   │   ├── models.cpython-313.pyc
│   │           │   │   │   │   ├── packages.cpython-313.pyc
│   │           │   │   │   │   ├── sessions.cpython-313.pyc
│   │           │   │   │   │   ├── status_codes.cpython-313.pyc
│   │           │   │   │   │   ├── structures.cpython-313.pyc
│   │           │   │   │   │   └── utils.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __version__.py
│   │           │   │   │   ├── _internal_utils.py
│   │           │   │   │   ├── adapters.py
│   │           │   │   │   ├── api.py
│   │           │   │   │   ├── auth.py
│   │           │   │   │   ├── certs.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── cookies.py
│   │           │   │   │   ├── exceptions.py
│   │           │   │   │   ├── help.py
│   │           │   │   │   ├── hooks.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   ├── models.py
│   │           │   │   │   ├── packages.py
│   │           │   │   │   ├── sessions.py
│   │           │   │   │   ├── status_codes.py
│   │           │   │   │   ├── structures.py
│   │           │   │   │   └── utils.py
│   │           │   │   ├── resolvelib
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── providers.cpython-313.pyc
│   │           │   │   │   │   ├── reporters.cpython-313.pyc
│   │           │   │   │   │   └── structs.cpython-313.pyc
│   │           │   │   │   ├── resolvers
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   ├── abstract.cpython-313.pyc
│   │           │   │   │   │   │   ├── criterion.cpython-313.pyc
│   │           │   │   │   │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   │   │   │   └── resolution.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── abstract.py
│   │           │   │   │   │   ├── criterion.py
│   │           │   │   │   │   ├── exceptions.py
│   │           │   │   │   │   └── resolution.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   ├── providers.py
│   │           │   │   │   ├── py.typed
│   │           │   │   │   ├── reporters.py
│   │           │   │   │   └── structs.py
│   │           │   │   ├── rich
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── __main__.cpython-313.pyc
│   │           │   │   │   │   ├── _cell_widths.cpython-313.pyc
│   │           │   │   │   │   ├── _emoji_codes.cpython-313.pyc
│   │           │   │   │   │   ├── _emoji_replace.cpython-313.pyc
│   │           │   │   │   │   ├── _export_format.cpython-313.pyc
│   │           │   │   │   │   ├── _extension.cpython-313.pyc
│   │           │   │   │   │   ├── _fileno.cpython-313.pyc
│   │           │   │   │   │   ├── _inspect.cpython-313.pyc
│   │           │   │   │   │   ├── _log_render.cpython-313.pyc
│   │           │   │   │   │   ├── _loop.cpython-313.pyc
│   │           │   │   │   │   ├── _null_file.cpython-313.pyc
│   │           │   │   │   │   ├── _palettes.cpython-313.pyc
│   │           │   │   │   │   ├── _pick.cpython-313.pyc
│   │           │   │   │   │   ├── _ratio.cpython-313.pyc
│   │           │   │   │   │   ├── _spinners.cpython-313.pyc
│   │           │   │   │   │   ├── _stack.cpython-313.pyc
│   │           │   │   │   │   ├── _timer.cpython-313.pyc
│   │           │   │   │   │   ├── _win32_console.cpython-313.pyc
│   │           │   │   │   │   ├── _windows_renderer.cpython-313.pyc
│   │           │   │   │   │   ├── _windows.cpython-313.pyc
│   │           │   │   │   │   ├── _wrap.cpython-313.pyc
│   │           │   │   │   │   ├── abc.cpython-313.pyc
│   │           │   │   │   │   ├── align.cpython-313.pyc
│   │           │   │   │   │   ├── ansi.cpython-313.pyc
│   │           │   │   │   │   ├── bar.cpython-313.pyc
│   │           │   │   │   │   ├── box.cpython-313.pyc
│   │           │   │   │   │   ├── cells.cpython-313.pyc
│   │           │   │   │   │   ├── color_triplet.cpython-313.pyc
│   │           │   │   │   │   ├── color.cpython-313.pyc
│   │           │   │   │   │   ├── columns.cpython-313.pyc
│   │           │   │   │   │   ├── console.cpython-313.pyc
│   │           │   │   │   │   ├── constrain.cpython-313.pyc
│   │           │   │   │   │   ├── containers.cpython-313.pyc
│   │           │   │   │   │   ├── control.cpython-313.pyc
│   │           │   │   │   │   ├── default_styles.cpython-313.pyc
│   │           │   │   │   │   ├── diagnose.cpython-313.pyc
│   │           │   │   │   │   ├── emoji.cpython-313.pyc
│   │           │   │   │   │   ├── errors.cpython-313.pyc
│   │           │   │   │   │   ├── file_proxy.cpython-313.pyc
│   │           │   │   │   │   ├── filesize.cpython-313.pyc
│   │           │   │   │   │   ├── highlighter.cpython-313.pyc
│   │           │   │   │   │   ├── json.cpython-313.pyc
│   │           │   │   │   │   ├── jupyter.cpython-313.pyc
│   │           │   │   │   │   ├── layout.cpython-313.pyc
│   │           │   │   │   │   ├── live_render.cpython-313.pyc
│   │           │   │   │   │   ├── live.cpython-313.pyc
│   │           │   │   │   │   ├── logging.cpython-313.pyc
│   │           │   │   │   │   ├── markup.cpython-313.pyc
│   │           │   │   │   │   ├── measure.cpython-313.pyc
│   │           │   │   │   │   ├── padding.cpython-313.pyc
│   │           │   │   │   │   ├── pager.cpython-313.pyc
│   │           │   │   │   │   ├── palette.cpython-313.pyc
│   │           │   │   │   │   ├── panel.cpython-313.pyc
│   │           │   │   │   │   ├── pretty.cpython-313.pyc
│   │           │   │   │   │   ├── progress_bar.cpython-313.pyc
│   │           │   │   │   │   ├── progress.cpython-313.pyc
│   │           │   │   │   │   ├── prompt.cpython-313.pyc
│   │           │   │   │   │   ├── protocol.cpython-313.pyc
│   │           │   │   │   │   ├── region.cpython-313.pyc
│   │           │   │   │   │   ├── repr.cpython-313.pyc
│   │           │   │   │   │   ├── rule.cpython-313.pyc
│   │           │   │   │   │   ├── scope.cpython-313.pyc
│   │           │   │   │   │   ├── screen.cpython-313.pyc
│   │           │   │   │   │   ├── segment.cpython-313.pyc
│   │           │   │   │   │   ├── spinner.cpython-313.pyc
│   │           │   │   │   │   ├── status.cpython-313.pyc
│   │           │   │   │   │   ├── style.cpython-313.pyc
│   │           │   │   │   │   ├── styled.cpython-313.pyc
│   │           │   │   │   │   ├── syntax.cpython-313.pyc
│   │           │   │   │   │   ├── table.cpython-313.pyc
│   │           │   │   │   │   ├── terminal_theme.cpython-313.pyc
│   │           │   │   │   │   ├── text.cpython-313.pyc
│   │           │   │   │   │   ├── theme.cpython-313.pyc
│   │           │   │   │   │   ├── themes.cpython-313.pyc
│   │           │   │   │   │   ├── traceback.cpython-313.pyc
│   │           │   │   │   │   └── tree.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __main__.py
│   │           │   │   │   ├── _cell_widths.py
│   │           │   │   │   ├── _emoji_codes.py
│   │           │   │   │   ├── _emoji_replace.py
│   │           │   │   │   ├── _export_format.py
│   │           │   │   │   ├── _extension.py
│   │           │   │   │   ├── _fileno.py
│   │           │   │   │   ├── _inspect.py
│   │           │   │   │   ├── _log_render.py
│   │           │   │   │   ├── _loop.py
│   │           │   │   │   ├── _null_file.py
│   │           │   │   │   ├── _palettes.py
│   │           │   │   │   ├── _pick.py
│   │           │   │   │   ├── _ratio.py
│   │           │   │   │   ├── _spinners.py
│   │           │   │   │   ├── _stack.py
│   │           │   │   │   ├── _timer.py
│   │           │   │   │   ├── _win32_console.py
│   │           │   │   │   ├── _windows_renderer.py
│   │           │   │   │   ├── _windows.py
│   │           │   │   │   ├── _wrap.py
│   │           │   │   │   ├── abc.py
│   │           │   │   │   ├── align.py
│   │           │   │   │   ├── ansi.py
│   │           │   │   │   ├── bar.py
│   │           │   │   │   ├── box.py
│   │           │   │   │   ├── cells.py
│   │           │   │   │   ├── color_triplet.py
│   │           │   │   │   ├── color.py
│   │           │   │   │   ├── columns.py
│   │           │   │   │   ├── console.py
│   │           │   │   │   ├── constrain.py
│   │           │   │   │   ├── containers.py
│   │           │   │   │   ├── control.py
│   │           │   │   │   ├── default_styles.py
│   │           │   │   │   ├── diagnose.py
│   │           │   │   │   ├── emoji.py
│   │           │   │   │   ├── errors.py
│   │           │   │   │   ├── file_proxy.py
│   │           │   │   │   ├── filesize.py
│   │           │   │   │   ├── highlighter.py
│   │           │   │   │   ├── json.py
│   │           │   │   │   ├── jupyter.py
│   │           │   │   │   ├── layout.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   ├── live_render.py
│   │           │   │   │   ├── live.py
│   │           │   │   │   ├── logging.py
│   │           │   │   │   ├── markup.py
│   │           │   │   │   ├── measure.py
│   │           │   │   │   ├── padding.py
│   │           │   │   │   ├── pager.py
│   │           │   │   │   ├── palette.py
│   │           │   │   │   ├── panel.py
│   │           │   │   │   ├── pretty.py
│   │           │   │   │   ├── progress_bar.py
│   │           │   │   │   ├── progress.py
│   │           │   │   │   ├── prompt.py
│   │           │   │   │   ├── protocol.py
│   │           │   │   │   ├── py.typed
│   │           │   │   │   ├── region.py
│   │           │   │   │   ├── repr.py
│   │           │   │   │   ├── rule.py
│   │           │   │   │   ├── scope.py
│   │           │   │   │   ├── screen.py
│   │           │   │   │   ├── segment.py
│   │           │   │   │   ├── spinner.py
│   │           │   │   │   ├── status.py
│   │           │   │   │   ├── style.py
│   │           │   │   │   ├── styled.py
│   │           │   │   │   ├── syntax.py
│   │           │   │   │   ├── table.py
│   │           │   │   │   ├── terminal_theme.py
│   │           │   │   │   ├── text.py
│   │           │   │   │   ├── theme.py
│   │           │   │   │   ├── themes.py
│   │           │   │   │   ├── traceback.py
│   │           │   │   │   └── tree.py
│   │           │   │   ├── tomli
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── _parser.cpython-313.pyc
│   │           │   │   │   │   ├── _re.cpython-313.pyc
│   │           │   │   │   │   └── _types.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _parser.py
│   │           │   │   │   ├── _re.py
│   │           │   │   │   ├── _types.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   └── py.typed
│   │           │   │   ├── tomli_w
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   └── _writer.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _writer.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   └── py.typed
│   │           │   │   ├── truststore
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── _api.cpython-313.pyc
│   │           │   │   │   │   ├── _macos.cpython-313.pyc
│   │           │   │   │   │   ├── _openssl.cpython-313.pyc
│   │           │   │   │   │   ├── _ssl_constants.cpython-313.pyc
│   │           │   │   │   │   └── _windows.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _api.py
│   │           │   │   │   ├── _macos.py
│   │           │   │   │   ├── _openssl.py
│   │           │   │   │   ├── _ssl_constants.py
│   │           │   │   │   ├── _windows.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   └── py.typed
│   │           │   │   ├── urllib3
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── _collections.cpython-313.pyc
│   │           │   │   │   │   ├── _version.cpython-313.pyc
│   │           │   │   │   │   ├── connection.cpython-313.pyc
│   │           │   │   │   │   ├── connectionpool.cpython-313.pyc
│   │           │   │   │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   │   │   ├── fields.cpython-313.pyc
│   │           │   │   │   │   ├── filepost.cpython-313.pyc
│   │           │   │   │   │   ├── poolmanager.cpython-313.pyc
│   │           │   │   │   │   ├── request.cpython-313.pyc
│   │           │   │   │   │   └── response.cpython-313.pyc
│   │           │   │   │   ├── contrib
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   ├── _appengine_environ.cpython-313.pyc
│   │           │   │   │   │   │   ├── appengine.cpython-313.pyc
│   │           │   │   │   │   │   ├── ntlmpool.cpython-313.pyc
│   │           │   │   │   │   │   ├── pyopenssl.cpython-313.pyc
│   │           │   │   │   │   │   ├── securetransport.cpython-313.pyc
│   │           │   │   │   │   │   └── socks.cpython-313.pyc
│   │           │   │   │   │   ├── _securetransport
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── bindings.cpython-313.pyc
│   │           │   │   │   │   │   │   └── low_level.cpython-313.pyc
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   ├── bindings.py
│   │           │   │   │   │   │   └── low_level.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── _appengine_environ.py
│   │           │   │   │   │   ├── appengine.py
│   │           │   │   │   │   ├── ntlmpool.py
│   │           │   │   │   │   ├── pyopenssl.py
│   │           │   │   │   │   ├── securetransport.py
│   │           │   │   │   │   └── socks.py
│   │           │   │   │   ├── packages
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   └── six.cpython-313.pyc
│   │           │   │   │   │   ├── backports
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   │   ├── makefile.cpython-313.pyc
│   │           │   │   │   │   │   │   └── weakref_finalize.cpython-313.pyc
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   ├── makefile.py
│   │           │   │   │   │   │   └── weakref_finalize.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── six.py
│   │           │   │   │   ├── util
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   │   ├── connection.cpython-313.pyc
│   │           │   │   │   │   │   ├── proxy.cpython-313.pyc
│   │           │   │   │   │   │   ├── queue.cpython-313.pyc
│   │           │   │   │   │   │   ├── request.cpython-313.pyc
│   │           │   │   │   │   │   ├── response.cpython-313.pyc
│   │           │   │   │   │   │   ├── retry.cpython-313.pyc
│   │           │   │   │   │   │   ├── ssl_.cpython-313.pyc
│   │           │   │   │   │   │   ├── ssl_match_hostname.cpython-313.pyc
│   │           │   │   │   │   │   ├── ssltransport.cpython-313.pyc
│   │           │   │   │   │   │   ├── timeout.cpython-313.pyc
│   │           │   │   │   │   │   ├── url.cpython-313.pyc
│   │           │   │   │   │   │   └── wait.cpython-313.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── connection.py
│   │           │   │   │   │   ├── proxy.py
│   │           │   │   │   │   ├── queue.py
│   │           │   │   │   │   ├── request.py
│   │           │   │   │   │   ├── response.py
│   │           │   │   │   │   ├── retry.py
│   │           │   │   │   │   ├── ssl_.py
│   │           │   │   │   │   ├── ssl_match_hostname.py
│   │           │   │   │   │   ├── ssltransport.py
│   │           │   │   │   │   ├── timeout.py
│   │           │   │   │   │   ├── url.py
│   │           │   │   │   │   └── wait.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _collections.py
│   │           │   │   │   ├── _version.py
│   │           │   │   │   ├── connection.py
│   │           │   │   │   ├── connectionpool.py
│   │           │   │   │   ├── exceptions.py
│   │           │   │   │   ├── fields.py
│   │           │   │   │   ├── filepost.py
│   │           │   │   │   ├── LICENSE.txt
│   │           │   │   │   ├── poolmanager.py
│   │           │   │   │   ├── request.py
│   │           │   │   │   └── response.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── README.rst
│   │           │   │   └── vendor.txt
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── __pip-runner__.py
│   │           │   └── py.typed
│   │           ├── pip-25.3.dist-info
│   │           │   ├── licenses
│   │           │   │   ├── src
│   │           │   │   │   └── pip
│   │           │   │   │       └── _vendor
│   │           │   │   │           ├── cachecontrol
│   │           │   │   │           │   └── LICENSE.txt
│   │           │   │   │           ├── certifi
│   │           │   │   │           │   └── LICENSE
│   │           │   │   │           ├── dependency_groups
│   │           │   │   │           │   └── LICENSE.txt
│   │           │   │   │           ├── distlib
│   │           │   │   │           │   └── LICENSE.txt
│   │           │   │   │           ├── distro
│   │           │   │   │           │   └── LICENSE
│   │           │   │   │           ├── idna
│   │           │   │   │           │   └── LICENSE.md
│   │           │   │   │           ├── msgpack
│   │           │   │   │           │   └── COPYING
│   │           │   │   │           ├── packaging
│   │           │   │   │           │   ├── LICENSE
│   │           │   │   │           │   ├── LICENSE.APACHE
│   │           │   │   │           │   └── LICENSE.BSD
│   │           │   │   │           ├── pkg_resources
│   │           │   │   │           │   └── LICENSE
│   │           │   │   │           ├── platformdirs
│   │           │   │   │           │   └── LICENSE
│   │           │   │   │           ├── pygments
│   │           │   │   │           │   └── LICENSE
│   │           │   │   │           ├── pyproject_hooks
│   │           │   │   │           │   └── LICENSE
│   │           │   │   │           ├── requests
│   │           │   │   │           │   └── LICENSE
│   │           │   │   │           ├── resolvelib
│   │           │   │   │           │   └── LICENSE
│   │           │   │   │           ├── rich
│   │           │   │   │           │   └── LICENSE
│   │           │   │   │           ├── tomli
│   │           │   │   │           │   └── LICENSE
│   │           │   │   │           ├── tomli_w
│   │           │   │   │           │   └── LICENSE
│   │           │   │   │           ├── truststore
│   │           │   │   │           │   └── LICENSE
│   │           │   │   │           └── urllib3
│   │           │   │   │               └── LICENSE.txt
│   │           │   │   ├── AUTHORS.txt
│   │           │   │   └── LICENSE.txt
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   └── WHEEL
│   │           ├── pluggy
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── _callers.cpython-313.pyc
│   │           │   │   ├── _hooks.cpython-313.pyc
│   │           │   │   ├── _manager.cpython-313.pyc
│   │           │   │   ├── _result.cpython-313.pyc
│   │           │   │   ├── _tracing.cpython-313.pyc
│   │           │   │   ├── _version.cpython-313.pyc
│   │           │   │   └── _warnings.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── _callers.py
│   │           │   ├── _hooks.py
│   │           │   ├── _manager.py
│   │           │   ├── _result.py
│   │           │   ├── _tracing.py
│   │           │   ├── _version.py
│   │           │   ├── _warnings.py
│   │           │   └── py.typed
│   │           ├── pluggy-1.6.0.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── pydantic
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── _migration.cpython-313.pyc
│   │           │   │   ├── alias_generators.cpython-313.pyc
│   │           │   │   ├── aliases.cpython-313.pyc
│   │           │   │   ├── annotated_handlers.cpython-313.pyc
│   │           │   │   ├── class_validators.cpython-313.pyc
│   │           │   │   ├── color.cpython-313.pyc
│   │           │   │   ├── config.cpython-313.pyc
│   │           │   │   ├── dataclasses.cpython-313.pyc
│   │           │   │   ├── datetime_parse.cpython-313.pyc
│   │           │   │   ├── decorator.cpython-313.pyc
│   │           │   │   ├── env_settings.cpython-313.pyc
│   │           │   │   ├── error_wrappers.cpython-313.pyc
│   │           │   │   ├── errors.cpython-313.pyc
│   │           │   │   ├── fields.cpython-313.pyc
│   │           │   │   ├── functional_serializers.cpython-313.pyc
│   │           │   │   ├── functional_validators.cpython-313.pyc
│   │           │   │   ├── generics.cpython-313.pyc
│   │           │   │   ├── json_schema.cpython-313.pyc
│   │           │   │   ├── json.cpython-313.pyc
│   │           │   │   ├── main.cpython-313.pyc
│   │           │   │   ├── mypy.cpython-313.pyc
│   │           │   │   ├── networks.cpython-313.pyc
│   │           │   │   ├── parse.cpython-313.pyc
│   │           │   │   ├── root_model.cpython-313.pyc
│   │           │   │   ├── schema.cpython-313.pyc
│   │           │   │   ├── tools.cpython-313.pyc
│   │           │   │   ├── type_adapter.cpython-313.pyc
│   │           │   │   ├── types.cpython-313.pyc
│   │           │   │   ├── typing.cpython-313.pyc
│   │           │   │   ├── utils.cpython-313.pyc
│   │           │   │   ├── validate_call_decorator.cpython-313.pyc
│   │           │   │   ├── validators.cpython-313.pyc
│   │           │   │   ├── version.cpython-313.pyc
│   │           │   │   └── warnings.cpython-313.pyc
│   │           │   ├── _internal
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _config.cpython-313.pyc
│   │           │   │   │   ├── _core_metadata.cpython-313.pyc
│   │           │   │   │   ├── _core_utils.cpython-313.pyc
│   │           │   │   │   ├── _dataclasses.cpython-313.pyc
│   │           │   │   │   ├── _decorators_v1.cpython-313.pyc
│   │           │   │   │   ├── _decorators.cpython-313.pyc
│   │           │   │   │   ├── _discriminated_union.cpython-313.pyc
│   │           │   │   │   ├── _docs_extraction.cpython-313.pyc
│   │           │   │   │   ├── _fields.cpython-313.pyc
│   │           │   │   │   ├── _forward_ref.cpython-313.pyc
│   │           │   │   │   ├── _generate_schema.cpython-313.pyc
│   │           │   │   │   ├── _generics.cpython-313.pyc
│   │           │   │   │   ├── _git.cpython-313.pyc
│   │           │   │   │   ├── _import_utils.cpython-313.pyc
│   │           │   │   │   ├── _internal_dataclass.cpython-313.pyc
│   │           │   │   │   ├── _known_annotated_metadata.cpython-313.pyc
│   │           │   │   │   ├── _mock_val_ser.cpython-313.pyc
│   │           │   │   │   ├── _model_construction.cpython-313.pyc
│   │           │   │   │   ├── _namespace_utils.cpython-313.pyc
│   │           │   │   │   ├── _repr.cpython-313.pyc
│   │           │   │   │   ├── _schema_gather.cpython-313.pyc
│   │           │   │   │   ├── _schema_generation_shared.cpython-313.pyc
│   │           │   │   │   ├── _serializers.cpython-313.pyc
│   │           │   │   │   ├── _signature.cpython-313.pyc
│   │           │   │   │   ├── _typing_extra.cpython-313.pyc
│   │           │   │   │   ├── _utils.cpython-313.pyc
│   │           │   │   │   ├── _validate_call.cpython-313.pyc
│   │           │   │   │   └── _validators.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _config.py
│   │           │   │   ├── _core_metadata.py
│   │           │   │   ├── _core_utils.py
│   │           │   │   ├── _dataclasses.py
│   │           │   │   ├── _decorators_v1.py
│   │           │   │   ├── _decorators.py
│   │           │   │   ├── _discriminated_union.py
│   │           │   │   ├── _docs_extraction.py
│   │           │   │   ├── _fields.py
│   │           │   │   ├── _forward_ref.py
│   │           │   │   ├── _generate_schema.py
│   │           │   │   ├── _generics.py
│   │           │   │   ├── _git.py
│   │           │   │   ├── _import_utils.py
│   │           │   │   ├── _internal_dataclass.py
│   │           │   │   ├── _known_annotated_metadata.py
│   │           │   │   ├── _mock_val_ser.py
│   │           │   │   ├── _model_construction.py
│   │           │   │   ├── _namespace_utils.py
│   │           │   │   ├── _repr.py
│   │           │   │   ├── _schema_gather.py
│   │           │   │   ├── _schema_generation_shared.py
│   │           │   │   ├── _serializers.py
│   │           │   │   ├── _signature.py
│   │           │   │   ├── _typing_extra.py
│   │           │   │   ├── _utils.py
│   │           │   │   ├── _validate_call.py
│   │           │   │   └── _validators.py
│   │           │   ├── deprecated
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── class_validators.cpython-313.pyc
│   │           │   │   │   ├── config.cpython-313.pyc
│   │           │   │   │   ├── copy_internals.cpython-313.pyc
│   │           │   │   │   ├── decorator.cpython-313.pyc
│   │           │   │   │   ├── json.cpython-313.pyc
│   │           │   │   │   ├── parse.cpython-313.pyc
│   │           │   │   │   └── tools.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── class_validators.py
│   │           │   │   ├── config.py
│   │           │   │   ├── copy_internals.py
│   │           │   │   ├── decorator.py
│   │           │   │   ├── json.py
│   │           │   │   ├── parse.py
│   │           │   │   └── tools.py
│   │           │   ├── experimental
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── arguments_schema.cpython-313.pyc
│   │           │   │   │   ├── missing_sentinel.cpython-313.pyc
│   │           │   │   │   └── pipeline.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── arguments_schema.py
│   │           │   │   ├── missing_sentinel.py
│   │           │   │   └── pipeline.py
│   │           │   ├── plugin
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _loader.cpython-313.pyc
│   │           │   │   │   └── _schema_validator.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _loader.py
│   │           │   │   └── _schema_validator.py
│   │           │   ├── v1
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _hypothesis_plugin.cpython-313.pyc
│   │           │   │   │   ├── annotated_types.cpython-313.pyc
│   │           │   │   │   ├── class_validators.cpython-313.pyc
│   │           │   │   │   ├── color.cpython-313.pyc
│   │           │   │   │   ├── config.cpython-313.pyc
│   │           │   │   │   ├── dataclasses.cpython-313.pyc
│   │           │   │   │   ├── datetime_parse.cpython-313.pyc
│   │           │   │   │   ├── decorator.cpython-313.pyc
│   │           │   │   │   ├── env_settings.cpython-313.pyc
│   │           │   │   │   ├── error_wrappers.cpython-313.pyc
│   │           │   │   │   ├── errors.cpython-313.pyc
│   │           │   │   │   ├── fields.cpython-313.pyc
│   │           │   │   │   ├── generics.cpython-313.pyc
│   │           │   │   │   ├── json.cpython-313.pyc
│   │           │   │   │   ├── main.cpython-313.pyc
│   │           │   │   │   ├── mypy.cpython-313.pyc
│   │           │   │   │   ├── networks.cpython-313.pyc
│   │           │   │   │   ├── parse.cpython-313.pyc
│   │           │   │   │   ├── schema.cpython-313.pyc
│   │           │   │   │   ├── tools.cpython-313.pyc
│   │           │   │   │   ├── types.cpython-313.pyc
│   │           │   │   │   ├── typing.cpython-313.pyc
│   │           │   │   │   ├── utils.cpython-313.pyc
│   │           │   │   │   ├── validators.cpython-313.pyc
│   │           │   │   │   └── version.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _hypothesis_plugin.py
│   │           │   │   ├── annotated_types.py
│   │           │   │   ├── class_validators.py
│   │           │   │   ├── color.py
│   │           │   │   ├── config.py
│   │           │   │   ├── dataclasses.py
│   │           │   │   ├── datetime_parse.py
│   │           │   │   ├── decorator.py
│   │           │   │   ├── env_settings.py
│   │           │   │   ├── error_wrappers.py
│   │           │   │   ├── errors.py
│   │           │   │   ├── fields.py
│   │           │   │   ├── generics.py
│   │           │   │   ├── json.py
│   │           │   │   ├── main.py
│   │           │   │   ├── mypy.py
│   │           │   │   ├── networks.py
│   │           │   │   ├── parse.py
│   │           │   │   ├── py.typed
│   │           │   │   ├── schema.py
│   │           │   │   ├── tools.py
│   │           │   │   ├── types.py
│   │           │   │   ├── typing.py
│   │           │   │   ├── utils.py
│   │           │   │   ├── validators.py
│   │           │   │   └── version.py
│   │           │   ├── __init__.py
│   │           │   ├── _migration.py
│   │           │   ├── alias_generators.py
│   │           │   ├── aliases.py
│   │           │   ├── annotated_handlers.py
│   │           │   ├── class_validators.py
│   │           │   ├── color.py
│   │           │   ├── config.py
│   │           │   ├── dataclasses.py
│   │           │   ├── datetime_parse.py
│   │           │   ├── decorator.py
│   │           │   ├── env_settings.py
│   │           │   ├── error_wrappers.py
│   │           │   ├── errors.py
│   │           │   ├── fields.py
│   │           │   ├── functional_serializers.py
│   │           │   ├── functional_validators.py
│   │           │   ├── generics.py
│   │           │   ├── json_schema.py
│   │           │   ├── json.py
│   │           │   ├── main.py
│   │           │   ├── mypy.py
│   │           │   ├── networks.py
│   │           │   ├── parse.py
│   │           │   ├── py.typed
│   │           │   ├── root_model.py
│   │           │   ├── schema.py
│   │           │   ├── tools.py
│   │           │   ├── type_adapter.py
│   │           │   ├── types.py
│   │           │   ├── typing.py
│   │           │   ├── utils.py
│   │           │   ├── validate_call_decorator.py
│   │           │   ├── validators.py
│   │           │   ├── version.py
│   │           │   └── warnings.py
│   │           ├── pydantic_core
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   └── core_schema.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── _pydantic_core.cpython-313-darwin.so
│   │           │   ├── _pydantic_core.pyi
│   │           │   ├── core_schema.py
│   │           │   └── py.typed
│   │           ├── pydantic_core-2.41.5.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── pydantic-2.12.5.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── pygments
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── __main__.cpython-313.pyc
│   │           │   │   ├── cmdline.cpython-313.pyc
│   │           │   │   ├── console.cpython-313.pyc
│   │           │   │   ├── filter.cpython-313.pyc
│   │           │   │   ├── formatter.cpython-313.pyc
│   │           │   │   ├── lexer.cpython-313.pyc
│   │           │   │   ├── modeline.cpython-313.pyc
│   │           │   │   ├── plugin.cpython-313.pyc
│   │           │   │   ├── regexopt.cpython-313.pyc
│   │           │   │   ├── scanner.cpython-313.pyc
│   │           │   │   ├── sphinxext.cpython-313.pyc
│   │           │   │   ├── style.cpython-313.pyc
│   │           │   │   ├── token.cpython-313.pyc
│   │           │   │   ├── unistring.cpython-313.pyc
│   │           │   │   └── util.cpython-313.pyc
│   │           │   ├── filters
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-313.pyc
│   │           │   │   └── __init__.py
│   │           │   ├── formatters
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _mapping.cpython-313.pyc
│   │           │   │   │   ├── bbcode.cpython-313.pyc
│   │           │   │   │   ├── groff.cpython-313.pyc
│   │           │   │   │   ├── html.cpython-313.pyc
│   │           │   │   │   ├── img.cpython-313.pyc
│   │           │   │   │   ├── irc.cpython-313.pyc
│   │           │   │   │   ├── latex.cpython-313.pyc
│   │           │   │   │   ├── other.cpython-313.pyc
│   │           │   │   │   ├── pangomarkup.cpython-313.pyc
│   │           │   │   │   ├── rtf.cpython-313.pyc
│   │           │   │   │   ├── svg.cpython-313.pyc
│   │           │   │   │   ├── terminal.cpython-313.pyc
│   │           │   │   │   └── terminal256.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _mapping.py
│   │           │   │   ├── bbcode.py
│   │           │   │   ├── groff.py
│   │           │   │   ├── html.py
│   │           │   │   ├── img.py
│   │           │   │   ├── irc.py
│   │           │   │   ├── latex.py
│   │           │   │   ├── other.py
│   │           │   │   ├── pangomarkup.py
│   │           │   │   ├── rtf.py
│   │           │   │   ├── svg.py
│   │           │   │   ├── terminal.py
│   │           │   │   └── terminal256.py
│   │           │   ├── lexers
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _ada_builtins.cpython-313.pyc
│   │           │   │   │   ├── _asy_builtins.cpython-313.pyc
│   │           │   │   │   ├── _cl_builtins.cpython-313.pyc
│   │           │   │   │   ├── _cocoa_builtins.cpython-313.pyc
│   │           │   │   │   ├── _csound_builtins.cpython-313.pyc
│   │           │   │   │   ├── _css_builtins.cpython-313.pyc
│   │           │   │   │   ├── _googlesql_builtins.cpython-313.pyc
│   │           │   │   │   ├── _julia_builtins.cpython-313.pyc
│   │           │   │   │   ├── _lasso_builtins.cpython-313.pyc
│   │           │   │   │   ├── _lilypond_builtins.cpython-313.pyc
│   │           │   │   │   ├── _lua_builtins.cpython-313.pyc
│   │           │   │   │   ├── _luau_builtins.cpython-313.pyc
│   │           │   │   │   ├── _mapping.cpython-313.pyc
│   │           │   │   │   ├── _mql_builtins.cpython-313.pyc
│   │           │   │   │   ├── _mysql_builtins.cpython-313.pyc
│   │           │   │   │   ├── _openedge_builtins.cpython-313.pyc
│   │           │   │   │   ├── _php_builtins.cpython-313.pyc
│   │           │   │   │   ├── _postgres_builtins.cpython-313.pyc
│   │           │   │   │   ├── _qlik_builtins.cpython-313.pyc
│   │           │   │   │   ├── _scheme_builtins.cpython-313.pyc
│   │           │   │   │   ├── _scilab_builtins.cpython-313.pyc
│   │           │   │   │   ├── _sourcemod_builtins.cpython-313.pyc
│   │           │   │   │   ├── _sql_builtins.cpython-313.pyc
│   │           │   │   │   ├── _stan_builtins.cpython-313.pyc
│   │           │   │   │   ├── _stata_builtins.cpython-313.pyc
│   │           │   │   │   ├── _tsql_builtins.cpython-313.pyc
│   │           │   │   │   ├── _usd_builtins.cpython-313.pyc
│   │           │   │   │   ├── _vbscript_builtins.cpython-313.pyc
│   │           │   │   │   ├── _vim_builtins.cpython-313.pyc
│   │           │   │   │   ├── actionscript.cpython-313.pyc
│   │           │   │   │   ├── ada.cpython-313.pyc
│   │           │   │   │   ├── agile.cpython-313.pyc
│   │           │   │   │   ├── algebra.cpython-313.pyc
│   │           │   │   │   ├── ambient.cpython-313.pyc
│   │           │   │   │   ├── amdgpu.cpython-313.pyc
│   │           │   │   │   ├── ampl.cpython-313.pyc
│   │           │   │   │   ├── apdlexer.cpython-313.pyc
│   │           │   │   │   ├── apl.cpython-313.pyc
│   │           │   │   │   ├── archetype.cpython-313.pyc
│   │           │   │   │   ├── arrow.cpython-313.pyc
│   │           │   │   │   ├── arturo.cpython-313.pyc
│   │           │   │   │   ├── asc.cpython-313.pyc
│   │           │   │   │   ├── asm.cpython-313.pyc
│   │           │   │   │   ├── asn1.cpython-313.pyc
│   │           │   │   │   ├── automation.cpython-313.pyc
│   │           │   │   │   ├── bare.cpython-313.pyc
│   │           │   │   │   ├── basic.cpython-313.pyc
│   │           │   │   │   ├── bdd.cpython-313.pyc
│   │           │   │   │   ├── berry.cpython-313.pyc
│   │           │   │   │   ├── bibtex.cpython-313.pyc
│   │           │   │   │   ├── blueprint.cpython-313.pyc
│   │           │   │   │   ├── boa.cpython-313.pyc
│   │           │   │   │   ├── bqn.cpython-313.pyc
│   │           │   │   │   ├── business.cpython-313.pyc
│   │           │   │   │   ├── c_cpp.cpython-313.pyc
│   │           │   │   │   ├── c_like.cpython-313.pyc
│   │           │   │   │   ├── capnproto.cpython-313.pyc
│   │           │   │   │   ├── carbon.cpython-313.pyc
│   │           │   │   │   ├── cddl.cpython-313.pyc
│   │           │   │   │   ├── chapel.cpython-313.pyc
│   │           │   │   │   ├── clean.cpython-313.pyc
│   │           │   │   │   ├── codeql.cpython-313.pyc
│   │           │   │   │   ├── comal.cpython-313.pyc
│   │           │   │   │   ├── compiled.cpython-313.pyc
│   │           │   │   │   ├── configs.cpython-313.pyc
│   │           │   │   │   ├── console.cpython-313.pyc
│   │           │   │   │   ├── cplint.cpython-313.pyc
│   │           │   │   │   ├── crystal.cpython-313.pyc
│   │           │   │   │   ├── csound.cpython-313.pyc
│   │           │   │   │   ├── css.cpython-313.pyc
│   │           │   │   │   ├── d.cpython-313.pyc
│   │           │   │   │   ├── dalvik.cpython-313.pyc
│   │           │   │   │   ├── data.cpython-313.pyc
│   │           │   │   │   ├── dax.cpython-313.pyc
│   │           │   │   │   ├── devicetree.cpython-313.pyc
│   │           │   │   │   ├── diff.cpython-313.pyc
│   │           │   │   │   ├── dns.cpython-313.pyc
│   │           │   │   │   ├── dotnet.cpython-313.pyc
│   │           │   │   │   ├── dsls.cpython-313.pyc
│   │           │   │   │   ├── dylan.cpython-313.pyc
│   │           │   │   │   ├── ecl.cpython-313.pyc
│   │           │   │   │   ├── eiffel.cpython-313.pyc
│   │           │   │   │   ├── elm.cpython-313.pyc
│   │           │   │   │   ├── elpi.cpython-313.pyc
│   │           │   │   │   ├── email.cpython-313.pyc
│   │           │   │   │   ├── erlang.cpython-313.pyc
│   │           │   │   │   ├── esoteric.cpython-313.pyc
│   │           │   │   │   ├── ezhil.cpython-313.pyc
│   │           │   │   │   ├── factor.cpython-313.pyc
│   │           │   │   │   ├── fantom.cpython-313.pyc
│   │           │   │   │   ├── felix.cpython-313.pyc
│   │           │   │   │   ├── fift.cpython-313.pyc
│   │           │   │   │   ├── floscript.cpython-313.pyc
│   │           │   │   │   ├── forth.cpython-313.pyc
│   │           │   │   │   ├── fortran.cpython-313.pyc
│   │           │   │   │   ├── foxpro.cpython-313.pyc
│   │           │   │   │   ├── freefem.cpython-313.pyc
│   │           │   │   │   ├── func.cpython-313.pyc
│   │           │   │   │   ├── functional.cpython-313.pyc
│   │           │   │   │   ├── futhark.cpython-313.pyc
│   │           │   │   │   ├── gcodelexer.cpython-313.pyc
│   │           │   │   │   ├── gdscript.cpython-313.pyc
│   │           │   │   │   ├── gleam.cpython-313.pyc
│   │           │   │   │   ├── go.cpython-313.pyc
│   │           │   │   │   ├── grammar_notation.cpython-313.pyc
│   │           │   │   │   ├── graph.cpython-313.pyc
│   │           │   │   │   ├── graphics.cpython-313.pyc
│   │           │   │   │   ├── graphql.cpython-313.pyc
│   │           │   │   │   ├── graphviz.cpython-313.pyc
│   │           │   │   │   ├── gsql.cpython-313.pyc
│   │           │   │   │   ├── hare.cpython-313.pyc
│   │           │   │   │   ├── haskell.cpython-313.pyc
│   │           │   │   │   ├── haxe.cpython-313.pyc
│   │           │   │   │   ├── hdl.cpython-313.pyc
│   │           │   │   │   ├── hexdump.cpython-313.pyc
│   │           │   │   │   ├── html.cpython-313.pyc
│   │           │   │   │   ├── idl.cpython-313.pyc
│   │           │   │   │   ├── igor.cpython-313.pyc
│   │           │   │   │   ├── inferno.cpython-313.pyc
│   │           │   │   │   ├── installers.cpython-313.pyc
│   │           │   │   │   ├── int_fiction.cpython-313.pyc
│   │           │   │   │   ├── iolang.cpython-313.pyc
│   │           │   │   │   ├── j.cpython-313.pyc
│   │           │   │   │   ├── javascript.cpython-313.pyc
│   │           │   │   │   ├── jmespath.cpython-313.pyc
│   │           │   │   │   ├── jslt.cpython-313.pyc
│   │           │   │   │   ├── json5.cpython-313.pyc
│   │           │   │   │   ├── jsonnet.cpython-313.pyc
│   │           │   │   │   ├── jsx.cpython-313.pyc
│   │           │   │   │   ├── julia.cpython-313.pyc
│   │           │   │   │   ├── jvm.cpython-313.pyc
│   │           │   │   │   ├── kuin.cpython-313.pyc
│   │           │   │   │   ├── kusto.cpython-313.pyc
│   │           │   │   │   ├── ldap.cpython-313.pyc
│   │           │   │   │   ├── lean.cpython-313.pyc
│   │           │   │   │   ├── lilypond.cpython-313.pyc
│   │           │   │   │   ├── lisp.cpython-313.pyc
│   │           │   │   │   ├── macaulay2.cpython-313.pyc
│   │           │   │   │   ├── make.cpython-313.pyc
│   │           │   │   │   ├── maple.cpython-313.pyc
│   │           │   │   │   ├── markup.cpython-313.pyc
│   │           │   │   │   ├── math.cpython-313.pyc
│   │           │   │   │   ├── matlab.cpython-313.pyc
│   │           │   │   │   ├── maxima.cpython-313.pyc
│   │           │   │   │   ├── meson.cpython-313.pyc
│   │           │   │   │   ├── mime.cpython-313.pyc
│   │           │   │   │   ├── minecraft.cpython-313.pyc
│   │           │   │   │   ├── mips.cpython-313.pyc
│   │           │   │   │   ├── ml.cpython-313.pyc
│   │           │   │   │   ├── modeling.cpython-313.pyc
│   │           │   │   │   ├── modula2.cpython-313.pyc
│   │           │   │   │   ├── mojo.cpython-313.pyc
│   │           │   │   │   ├── monte.cpython-313.pyc
│   │           │   │   │   ├── mosel.cpython-313.pyc
│   │           │   │   │   ├── ncl.cpython-313.pyc
│   │           │   │   │   ├── nimrod.cpython-313.pyc
│   │           │   │   │   ├── nit.cpython-313.pyc
│   │           │   │   │   ├── nix.cpython-313.pyc
│   │           │   │   │   ├── numbair.cpython-313.pyc
│   │           │   │   │   ├── oberon.cpython-313.pyc
│   │           │   │   │   ├── objective.cpython-313.pyc
│   │           │   │   │   ├── ooc.cpython-313.pyc
│   │           │   │   │   ├── openscad.cpython-313.pyc
│   │           │   │   │   ├── other.cpython-313.pyc
│   │           │   │   │   ├── parasail.cpython-313.pyc
│   │           │   │   │   ├── parsers.cpython-313.pyc
│   │           │   │   │   ├── pascal.cpython-313.pyc
│   │           │   │   │   ├── pawn.cpython-313.pyc
│   │           │   │   │   ├── pddl.cpython-313.pyc
│   │           │   │   │   ├── perl.cpython-313.pyc
│   │           │   │   │   ├── phix.cpython-313.pyc
│   │           │   │   │   ├── php.cpython-313.pyc
│   │           │   │   │   ├── pointless.cpython-313.pyc
│   │           │   │   │   ├── pony.cpython-313.pyc
│   │           │   │   │   ├── praat.cpython-313.pyc
│   │           │   │   │   ├── procfile.cpython-313.pyc
│   │           │   │   │   ├── prolog.cpython-313.pyc
│   │           │   │   │   ├── promql.cpython-313.pyc
│   │           │   │   │   ├── prql.cpython-313.pyc
│   │           │   │   │   ├── ptx.cpython-313.pyc
│   │           │   │   │   ├── python.cpython-313.pyc
│   │           │   │   │   ├── q.cpython-313.pyc
│   │           │   │   │   ├── qlik.cpython-313.pyc
│   │           │   │   │   ├── qvt.cpython-313.pyc
│   │           │   │   │   ├── r.cpython-313.pyc
│   │           │   │   │   ├── rdf.cpython-313.pyc
│   │           │   │   │   ├── rebol.cpython-313.pyc
│   │           │   │   │   ├── rego.cpython-313.pyc
│   │           │   │   │   ├── resource.cpython-313.pyc
│   │           │   │   │   ├── ride.cpython-313.pyc
│   │           │   │   │   ├── rita.cpython-313.pyc
│   │           │   │   │   ├── rnc.cpython-313.pyc
│   │           │   │   │   ├── roboconf.cpython-313.pyc
│   │           │   │   │   ├── robotframework.cpython-313.pyc
│   │           │   │   │   ├── ruby.cpython-313.pyc
│   │           │   │   │   ├── rust.cpython-313.pyc
│   │           │   │   │   ├── sas.cpython-313.pyc
│   │           │   │   │   ├── savi.cpython-313.pyc
│   │           │   │   │   ├── scdoc.cpython-313.pyc
│   │           │   │   │   ├── scripting.cpython-313.pyc
│   │           │   │   │   ├── sgf.cpython-313.pyc
│   │           │   │   │   ├── shell.cpython-313.pyc
│   │           │   │   │   ├── sieve.cpython-313.pyc
│   │           │   │   │   ├── slash.cpython-313.pyc
│   │           │   │   │   ├── smalltalk.cpython-313.pyc
│   │           │   │   │   ├── smithy.cpython-313.pyc
│   │           │   │   │   ├── smv.cpython-313.pyc
│   │           │   │   │   ├── snobol.cpython-313.pyc
│   │           │   │   │   ├── solidity.cpython-313.pyc
│   │           │   │   │   ├── soong.cpython-313.pyc
│   │           │   │   │   ├── sophia.cpython-313.pyc
│   │           │   │   │   ├── special.cpython-313.pyc
│   │           │   │   │   ├── spice.cpython-313.pyc
│   │           │   │   │   ├── sql.cpython-313.pyc
│   │           │   │   │   ├── srcinfo.cpython-313.pyc
│   │           │   │   │   ├── stata.cpython-313.pyc
│   │           │   │   │   ├── supercollider.cpython-313.pyc
│   │           │   │   │   ├── tablegen.cpython-313.pyc
│   │           │   │   │   ├── tact.cpython-313.pyc
│   │           │   │   │   ├── tal.cpython-313.pyc
│   │           │   │   │   ├── tcl.cpython-313.pyc
│   │           │   │   │   ├── teal.cpython-313.pyc
│   │           │   │   │   ├── templates.cpython-313.pyc
│   │           │   │   │   ├── teraterm.cpython-313.pyc
│   │           │   │   │   ├── testing.cpython-313.pyc
│   │           │   │   │   ├── text.cpython-313.pyc
│   │           │   │   │   ├── textedit.cpython-313.pyc
│   │           │   │   │   ├── textfmts.cpython-313.pyc
│   │           │   │   │   ├── theorem.cpython-313.pyc
│   │           │   │   │   ├── thingsdb.cpython-313.pyc
│   │           │   │   │   ├── tlb.cpython-313.pyc
│   │           │   │   │   ├── tls.cpython-313.pyc
│   │           │   │   │   ├── tnt.cpython-313.pyc
│   │           │   │   │   ├── trafficscript.cpython-313.pyc
│   │           │   │   │   ├── typoscript.cpython-313.pyc
│   │           │   │   │   ├── typst.cpython-313.pyc
│   │           │   │   │   ├── ul4.cpython-313.pyc
│   │           │   │   │   ├── unicon.cpython-313.pyc
│   │           │   │   │   ├── urbi.cpython-313.pyc
│   │           │   │   │   ├── usd.cpython-313.pyc
│   │           │   │   │   ├── varnish.cpython-313.pyc
│   │           │   │   │   ├── verification.cpython-313.pyc
│   │           │   │   │   ├── verifpal.cpython-313.pyc
│   │           │   │   │   ├── vip.cpython-313.pyc
│   │           │   │   │   ├── vyper.cpython-313.pyc
│   │           │   │   │   ├── web.cpython-313.pyc
│   │           │   │   │   ├── webassembly.cpython-313.pyc
│   │           │   │   │   ├── webidl.cpython-313.pyc
│   │           │   │   │   ├── webmisc.cpython-313.pyc
│   │           │   │   │   ├── wgsl.cpython-313.pyc
│   │           │   │   │   ├── whiley.cpython-313.pyc
│   │           │   │   │   ├── wowtoc.cpython-313.pyc
│   │           │   │   │   ├── wren.cpython-313.pyc
│   │           │   │   │   ├── x10.cpython-313.pyc
│   │           │   │   │   ├── xorg.cpython-313.pyc
│   │           │   │   │   ├── yang.cpython-313.pyc
│   │           │   │   │   ├── yara.cpython-313.pyc
│   │           │   │   │   └── zig.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _ada_builtins.py
│   │           │   │   ├── _asy_builtins.py
│   │           │   │   ├── _cl_builtins.py
│   │           │   │   ├── _cocoa_builtins.py
│   │           │   │   ├── _csound_builtins.py
│   │           │   │   ├── _css_builtins.py
│   │           │   │   ├── _googlesql_builtins.py
│   │           │   │   ├── _julia_builtins.py
│   │           │   │   ├── _lasso_builtins.py
│   │           │   │   ├── _lilypond_builtins.py
│   │           │   │   ├── _lua_builtins.py
│   │           │   │   ├── _luau_builtins.py
│   │           │   │   ├── _mapping.py
│   │           │   │   ├── _mql_builtins.py
│   │           │   │   ├── _mysql_builtins.py
│   │           │   │   ├── _openedge_builtins.py
│   │           │   │   ├── _php_builtins.py
│   │           │   │   ├── _postgres_builtins.py
│   │           │   │   ├── _qlik_builtins.py
│   │           │   │   ├── _scheme_builtins.py
│   │           │   │   ├── _scilab_builtins.py
│   │           │   │   ├── _sourcemod_builtins.py
│   │           │   │   ├── _sql_builtins.py
│   │           │   │   ├── _stan_builtins.py
│   │           │   │   ├── _stata_builtins.py
│   │           │   │   ├── _tsql_builtins.py
│   │           │   │   ├── _usd_builtins.py
│   │           │   │   ├── _vbscript_builtins.py
│   │           │   │   ├── _vim_builtins.py
│   │           │   │   ├── actionscript.py
│   │           │   │   ├── ada.py
│   │           │   │   ├── agile.py
│   │           │   │   ├── algebra.py
│   │           │   │   ├── ambient.py
│   │           │   │   ├── amdgpu.py
│   │           │   │   ├── ampl.py
│   │           │   │   ├── apdlexer.py
│   │           │   │   ├── apl.py
│   │           │   │   ├── archetype.py
│   │           │   │   ├── arrow.py
│   │           │   │   ├── arturo.py
│   │           │   │   ├── asc.py
│   │           │   │   ├── asm.py
│   │           │   │   ├── asn1.py
│   │           │   │   ├── automation.py
│   │           │   │   ├── bare.py
│   │           │   │   ├── basic.py
│   │           │   │   ├── bdd.py
│   │           │   │   ├── berry.py
│   │           │   │   ├── bibtex.py
│   │           │   │   ├── blueprint.py
│   │           │   │   ├── boa.py
│   │           │   │   ├── bqn.py
│   │           │   │   ├── business.py
│   │           │   │   ├── c_cpp.py
│   │           │   │   ├── c_like.py
│   │           │   │   ├── capnproto.py
│   │           │   │   ├── carbon.py
│   │           │   │   ├── cddl.py
│   │           │   │   ├── chapel.py
│   │           │   │   ├── clean.py
│   │           │   │   ├── codeql.py
│   │           │   │   ├── comal.py
│   │           │   │   ├── compiled.py
│   │           │   │   ├── configs.py
│   │           │   │   ├── console.py
│   │           │   │   ├── cplint.py
│   │           │   │   ├── crystal.py
│   │           │   │   ├── csound.py
│   │           │   │   ├── css.py
│   │           │   │   ├── d.py
│   │           │   │   ├── dalvik.py
│   │           │   │   ├── data.py
│   │           │   │   ├── dax.py
│   │           │   │   ├── devicetree.py
│   │           │   │   ├── diff.py
│   │           │   │   ├── dns.py
│   │           │   │   ├── dotnet.py
│   │           │   │   ├── dsls.py
│   │           │   │   ├── dylan.py
│   │           │   │   ├── ecl.py
│   │           │   │   ├── eiffel.py
│   │           │   │   ├── elm.py
│   │           │   │   ├── elpi.py
│   │           │   │   ├── email.py
│   │           │   │   ├── erlang.py
│   │           │   │   ├── esoteric.py
│   │           │   │   ├── ezhil.py
│   │           │   │   ├── factor.py
│   │           │   │   ├── fantom.py
│   │           │   │   ├── felix.py
│   │           │   │   ├── fift.py
│   │           │   │   ├── floscript.py
│   │           │   │   ├── forth.py
│   │           │   │   ├── fortran.py
│   │           │   │   ├── foxpro.py
│   │           │   │   ├── freefem.py
│   │           │   │   ├── func.py
│   │           │   │   ├── functional.py
│   │           │   │   ├── futhark.py
│   │           │   │   ├── gcodelexer.py
│   │           │   │   ├── gdscript.py
│   │           │   │   ├── gleam.py
│   │           │   │   ├── go.py
│   │           │   │   ├── grammar_notation.py
│   │           │   │   ├── graph.py
│   │           │   │   ├── graphics.py
│   │           │   │   ├── graphql.py
│   │           │   │   ├── graphviz.py
│   │           │   │   ├── gsql.py
│   │           │   │   ├── hare.py
│   │           │   │   ├── haskell.py
│   │           │   │   ├── haxe.py
│   │           │   │   ├── hdl.py
│   │           │   │   ├── hexdump.py
│   │           │   │   ├── html.py
│   │           │   │   ├── idl.py
│   │           │   │   ├── igor.py
│   │           │   │   ├── inferno.py
│   │           │   │   ├── installers.py
│   │           │   │   ├── int_fiction.py
│   │           │   │   ├── iolang.py
│   │           │   │   ├── j.py
│   │           │   │   ├── javascript.py
│   │           │   │   ├── jmespath.py
│   │           │   │   ├── jslt.py
│   │           │   │   ├── json5.py
│   │           │   │   ├── jsonnet.py
│   │           │   │   ├── jsx.py
│   │           │   │   ├── julia.py
│   │           │   │   ├── jvm.py
│   │           │   │   ├── kuin.py
│   │           │   │   ├── kusto.py
│   │           │   │   ├── ldap.py
│   │           │   │   ├── lean.py
│   │           │   │   ├── lilypond.py
│   │           │   │   ├── lisp.py
│   │           │   │   ├── macaulay2.py
│   │           │   │   ├── make.py
│   │           │   │   ├── maple.py
│   │           │   │   ├── markup.py
│   │           │   │   ├── math.py
│   │           │   │   ├── matlab.py
│   │           │   │   ├── maxima.py
│   │           │   │   ├── meson.py
│   │           │   │   ├── mime.py
│   │           │   │   ├── minecraft.py
│   │           │   │   ├── mips.py
│   │           │   │   ├── ml.py
│   │           │   │   ├── modeling.py
│   │           │   │   ├── modula2.py
│   │           │   │   ├── mojo.py
│   │           │   │   ├── monte.py
│   │           │   │   ├── mosel.py
│   │           │   │   ├── ncl.py
│   │           │   │   ├── nimrod.py
│   │           │   │   ├── nit.py
│   │           │   │   ├── nix.py
│   │           │   │   ├── numbair.py
│   │           │   │   ├── oberon.py
│   │           │   │   ├── objective.py
│   │           │   │   ├── ooc.py
│   │           │   │   ├── openscad.py
│   │           │   │   ├── other.py
│   │           │   │   ├── parasail.py
│   │           │   │   ├── parsers.py
│   │           │   │   ├── pascal.py
│   │           │   │   ├── pawn.py
│   │           │   │   ├── pddl.py
│   │           │   │   ├── perl.py
│   │           │   │   ├── phix.py
│   │           │   │   ├── php.py
│   │           │   │   ├── pointless.py
│   │           │   │   ├── pony.py
│   │           │   │   ├── praat.py
│   │           │   │   ├── procfile.py
│   │           │   │   ├── prolog.py
│   │           │   │   ├── promql.py
│   │           │   │   ├── prql.py
│   │           │   │   ├── ptx.py
│   │           │   │   ├── python.py
│   │           │   │   ├── q.py
│   │           │   │   ├── qlik.py
│   │           │   │   ├── qvt.py
│   │           │   │   ├── r.py
│   │           │   │   ├── rdf.py
│   │           │   │   ├── rebol.py
│   │           │   │   ├── rego.py
│   │           │   │   ├── resource.py
│   │           │   │   ├── ride.py
│   │           │   │   ├── rita.py
│   │           │   │   ├── rnc.py
│   │           │   │   ├── roboconf.py
│   │           │   │   ├── robotframework.py
│   │           │   │   ├── ruby.py
│   │           │   │   ├── rust.py
│   │           │   │   ├── sas.py
│   │           │   │   ├── savi.py
│   │           │   │   ├── scdoc.py
│   │           │   │   ├── scripting.py
│   │           │   │   ├── sgf.py
│   │           │   │   ├── shell.py
│   │           │   │   ├── sieve.py
│   │           │   │   ├── slash.py
│   │           │   │   ├── smalltalk.py
│   │           │   │   ├── smithy.py
│   │           │   │   ├── smv.py
│   │           │   │   ├── snobol.py
│   │           │   │   ├── solidity.py
│   │           │   │   ├── soong.py
│   │           │   │   ├── sophia.py
│   │           │   │   ├── special.py
│   │           │   │   ├── spice.py
│   │           │   │   ├── sql.py
│   │           │   │   ├── srcinfo.py
│   │           │   │   ├── stata.py
│   │           │   │   ├── supercollider.py
│   │           │   │   ├── tablegen.py
│   │           │   │   ├── tact.py
│   │           │   │   ├── tal.py
│   │           │   │   ├── tcl.py
│   │           │   │   ├── teal.py
│   │           │   │   ├── templates.py
│   │           │   │   ├── teraterm.py
│   │           │   │   ├── testing.py
│   │           │   │   ├── text.py
│   │           │   │   ├── textedit.py
│   │           │   │   ├── textfmts.py
│   │           │   │   ├── theorem.py
│   │           │   │   ├── thingsdb.py
│   │           │   │   ├── tlb.py
│   │           │   │   ├── tls.py
│   │           │   │   ├── tnt.py
│   │           │   │   ├── trafficscript.py
│   │           │   │   ├── typoscript.py
│   │           │   │   ├── typst.py
│   │           │   │   ├── ul4.py
│   │           │   │   ├── unicon.py
│   │           │   │   ├── urbi.py
│   │           │   │   ├── usd.py
│   │           │   │   ├── varnish.py
│   │           │   │   ├── verification.py
│   │           │   │   ├── verifpal.py
│   │           │   │   ├── vip.py
│   │           │   │   ├── vyper.py
│   │           │   │   ├── web.py
│   │           │   │   ├── webassembly.py
│   │           │   │   ├── webidl.py
│   │           │   │   ├── webmisc.py
│   │           │   │   ├── wgsl.py
│   │           │   │   ├── whiley.py
│   │           │   │   ├── wowtoc.py
│   │           │   │   ├── wren.py
│   │           │   │   ├── x10.py
│   │           │   │   ├── xorg.py
│   │           │   │   ├── yang.py
│   │           │   │   ├── yara.py
│   │           │   │   └── zig.py
│   │           │   ├── styles
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── _mapping.cpython-313.pyc
│   │           │   │   │   ├── abap.cpython-313.pyc
│   │           │   │   │   ├── algol_nu.cpython-313.pyc
│   │           │   │   │   ├── algol.cpython-313.pyc
│   │           │   │   │   ├── arduino.cpython-313.pyc
│   │           │   │   │   ├── autumn.cpython-313.pyc
│   │           │   │   │   ├── borland.cpython-313.pyc
│   │           │   │   │   ├── bw.cpython-313.pyc
│   │           │   │   │   ├── coffee.cpython-313.pyc
│   │           │   │   │   ├── colorful.cpython-313.pyc
│   │           │   │   │   ├── default.cpython-313.pyc
│   │           │   │   │   ├── dracula.cpython-313.pyc
│   │           │   │   │   ├── emacs.cpython-313.pyc
│   │           │   │   │   ├── friendly_grayscale.cpython-313.pyc
│   │           │   │   │   ├── friendly.cpython-313.pyc
│   │           │   │   │   ├── fruity.cpython-313.pyc
│   │           │   │   │   ├── gh_dark.cpython-313.pyc
│   │           │   │   │   ├── gruvbox.cpython-313.pyc
│   │           │   │   │   ├── igor.cpython-313.pyc
│   │           │   │   │   ├── inkpot.cpython-313.pyc
│   │           │   │   │   ├── lightbulb.cpython-313.pyc
│   │           │   │   │   ├── lilypond.cpython-313.pyc
│   │           │   │   │   ├── lovelace.cpython-313.pyc
│   │           │   │   │   ├── manni.cpython-313.pyc
│   │           │   │   │   ├── material.cpython-313.pyc
│   │           │   │   │   ├── monokai.cpython-313.pyc
│   │           │   │   │   ├── murphy.cpython-313.pyc
│   │           │   │   │   ├── native.cpython-313.pyc
│   │           │   │   │   ├── nord.cpython-313.pyc
│   │           │   │   │   ├── onedark.cpython-313.pyc
│   │           │   │   │   ├── paraiso_dark.cpython-313.pyc
│   │           │   │   │   ├── paraiso_light.cpython-313.pyc
│   │           │   │   │   ├── pastie.cpython-313.pyc
│   │           │   │   │   ├── perldoc.cpython-313.pyc
│   │           │   │   │   ├── rainbow_dash.cpython-313.pyc
│   │           │   │   │   ├── rrt.cpython-313.pyc
│   │           │   │   │   ├── sas.cpython-313.pyc
│   │           │   │   │   ├── solarized.cpython-313.pyc
│   │           │   │   │   ├── staroffice.cpython-313.pyc
│   │           │   │   │   ├── stata_dark.cpython-313.pyc
│   │           │   │   │   ├── stata_light.cpython-313.pyc
│   │           │   │   │   ├── tango.cpython-313.pyc
│   │           │   │   │   ├── trac.cpython-313.pyc
│   │           │   │   │   ├── vim.cpython-313.pyc
│   │           │   │   │   ├── vs.cpython-313.pyc
│   │           │   │   │   ├── xcode.cpython-313.pyc
│   │           │   │   │   └── zenburn.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _mapping.py
│   │           │   │   ├── abap.py
│   │           │   │   ├── algol_nu.py
│   │           │   │   ├── algol.py
│   │           │   │   ├── arduino.py
│   │           │   │   ├── autumn.py
│   │           │   │   ├── borland.py
│   │           │   │   ├── bw.py
│   │           │   │   ├── coffee.py
│   │           │   │   ├── colorful.py
│   │           │   │   ├── default.py
│   │           │   │   ├── dracula.py
│   │           │   │   ├── emacs.py
│   │           │   │   ├── friendly_grayscale.py
│   │           │   │   ├── friendly.py
│   │           │   │   ├── fruity.py
│   │           │   │   ├── gh_dark.py
│   │           │   │   ├── gruvbox.py
│   │           │   │   ├── igor.py
│   │           │   │   ├── inkpot.py
│   │           │   │   ├── lightbulb.py
│   │           │   │   ├── lilypond.py
│   │           │   │   ├── lovelace.py
│   │           │   │   ├── manni.py
│   │           │   │   ├── material.py
│   │           │   │   ├── monokai.py
│   │           │   │   ├── murphy.py
│   │           │   │   ├── native.py
│   │           │   │   ├── nord.py
│   │           │   │   ├── onedark.py
│   │           │   │   ├── paraiso_dark.py
│   │           │   │   ├── paraiso_light.py
│   │           │   │   ├── pastie.py
│   │           │   │   ├── perldoc.py
│   │           │   │   ├── rainbow_dash.py
│   │           │   │   ├── rrt.py
│   │           │   │   ├── sas.py
│   │           │   │   ├── solarized.py
│   │           │   │   ├── staroffice.py
│   │           │   │   ├── stata_dark.py
│   │           │   │   ├── stata_light.py
│   │           │   │   ├── tango.py
│   │           │   │   ├── trac.py
│   │           │   │   ├── vim.py
│   │           │   │   ├── vs.py
│   │           │   │   ├── xcode.py
│   │           │   │   └── zenburn.py
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── cmdline.py
│   │           │   ├── console.py
│   │           │   ├── filter.py
│   │           │   ├── formatter.py
│   │           │   ├── lexer.py
│   │           │   ├── modeline.py
│   │           │   ├── plugin.py
│   │           │   ├── regexopt.py
│   │           │   ├── scanner.py
│   │           │   ├── sphinxext.py
│   │           │   ├── style.py
│   │           │   ├── token.py
│   │           │   ├── unistring.py
│   │           │   └── util.py
│   │           ├── pygments-2.19.2.dist-info
│   │           │   ├── licenses
│   │           │   │   ├── AUTHORS
│   │           │   │   └── LICENSE
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── pytest
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   └── __main__.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   └── py.typed
│   │           ├── pytest-9.0.2.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── python_multipart
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── decoders.cpython-313.pyc
│   │           │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   └── multipart.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── decoders.py
│   │           │   ├── exceptions.py
│   │           │   ├── multipart.py
│   │           │   └── py.typed
│   │           ├── python_multipart-0.0.21.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── starlette
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── _exception_handler.cpython-313.pyc
│   │           │   │   ├── _utils.cpython-313.pyc
│   │           │   │   ├── applications.cpython-313.pyc
│   │           │   │   ├── authentication.cpython-313.pyc
│   │           │   │   ├── background.cpython-313.pyc
│   │           │   │   ├── concurrency.cpython-313.pyc
│   │           │   │   ├── config.cpython-313.pyc
│   │           │   │   ├── convertors.cpython-313.pyc
│   │           │   │   ├── datastructures.cpython-313.pyc
│   │           │   │   ├── endpoints.cpython-313.pyc
│   │           │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   ├── formparsers.cpython-313.pyc
│   │           │   │   ├── requests.cpython-313.pyc
│   │           │   │   ├── responses.cpython-313.pyc
│   │           │   │   ├── routing.cpython-313.pyc
│   │           │   │   ├── schemas.cpython-313.pyc
│   │           │   │   ├── staticfiles.cpython-313.pyc
│   │           │   │   ├── status.cpython-313.pyc
│   │           │   │   ├── templating.cpython-313.pyc
│   │           │   │   ├── testclient.cpython-313.pyc
│   │           │   │   ├── types.cpython-313.pyc
│   │           │   │   └── websockets.cpython-313.pyc
│   │           │   ├── middleware
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── authentication.cpython-313.pyc
│   │           │   │   │   ├── base.cpython-313.pyc
│   │           │   │   │   ├── cors.cpython-313.pyc
│   │           │   │   │   ├── errors.cpython-313.pyc
│   │           │   │   │   ├── exceptions.cpython-313.pyc
│   │           │   │   │   ├── gzip.cpython-313.pyc
│   │           │   │   │   ├── httpsredirect.cpython-313.pyc
│   │           │   │   │   ├── sessions.cpython-313.pyc
│   │           │   │   │   ├── trustedhost.cpython-313.pyc
│   │           │   │   │   └── wsgi.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── authentication.py
│   │           │   │   ├── base.py
│   │           │   │   ├── cors.py
│   │           │   │   ├── errors.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── gzip.py
│   │           │   │   ├── httpsredirect.py
│   │           │   │   ├── sessions.py
│   │           │   │   ├── trustedhost.py
│   │           │   │   └── wsgi.py
│   │           │   ├── __init__.py
│   │           │   ├── _exception_handler.py
│   │           │   ├── _utils.py
│   │           │   ├── applications.py
│   │           │   ├── authentication.py
│   │           │   ├── background.py
│   │           │   ├── concurrency.py
│   │           │   ├── config.py
│   │           │   ├── convertors.py
│   │           │   ├── datastructures.py
│   │           │   ├── endpoints.py
│   │           │   ├── exceptions.py
│   │           │   ├── formparsers.py
│   │           │   ├── py.typed
│   │           │   ├── requests.py
│   │           │   ├── responses.py
│   │           │   ├── routing.py
│   │           │   ├── schemas.py
│   │           │   ├── staticfiles.py
│   │           │   ├── status.py
│   │           │   ├── templating.py
│   │           │   ├── testclient.py
│   │           │   ├── types.py
│   │           │   └── websockets.py
│   │           ├── starlette-0.50.0.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE.md
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── typing_extensions-4.15.0.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── typing_inspection
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── introspection.cpython-313.pyc
│   │           │   │   └── typing_objects.cpython-313.pyc
│   │           │   ├── __init__.py
│   │           │   ├── introspection.py
│   │           │   ├── py.typed
│   │           │   ├── typing_objects.py
│   │           │   └── typing_objects.pyi
│   │           ├── typing_inspection-0.4.2.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── uvicorn
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-313.pyc
│   │           │   │   ├── __main__.cpython-313.pyc
│   │           │   │   ├── _compat.cpython-313.pyc
│   │           │   │   ├── _subprocess.cpython-313.pyc
│   │           │   │   ├── _types.cpython-313.pyc
│   │           │   │   ├── config.cpython-313.pyc
│   │           │   │   ├── importer.cpython-313.pyc
│   │           │   │   ├── logging.cpython-313.pyc
│   │           │   │   ├── main.cpython-313.pyc
│   │           │   │   ├── server.cpython-313.pyc
│   │           │   │   └── workers.cpython-313.pyc
│   │           │   ├── lifespan
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── off.cpython-313.pyc
│   │           │   │   │   └── on.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── off.py
│   │           │   │   └── on.py
│   │           │   ├── loops
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── asyncio.cpython-313.pyc
│   │           │   │   │   ├── auto.cpython-313.pyc
│   │           │   │   │   └── uvloop.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── asyncio.py
│   │           │   │   ├── auto.py
│   │           │   │   └── uvloop.py
│   │           │   ├── middleware
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── asgi2.cpython-313.pyc
│   │           │   │   │   ├── message_logger.cpython-313.pyc
│   │           │   │   │   ├── proxy_headers.cpython-313.pyc
│   │           │   │   │   └── wsgi.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── asgi2.py
│   │           │   │   ├── message_logger.py
│   │           │   │   ├── proxy_headers.py
│   │           │   │   └── wsgi.py
│   │           │   ├── protocols
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   └── utils.cpython-313.pyc
│   │           │   │   ├── http
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── auto.cpython-313.pyc
│   │           │   │   │   │   ├── flow_control.cpython-313.pyc
│   │           │   │   │   │   ├── h11_impl.cpython-313.pyc
│   │           │   │   │   │   └── httptools_impl.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── auto.py
│   │           │   │   │   ├── flow_control.py
│   │           │   │   │   ├── h11_impl.py
│   │           │   │   │   └── httptools_impl.py
│   │           │   │   ├── websockets
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   │   ├── auto.cpython-313.pyc
│   │           │   │   │   │   ├── websockets_impl.cpython-313.pyc
│   │           │   │   │   │   ├── websockets_sansio_impl.cpython-313.pyc
│   │           │   │   │   │   └── wsproto_impl.cpython-313.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── auto.py
│   │           │   │   │   ├── websockets_impl.py
│   │           │   │   │   ├── websockets_sansio_impl.py
│   │           │   │   │   └── wsproto_impl.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── utils.py
│   │           │   ├── supervisors
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-313.pyc
│   │           │   │   │   ├── basereload.cpython-313.pyc
│   │           │   │   │   ├── multiprocess.cpython-313.pyc
│   │           │   │   │   ├── statreload.cpython-313.pyc
│   │           │   │   │   └── watchfilesreload.cpython-313.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── basereload.py
│   │           │   │   ├── multiprocess.py
│   │           │   │   ├── statreload.py
│   │           │   │   └── watchfilesreload.py
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── _compat.py
│   │           │   ├── _subprocess.py
│   │           │   ├── _types.py
│   │           │   ├── config.py
│   │           │   ├── importer.py
│   │           │   ├── logging.py
│   │           │   ├── main.py
│   │           │   ├── py.typed
│   │           │   ├── server.py
│   │           │   └── workers.py
│   │           ├── uvicorn-0.40.0.dist-info
│   │           │   ├── licenses
│   │           │   │   └── LICENSE.md
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── __editable__.image_to_3d_relief-1.0.0.pth
│   │           ├── py.py
│   │           └── typing_extensions.py
│   └── pyvenv.cfg
├── presets
│   ├── cmyk_like_auto.json
│   ├── default_4_auto.json
│   ├── default_4_manual.json
│   └── default.json
├── src
│   ├── app
│   │   ├── __pycache__
│   │   │   ├── bundle_runner.cpython-313.pyc
│   │   │   ├── cli_errors.cpython-313.pyc
│   │   │   ├── cli_overrides.cpython-313.pyc
│   │   │   ├── doctor.cpython-313.pyc
│   │   │   ├── filaments_cli.cpython-313.pyc
│   │   │   ├── image_io.cpython-313.pyc
│   │   │   ├── main.cpython-313.pyc
│   │   │   ├── pipeline.cpython-313.pyc
│   │   │   ├── preview_runner.cpython-313.pyc
│   │   │   └── version.cpython-313.pyc
│   │   ├── bundle_runner.py
│   │   ├── cli_errors.py
│   │   ├── cli_overrides.py
│   │   ├── doctor.py
│   │   ├── image_io.py
│   │   ├── logging.py
│   │   ├── main.py
│   │   ├── pipeline.py
│   │   ├── preview_runner.py
│   │   ├── types.py
│   │   └── version.py
│   ├── color
│   │   ├── __pycache__
│   │   │   └── color_distance.cpython-313.pyc
│   │   └── color_distance.py
│   ├── geom
│   │   ├── __pycache__
│   │   │   └── mesh_generation.cpython-313.pyc
│   │   └── mesh_generation.py
│   ├── image_to_3d_relief.egg-info
│   │   ├── dependency_links.txt
│   │   ├── PKG-INFO
│   │   ├── requires.txt
│   │   ├── SOURCES.txt
│   │   └── top_level.txt
│   ├── ops
│   │   ├── __pycache__
│   │   │   ├── add_border.cpython-313.pyc
│   │   │   ├── height_map.cpython-313.pyc
│   │   │   ├── layers_to_mm.cpython-313.pyc
│   │   │   ├── merge_small_regions.cpython-313.pyc
│   │   │   ├── palette_mapping.cpython-313.pyc
│   │   │   ├── palette_suggestion.cpython-313.pyc
│   │   │   ├── preprocess_edge_preserving.cpython-313.pyc
│   │   │   ├── scale_to_canvas.cpython-313.pyc
│   │   │   └── segment_superpixels.cpython-313.pyc
│   │   ├── add_border.py
│   │   ├── height_map.py
│   │   ├── layers_to_mm.py
│   │   ├── merge_small_regions.py
│   │   ├── palette_mapping.py
│   │   ├── palette_suggestion.py
│   │   ├── preprocess_edge_preserving.py
│   │   ├── scale_to_canvas.py
│   │   └── segment_superpixels.py
│   ├── print
│   │   ├── __pycache__
│   │   │   ├── colorplan_export.cpython-313.pyc
│   │   │   ├── filament_assignment.cpython-313.pyc
│   │   │   └── filaments.cpython-313.pyc
│   │   ├── colorplan_export.py
│   │   ├── filament_assignment.py
│   │   └── filaments.py
│   ├── sim
│   │   ├── __pycache__
│   │   │   └── td_preview.cpython-313.pyc
│   │   └── td_preview.py
│   ├── solver
│   │   ├── __pycache__
│   │   │   └── region_recipe.cpython-313.pyc
│   │   └── region_recipe.py
│   ├── tools
│   │   ├── __pycache__
│   │   │   ├── filamentcolors_sync.cpython-313.pyc
│   │   │   ├── filaments_cli.cpython-313.pyc
│   │   │   └── preset_gen.cpython-313.pyc
│   │   ├── filamentcolors_sync.py
│   │   ├── filaments_cli.py
│   │   └── preset_gen.py
│   └── web
│       ├── __pycache__
│       │   └── server.cpython-313.pyc
│       └── server.py
├── tests
│   ├── __pycache__
│   │   ├── test_add_border.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_cli_bundle.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_cli_overrides_subprocess.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_cli_overrides.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_cli_pipeline.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_cli_preview.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_cli_version.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_color_distance.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_colorplan_export.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_colorplan_plan.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_examples_bundle.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_filament_assignment.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_filamentcolors_sync.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_filaments_cli.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_height_map.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_image_io.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_layers_to_mm.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_merge_small_regions.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_mesh_generation.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_palette_mapping.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_palette_suggestion.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_preprocess_edge_preserving.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_preset_gen.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_region_recipe.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_scale_to_canvas.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_segment_superpixels.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_smoke.cpython-313-pytest-9.0.2.pyc
│   │   ├── test_td_preview.cpython-313-pytest-9.0.2.pyc
│   │   └── test_web_server.cpython-313-pytest-9.0.2.pyc
│   ├── test_add_border.py
│   ├── test_cli_bundle.py
│   ├── test_cli_overrides_subprocess.py
│   ├── test_cli_overrides.py
│   ├── test_cli_pipeline.py
│   ├── test_cli_preview.py
│   ├── test_cli_version.py
│   ├── test_color_distance.py
│   ├── test_colorplan_export.py
│   ├── test_colorplan_plan.py
│   ├── test_examples_bundle.py
│   ├── test_filament_assignment.py
│   ├── test_filamentcolors_sync.py
│   ├── test_filaments_cli.py
│   ├── test_height_map.py
│   ├── test_image_io.py
│   ├── test_layers_to_mm.py
│   ├── test_merge_small_regions.py
│   ├── test_mesh_generation.py
│   ├── test_palette_mapping.py
│   ├── test_palette_suggestion.py
│   ├── test_preprocess_edge_preserving.py
│   ├── test_preset_gen.py
│   ├── test_region_recipe.py
│   ├── test_scale_to_canvas.py
│   ├── test_segment_superpixels.py
│   ├── test_smoke.py
│   ├── test_td_preview.py
│   └── test_web_server.py
├── CHANGELOG.md
├── CODEX_RULES.md
├── CONTRACTS.md
├── DECISIONS.md
├── LICENSE
├── Makefile
├── pyproject.toml
├── README.md
├── REPORT.md
├── result.zip
├── ROADMAP.md
└── STRUKTURA.md

497 directories, 4425 files
