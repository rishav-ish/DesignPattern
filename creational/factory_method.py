from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass
    
    @abstractmethod
    def onClick(self) -> None:
        pass
    
    
class WindowsButton(Button):
    def render(self) -> None:
        print("Windows Button Rendered")
    
    def onClick(self) -> None:
        print("Windows Button Clicked")
    
    
class HTMLButton(Button):
    def render(self) -> None:
        print("HTML Button Rendered")
    
    def onClick(self) -> None:
        print("HTML Button Clicked")
    
    
class Dialog(ABC):
    @abstractmethod
    def render(self) -> None:
        pass 
    
    @abstractmethod
    def createButton(self) -> Button:
        pass
    
    
class WindowsDialog(Dialog):
    def render(self) -> None:
        self.button = self.createButton()
        self.button.render()
    
    def createButton(self) -> Button:
        return WindowsButton()
    
    
class HTMLDialog(Dialog):
    def render(self) -> None:
        self.button = self.createButton()
        self.button.render()
    
    def createButton(self) -> Button:
        return HTMLButton()
    
    
if __name__ == "__main__":
    dialog = WindowsDialog()
    dialog.render()
    dialog = HTMLDialog()
    dialog.render()

