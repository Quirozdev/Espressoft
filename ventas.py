# se importan todos los componentes de la ui generada automaticamente
# ventas_ui.py se genera automaticamente al guardar el .ui en QT Designer y al utilizar el comando:
# pyuic5 -x (ruta_archivo.ui) -o (ruta_archivo_a_generar_ui.py)
# despues de -x va la ruta del archivo .ui que se quiere transformar y despues de -o (output) va la ruta del archivo que se va a generar
# Ejemplo (usando rutas relativas):
# pyuic5 -x ventas.ui -o ventas_ui.py
from ventas_ui import *

# se crea una clase que representa a la ventana principal, la cual hereda de la clase general del widget QMainWindows
# y tambien hereda de la clase que se genera automaticamente para la ui de la ventana principal (MainWindows)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        # setupUi genera la interfaz con todos los componentes hechos en QT Designer, se le pasa self
        # como el propio objeto de MainWindow
        self.setupUi(self)

        """
        ESTADOS DE INICIO
        """
        # el nombre que se le haya dado al componente en QT Designer, es el nombre que se utiliza para acceder 
        # a ese componente aqui, como atributo del objeto que lo contiene (MainWindow)
        # Ejemplo: Si en QT Designer a un boton se le puso el nombre "opciones_ventas_totales", para acceder
        # a ese componente desde aqui, se usaria algo como "self_opciones_ventas_totales" y con eso se puede
        # operar con el componente, como agregarle eventos o personalizarlo

       
        # en QT Designer hay un widget que contiene a los botones Ventas diarias, Ventas mensuales y Ventas anuales
        # para las ventas totales y otro para las ventas individuales respectivamente.
        # QT Designer no deja ocultar widgets/componentes al inicio de la aplicacion, por lo que aqui se ocultan
        # manualmente al principio usando el metodo .setHidden() y luego se muestran cuando se presionan los botones
        # desplegables de Ventas totales y/o Ventas individuales

        self.opciones_ventas_totales.setHidden(True)

        self.opciones_ventas_individuales.setHidden(True)

        """
        EVENTOS: PRESIONAR UN BOTON
        """

        # mediante el atributo clicked de un boton (QButtonPush) y usando el metodo .connect(), se puede asociar
        # una funcion al boton cuando este se presione.
        # por defecto, la funcion/metodo solo se puede pasar con su nombre sin parentesis (sin parametros), por que si no se estaria llamando cada
        # vez que inicia la aplicacion, para eso se utiliza una funcion lambda que si lo permite

        # los botones que pueden desplegar mas botones, estan constituidos de 2 botones que realizan la misma funcion, un boton que contiene el texto
        # del boton (por ejemplo Ventas totales) y otro que contiene el icono desplegable (el triangulito), cuando se presiona uno de estos 2,
        # "despliegan" los botones que le corresponden (por ejemplo si se presiona el boton Ventas totales o su boton correspondiente desplegable, este va a desplegar a 
        # los botones Ventas diarias, Ventas mensuales, Ventas anuales, que en realidead es el widget que los contiene) 

        # son 2 botones separados y no estan juntos en un solo boton (texto e icono), porque era complicado acomodarlos responsivamente para que el boton
        # de texto siempre estuviera pegado al borde izquierdo del menu lateral y el boton desplegable cerca del borde derecho del menu lateral
        self.boton_ventas_totales.clicked.connect(lambda: self.ocultar_mostrar_opciones(self.boton_ventas_totales, self.boton_ventas_totales_desplegable, self.opciones_ventas_totales))
        self.boton_ventas_totales_desplegable.clicked.connect(lambda: self.ocultar_mostrar_opciones(self.boton_ventas_totales, self.boton_ventas_totales_desplegable, self.opciones_ventas_totales))

        self.boton_ventas_individuales.clicked.connect(lambda: self.ocultar_mostrar_opciones(self.boton_ventas_individuales, self.boton_ventas_individuales_desplegable, self.opciones_ventas_individuales))
        self.boton_ventas_individuales_desplegable.clicked.connect(lambda: self.ocultar_mostrar_opciones(self.boton_ventas_individuales, self.boton_ventas_individuales_desplegable, self.opciones_ventas_individuales))

        # el boton de empleados no es un boton desplegable, por lo que solo se le asocia el metodo agregar_quitar_borde_izquierdo_boton() el cual al
        # presionarse simplemente se le agrega el borde izquierdo
        self.boton_empleados.clicked.connect(lambda: self.agregar_quitar_borde_izquierdo_boton(self.boton_empleados, True))

        # el boton para cerrar la aplicacion
        self.boton_cerrar.clicked.connect(self.cerrar)


    def ocultar_mostrar_opciones(self, boton_texto, boton_desplegable_correspondiente, widget_opciones):
        """
        Oculta o Muestra los widgets que contienen a botones que aparecen al ser desplegados por su boton_texto o boton_desplegable_correspondiente, de modo que da el efecto de un desplegable.
        Recibe como parametros el "boton_texto" que es el boton que contiene texto (Ventas totales o Ventas individuales), el boton_desplegable_correspondiente (los cuales pueden presionarse para cumplir la misma funcion)
        y el widget que se va a ocultar o mostrar.
        """
        # se checa si el widget ya se encuentra oculto (al iniciar la aplicacion va a empezar oculto)
        if widget_opciones.isHidden():
            # como se encuentra oculto y se presiono uno de los 2 botones para mostrarlo, entonces el boton que contiene al icono desplegable, se "voltea",
            # cambiando la imagen (para que de un efecto de desplegable)
            boton_desplegable_correspondiente.setIcon(QtGui.QIcon('resources/img/icono_desplegable_volteado.png'))
            # se le agrega el borde izquierdo blanco que aparece en el disenio al boton que contiene el texto
            self.agregar_quitar_borde_izquierdo_boton(boton_texto, True)
        else:
            # si no se encuentra oculto y se presiono uno de los 2 botones para mostrarlo, entonces el boton que contiene al icono desplegable, vuelve
            # a su estado "normal" cambiando a la imagen original
            boton_desplegable_correspondiente.setIcon(QtGui.QIcon('resources/img/icono_desplegable.png'))
            # se le quita el borde izquierdo al boton que contiene el texto
            self.agregar_quitar_borde_izquierdo_boton(boton_texto, False)
        # finalmente el widget de opciones/botones se oculta o muestra, dependiendo de si se encuentra oculto o no
        # si el widget esta oculto, entonces widget_opciones.isHidden() = True, por lo que:
        # widget_opciones.setHidden(not True)
        # widget_opciones.setHidden(False)  ----> Se muestra
        # si el widget no esta oculto, entonces widget_opciones.isHidden() = False, por lo que:
        # widget_opciones.setHidden(not False)
        # widget_opciones.setHidden(True)  ----> Se oculta
        widget_opciones.setHidden(not widget_opciones.isHidden())


    def agregar_quitar_borde_izquierdo_boton(self, boton, agregar: bool):
        """
        Agrega o quita el borde izquierdo (es de color blanco como en el disenio) de un boton determinado.
        Recibe como parametros el boton a agregar o quitar borde izquierdo y un booleano agregar, que si es True, entonces se agrega, en caso contrario se quita
        """
        if agregar:
            # se modifica la hoja de estilos del boton, manteniendo los atributos que ya tenia y agregandole la propiedad border-left
            boton.setStyleSheet('color: rgb(255, 255, 255);' 'font: 75 12pt "Times New Roman";' 'border: none;' 'border-left: 3px solid white;' 'padding: 10px;' 'background-color: rgb(65, 107, 191);')
            # se le quita el borde izquierdo a los demas botones
            self.quitar_borde_izquierdo_a_otros_botones(boton)
        else:
            # se le quita la propiedad border-left
            boton.setStyleSheet('color: rgb(255, 255, 255);' 'font: 75 12pt "Times New Roman";' 'border: none;' 'padding: 10px;') 


    def quitar_borde_izquierdo_a_otros_botones(self, boton_presionado):
        """
        Quita el borde izquierdo a los botones que no sean el ultimo boton_presionado.
        Recibe como parametro el boton_presionado, el cual es el unico que va a mantener el borde izquierdo
        """
        # se le quite el borde izquierdo a todos los botones que puedan tener borde izquierdo
        self.agregar_quitar_borde_izquierdo_boton(self.boton_ventas_totales, False)
        self.agregar_quitar_borde_izquierdo_boton(self.boton_ventas_individuales, False)
        self.agregar_quitar_borde_izquierdo_boton(self.boton_empleados, False)
        # se restaura el borde izquierdo unicamente al ultimo boton presionado desplegable
        # no se vuelve a usar el metodo .agregar_quitar_borde_izquierdo_boton() por que se haria un ciclo recursivo infinito
        boton_presionado.setStyleSheet('color: rgb(255, 255, 255);' 'font: 75 12pt "Times New Roman";' 'border: none;' 'border-left: 3px solid white;' 'padding: 10px;' 'background-color: rgb(65, 107, 191);')

    
    def cerrar(self):
        """
        Cierra la aplicacion.
        """
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()