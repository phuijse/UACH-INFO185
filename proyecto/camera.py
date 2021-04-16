import cv2
import numpy as np
import PIL.Image
import io

class CameraReader:
    
    def __init__(self, spthreshold=0.999):
        print("Iniciando lector de camara")
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
        print("OpenCV version: major: {0}, minor: {1}, subminor: {2}".format(major_ver, minor_ver, subminor_ver))
        videopath = 'torres_paine_pan.mp4'
        self.vid = cv2.VideoCapture(videopath)
        self.properties = {'width': int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)),
                           'height': int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                           'fps': self.vid.get(cv2.CAP_PROP_FPS)}
        
        self.frame_number = 0
        self.spthreshold = spthreshold
        y = np.linspace(0, self.properties['height'], num=self.properties['height'])
        x = np.linspace(0, self.properties['width'], self.properties['width'])
        X, Y = np.meshgrid(x, y)
        self.noise_angle = 2.0*np.pi*(20*Y + 2*X)
        assert self.vid.isOpened(), "Video no encontrado" 
        
    def __iter__(self):
        return self

    def __next__(self):
        """
        Función iteradora, cada vez que es llamada lee y retorna un frame de video
        
        Termina cuando el video ha sido consumido por completo
        """
        successfully_read, frame = self.vid.read()
        if not successfully_read:
            raise StopIteration
        
        self.current_original_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        noisy_frame = self.current_original_frame.copy().astype(np.float32)/255.        
        periodic_noise = 0.5 + 0.5*np.cos(self.noise_angle  - self.frame_number*0.1)
        periodic_noise = periodic_noise.reshape(noisy_frame.shape)
        noisy_frame += periodic_noise
        noisy_frame /= np.amax(np.abs(noisy_frame))
        
        spprob = np.random.rand(self.properties['height'], self.properties['width'])
        smask = spprob > self.spthreshold
        pmask = spprob < 1. - self.spthreshold
        noisy_frame[smask] = 1.
        noisy_frame[pmask] = 0.
        self.frame_number += 1
        return (255*noisy_frame).astype(np.uint8)
    
    def get_resolution(self):
        """
        Retorna una tupla con el alto (filas) y ancho (columnas) del video
        """
        return (self.properties['height'], self.properties['width'])
    
    def get_fps(self):
        """
        Retorna los cuadros por segundo (fps) del video
        """
        return self.properties['fps']
    
    def error(self, recovered_frame):
        """
        Retorna el error  cuadrático medio entre el frame original y el frame recuperado
        """
        return np.average((recovered_frame - self.current_original_frame)**2)
        
    def __del__(self):
        self.vid.release()  
        cv2.destroyAllWindows()


"""
def display_frame(out_widget, frame):
    f = io.BytesIO() 
    PIL.Image.fromarray(frame).save(f, 'JPEG')
    out_widget.value = f.getvalue()
"""