@echo OFF

cd executable\medidor-acustico
set path=%path%;%cd%\resources\lib\portaudio\

start medidor-acustico.exe
exit