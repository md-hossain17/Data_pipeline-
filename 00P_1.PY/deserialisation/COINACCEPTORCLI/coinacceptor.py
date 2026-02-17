class coinacceptor:
    def __init__(self):
        self._amount = 0
        self._value = 0.0
    

    
    def insertcoin(self, value: float) -> None:
        self._amount += 1
        self._value += value
        
    def getamount(self) -> int:
        return self._amount
    
    def returncoins(self) -> tuple[int, float]:
        coins_returned = self._amount
        value_returned = self._value
        self._amount = 0
        self._value = 0.0
        return coins_returned, value_returned
    
    def getvalue(self) -> float:
        return self._value