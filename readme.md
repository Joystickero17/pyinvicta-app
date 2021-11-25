## solución al problema de plugins en Pyside2

If you are running PyQt5 and PySide2, this solved the problem for me:

Copy the following files:

\Anaconda3\Lib\site-packages\PySide2\plugins\platforms\qminimal.dll
\Anaconda3\Lib\site-packages\PySide2\plugins\platforms\qoffscreen.dll
\Anaconda3\Lib\site-packages\PySide2\plugins\platforms\qwindows.dll
to:

\Anaconda3\Library\plugins\platforms\