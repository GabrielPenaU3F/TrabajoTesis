fs = 44100;
t_ruido = 3;
x = generar_ruido_blanco_gaussiano(t_ruido, fs, 8);
audio_player = audioplayer(x, fs);
play(audio_player);

audio_recorder = audiorecorder(fs, 24, 1); %24 bits, canal mono
recordblocking(audio_recorder, t_ruido + 7); 
y = getaudiodata(audio_recorder);