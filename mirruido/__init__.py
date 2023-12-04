
import numpy as np
import librosa
import soundfile as sf
import numpy as np
from sklearn.preprocessing import MinMaxScaler


#TODO Crear una clase para el objeto audio y para poder almacenar audio_procesado y 
# ofrecer metodos para retornar audio_procesado completo y sin segmentos de silencio

def procesarAudio(ruta_audio, top_db=30, confianza=.956):
  audio, tasa = sf.read(ruta_audio)
  area_bajo_curva = 0
  while area_bajo_curva < confianza:
    audio_procesado = np.zeros(audio.shape)
    #Read the intervals to reassign the filtered values
    for inicio, final in librosa.effects.split(audio, top_db=top_db):
        audio_procesado[inicio:final] = audio[inicio:final]

  
    y_valores  = MinMaxScaler().fit_transform(np.sort((np.abs(audio_procesado))).reshape(-1,1))
    x_valores = MinMaxScaler().fit_transform(np.array(range(0, len(y_valores))).reshape(-1,1))

    area_bajo_curva = np.trapz(np.ravel(x_valores), np.ravel(y_valores))
    if area_bajo_curva < confianza: top_db = top_db-1

    print(area_bajo_curva)
    print(top_db)
    return audio_procesado[audio_procesado != 0]