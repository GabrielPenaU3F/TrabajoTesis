# Trabajo de Tesis - Mediciones Acústicas Basadas en Software

Instalación y ejecución:

	1. Python

		Se requiere tener instalado Python, pip y pipreqs para poder ejecutar la aplicación.

		Primero, debe actualizar el archivo de dependencias. Para eso, ejecute el comando:

		>pipreqs --force --encoding=utf-8 Python

		A continuación, debe instalar todas las dependencias. Para ello sitúese en la carpeta 'Python' y ejecute el comando:

		>pip install -r requirements.txt

		Una vez que todas las dependencias están instaladas, ya se puede ejecutar la aplicación. Para ello, en el mismo directorio 'Python' corra el comando:

		>python medidor_acustico

		Para correr los tests, debe situarse en el directorio 'Python/medidor_acustico' y ejecutar:

		>python -m unittest discover

		Es importante que lo haga de esta forma, ya que si lo hace desde otro lugar Python le arrojará errores relacionados con los import. También puede correr los módulos de pruebas de manera individual, por ejemplo:

		>python -m unittest test/cases/test_ess.py

		También puede utilizar la librería Green para visualizar mejor los resultados de los tests. Si está en Windows, ejecute el archivo 'green-run-all-tests.bat' en la carpeta 'Pyton/medidor_acustico/test'. Si no está en Windows, deberá agregar manualmente el path del directorio 'Python\medidor_acustico' a la variable PYTHONPATH y luego, desde la carpeta 'Python\medidor_acustico' ejecutar el comando:

		>green -vvv -a

		Para obtener el reporte de cobertura en HTML, si está en Windows puede ejevutar el archivo 'run-all-tests-with-coverage.bat' en la carpeta 'Python/medidor_acustico/test'. Si no está en Windows, puede hacerlo de forma manual ejecutando los siguientes comandos en dicha carpeta:

		>coverage run run_all_tests.py
		>coverage html
		
		Nota: para que estos comandos funcionen correctamente, el directorio 'medidor_acustico' debe estar en la variable de entorno PYTHONPATH de su sistema operativo. Asegúrese de incluirlo primero.
	
	2. Precompilados
	
		2.1 Windows
			
			Dentro del archivo .rar encontrará un ejecutable 'medidor-acustico.exe' y una carpeta del mismo nombre. Descomprimalos ambos en un mismo directorio.
			
			Para ejecutar la aplicación, utilice el ejecutable previamente mencionado, NO el que está dentro de la carpeta.
			
			Siempre mueva el ejecutable y la carpeta juntos, no los separe; de lo contrario la aplicación no funcionará.
		
		2.2 Linux (probado en Ubuntu)
			
			Extraiga el contenido del archivo 'medidor-acustico.tar.gz'. Puede hacerlo con el comando
			
			>tar -zxvf medidor-acustico.tar.gz
			
			Dentro encontrará una carpeta 'medidor-acustico'. 
			
			Para poder ejecutar la aplicación, requiere tener instalada la librería PortAudio. Puede instalarla mediante el comando 
			
			>sudo apt install libportaudio2
			
			Luego, desde su terminal, sitúese dentro del directorio 'medidor-acustico' y ejecute el comando 

			>./medidor-acustico
			
	
	





