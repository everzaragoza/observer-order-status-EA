from .observer import Observer
 
 
class OrderStatus:
 
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.status = "NEW"
        self._observers: list[Observer] = []
 
    def subscribe(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
 
    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)
 
    def set_status(self, status: str) -> None:
        self.status = status
        for observer in list(self._observers):
            
            observer.update(self.order_id, status)
 