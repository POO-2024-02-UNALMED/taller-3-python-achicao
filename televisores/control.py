from televisores.tv import TV
class Control:
    _tv = None

    def turnOn(self):
        self._tv.turnOn()
    
    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self, num):
        self._tv.setCanal(num)

    def setVolumen(self, num):
        self._tv.setVolumen(num)

    def getTv(self):
        return self._tv
    
    def setTv(self,tv):
        self._tv = tv
    
    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)