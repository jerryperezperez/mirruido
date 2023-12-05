
import numpy as np
import librosa
import soundfile as sf
from sklearn.preprocessing import MinMaxScaler



class Mirruido:
  def __init__(self, ruta_audio=None, top_db=30, confianza=.95):
     self.ruta_audio = ruta_audio
     self.top_db = top_db
     self.confianza = confianza
     self.audio_procesado = None

  def procesarAudio(self):
    audio, tasa = sf.read(self.ruta_audio)
    area_bajo_curva = 0
    while area_bajo_curva < self.confianza:
      print(area_bajo_curva)
      print(self.top_db)
      self.audio_procesado = np.zeros(audio.shape)
      #Read the intervals to reassign the filtered values
      for inicio, final in librosa.effects.split(audio, top_db=self.top_db):
          self.audio_procesado[inicio:final] = audio[inicio:final]
    
      y_valores  = MinMaxScaler().fit_transform(np.sort((np.abs(self.audio_procesado))).reshape(-1,1))
      x_valores = MinMaxScaler().fit_transform(np.array(range(0, len(y_valores))).reshape(-1,1))

      area_bajo_curva = np.trapz(np.ravel(x_valores), np.ravel(y_valores))
      if area_bajo_curva < self.confianza: self.top_db = self.top_db-1

    
  
  def obtener_audio_procesado(self):
     return self.audio_procesado
  
  def obtener_audio_procesado_recortado(self):
     return self.audio_procesado[self.audio_procesado != 0]