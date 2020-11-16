from tkinter import *

class PlaceTxt():
    def __init__(self, root: Tk, canvas: Canvas, txt : str, txtx : int, txty :int , **kwargs) -> None:
        """[Deze class plaatst tekst op de gegeven coordinaten]
        Args:
            root (Tk): [root object (altijd root)]
            canvas (Canvas): [canvas object (altijd canvas)]
            txt (str): [tekst die je wilt plaatsen]
            txtx (int): [x coördinaat van je tekst]
            txty (int): [y coördinaat van je tekst]

        Keyword arguments:
            kleur (str): kleur van de tekst 
            font (str): font type (Arial, comic sans etc)
            size (int): grootte van tekst 

        """                                                        
        self.root = root                                                       
        self.text = canvas.create_text(root.winfo_screenwidth() * txtx, root.winfo_screenheight() * txty, text=txt, fill=kwargs['kleur'] if 'kleur' in kwargs else 'white',
                                                                        font=(kwargs['font'] if 'font' in kwargs else "Times 10",
                                                                            kwargs['size'] if 'size' in kwargs else 20))
