from televisores.tv import TV
class Control:
    _tv = None

    def turnOn(self):
        _tv.turnOn()
    
    def turnOff(self):
        _tv.turnOff()

    def canalUp(self):
        _tv.canalUp()

    def canalDown(self):
        _tv.canalDown

    def volumenUp(self):
        _tv.volumenUp()

    def volumenDown(self):
        _tv.volumenDown()

    def setCanal(self, num):
        _tv.setCanal(num)

    def setVolumen(self, num):
        _tv.setVolumen(num)

    def enlazar(self,tv):
        self._tv = tv
        tv.setControl(self)

    def getTv(self):
        return self._tv
    
    def setTv(self,tv):
        self._tv = tv
    