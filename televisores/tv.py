class TV:
    _canal = 1
    _precio = 500
    _volumen = 1
    _control = None
    _numTV = 0

    def __init__(self,marca,estado):
        self._marca = marca
        self._estado = estado
    
    def getMarca(self):
        return self._marca
    
    def setMarca(self,marca):
        self._marca = marca
    
    def getCanal(self):
        return self._canal
    
    def setCanal(self,canal):
        if 1 <= canal <= 120:
            self._canal = canal

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self,precio):
        self._precio = precio  

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self,volumen):
        if 0 <= volumen <= 7:
            self._volumen = volumen

    def getControl(self):
        return self._control
    
    def setControl(self,control):
        self._control = control

    @classmethod
    def setNumTV(cls,num):
        cls._numTV = num

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False
    
    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if getEstado() == True:
            if 1 <= self._canal < 120:
                self._canal += 1
    
    def canalDown(self):
        if getEstado() == True:
            if 1 < self._canal <= 120:
                self._canal += 1
    
    def volumenUp(self):
        if getEstado() == True:
            if 0 <= self._volumen < 7:
                self._volumen += 1
    
    def volumenDown(self):
        if getEstado() == True:
            if 0 < self._volumen <= 7:
                self._volumen += 1

    