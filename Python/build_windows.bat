set PYTHONPATH=medidor_acustico
python -m PyInstaller "medidor_acustico\main.py" ^
--name "medidor-acustico" ^
--clean ^
--windowed ^
--specpath "medidor_acustico" ^
--distpath "executable" ^
--hidden-import pyexcel ^
--hidden-import pyexcel.plugins.renderers.excel ^
--hidden-import pyexcel.plugins.renderers._texttable ^
--hidden-import pyexcel.plugins.parsers.excel ^
--hidden-import pyexcel.plugins.sources.http ^
--hidden-import pyexcel.plugins.sources.file_input ^
--hidden-import pyexcel.plugins.sources.memory_input ^
--hidden-import pyexcel.plugins.sources.file_output ^
--hidden-import pyexcel.plugins.sources.output_to_memory ^
--hidden-import pyexcel.plugins.sources.pydata.bookdict ^
--hidden-import pyexcel.plugins.sources.pydata.dictsource ^
--hidden-import pyexcel.plugins.sources.pydata.arraysource ^
--hidden-import pyexcel.plugins.sources.pydata.records ^
--hidden-import pyexcel_io ^
--hidden-import pyexcel_io.readers ^
--hidden-import pyexcel_io.writers ^
--hidden-import pyexcel_io.database ^
--hidden-import pyexcel_xlsx ^
--hidden-import pyexcel_xlsx.xlsxw ^
--hidden-import pyexcel_ods ^
--hidden-import pyexcel_ods.odsw ^
--add-data "resources;.\resources"

rmdir /Q /S build