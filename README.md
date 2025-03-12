# IA-UHU

# Prácticas Año 24/25

Vamos a realizar un Laberinto que sea recorrido por varios agentes.

Máximo de movimientos 1000.
Tamaño estándar del laberinto 10x15
Entrada y salida con E y S en las casillas del laberinto.

Laberinto
-Generar()
-Cargar()

Percepcion
-Observar()
Array<Movimiento>

InterfazAgente
-MetodosQueImplementanElRestoDeAgentes...

AgenteReactivo
-Actuar()

AgenteDeliverativo
-Actuar()


# Notas del ultimo dia

Lab=CargarFichero('Ruta')

E,S=Find(E,S)

def percibirEntorno(Laberinto,PosX,PosY){
	return ListaDeMovimientosDisponibles
}

// Señalar cuando no hay movimiento disponible como -1
while(!salidaEncontrada && pasos<1000 && numeroDeMovimiento!=-1){ // agregar que si no hay movimientos, acabe de buscar 
	int mov = Agente.mover(ListaMov,Pos,Lab) // Reactivo = una opcion random // Deliberativo = Pensando
}

Agente.actualizarPos(mov,pos){ return posicion}


Mensajes finales:

Posicion final: (X,Y), Salida en (X,Y)

Solucion Encontrada

Acciones: 1000

Laberinto recorrido


// Mover del Reactivo

moverReactivo(ListaMov){
	if (ListaMov.isEmpty()){
		return numeroDeMovimiento=-1
	} else {
		return mover(randint(ListaMov.leng()-1))
	}
}

moverDeliberativo(ListaMov){
        if (ListaMov.isEmpty()){ 
                return numeroDeMovimiento=-1
        } else {            
                for mov in movimientosDisponibles	 //comprobar que todas las ubicaciones hayan sido visitadas, si es asi, moverse a una ya recorrida
		return mover(randint(ListaMov.leng()-1))
        }
}
