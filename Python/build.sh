pyinstaller 'medidor_acustico/main.py' \
--windowed \
--name 'medidor-acustico' \
--clean \
--specpath 'medidor_acustico' \
--distpath 'exe' \
--hidden-import pyexcel.plugins \
--hidden-import pyexcel.plugins.parsers \
--hidden-import pyexcel.plugins.renderers \
--hidden-import pyexcel.plugins.sources \
--hidden-import pyexcel_io.readers.csvr \
--hidden-import pyexcel_io.readers.csvz \
--hidden-import pyexcel_io.readers.tsv \
--hidden-import pyexcel_io.readers.tsvz \
--hidden-import pyexcel_io.writers.csvw \
--hidden-import pyexcel_io.readers.csvz \
--hidden-import pyexcel_io.readers.tsv \
--hidden-import pyexcel_io.readers.tsvz \
--hidden-import pyexcel_io.database.importers.django \
--hidden-import pyexcel_io.database.importers.sqlalchemy \
--hidden-import pyexcel_io.database.exporters.django \
--hidden-import pyexcel_io.database.exporters.sqlalchemy \
--hidden-import pyexcel_xlsx \
--hidden-import pyexcel_xlsx.xlsxr \
--hidden-import pyexcel_xlsx.xlsxw \
--hidden-import pyexcel_ods \
--hidden-import pyexcel_ods.odsr \
--hidden-import pyexcel_ods.odsw \
--add-data 'resources:.'

rm -r build/