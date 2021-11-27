### Solución al problema de plugins en Pyside2

Para solucionar un problema relacionado a la falta de plugin en __windows__, es necesario seguir los siguientes pasos:

* localizar y copiar los siguientes archivos en los directorios que se mencionan acontinuación:

    * `\Anaconda3\Lib\site-packages\PySide2\plugins\platforms\qminimal.dll`
    * `\Anaconda3\Lib\site-packages\PySide2\plugins\platforms\qoffscreen.dll`
    * `\Anaconda3\Lib\site-packages\PySide2\plugins\platforms\qwindows.dll`

* copiar a la siguiente ruta:
  * `\Anaconda3\Library\plugins\platforms\`
