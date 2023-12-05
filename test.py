from mirruido import Mirruido


mirruido = Mirruido(ruta_audio="/home/jerryperez/Documents/110_24_a62f8bc9.wav")
mirruido.procesarAudio()

print(len(mirruido.obtener_audio_procesado()))
print(len(mirruido.obtener_audio_procesado_recortado()))


# mirruido = Mirruido(ruta_audio="/home/jerryperez/Documents/110_24_a62f8bc9.wav")
mirruido.procesarAudio()

print(len(mirruido.obtener_audio_procesado()))
print(len(mirruido.obtener_audio_procesado_recortado()))
