from logic import *


#hier nieuwe plaatjes,tekst etc
baseImg = PlaceImage(root,'t.png',0.5,0.5,canvas,foto_x_resize=root.winfo_screenwidth(),foto_y_resize=root.winfo_screenheight())

sunny = PlaceGif(root,canvas,'sun.gif',0.18,0.24,resize='min',amount=3)

zonnenPanelenTekst = PlaceTxt(root,canvas,'Zonnenpanelen',0.218,0.365,size=17)



#hier komen alle grafieken
# graph = PlaceGraph(root,canvas,fig,0.2,0.2,24)


root.mainloop()
