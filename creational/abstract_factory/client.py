from factory import WinFactory, MacFactory
from factory import GUIFactory

class Client:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        
    def render(self):
        self.factory.create_button().render()
        self.factory.create_checkbox().render()
        
        
if __name__ == "__main__":
    client = Client(WinFactory())
    client.render()
    
    client = Client(MacFactory())
    client.render()