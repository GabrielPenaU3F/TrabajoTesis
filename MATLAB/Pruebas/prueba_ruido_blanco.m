y = generar_ruido_blanco_gaussiano(10,44100,2);
audiowrite('whitenoise.wav',y,44100);