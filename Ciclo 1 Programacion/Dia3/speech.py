#EXERCICE 
import random

LAMBETAZO = ["QUERIDOS", "APRECIADOS", "DISTINGUIDOS", "HONORABLES", "ESTIMADOS", "RESPETADOS"]
POTENCIALES_MARRANOS = ["COMPATRIOTAS", "CIUDADANOS", "AMIGOS", "COTERANEOS", "COPARTIDARIOS", "ELECTORES"]
CONDICION = ["EN MI GOBIERNO", "CON SU APOYO", "SIENDO ELEGIDO", "CON SU AYUDA", "SI ME SIGUEN", "DURANTE MI MANDATO"]
COMPROMISO = ["VOY A DERROTAR", "VENCERE", "ELIMINARE", "ACABARE", "LUCHARE CONTRA", "COMBATIRE"]
ILUSION_GUERRERISTA = ["LA VIOLENCIA Y", "LA DELINCUENCIA Y", "LA CORRUPCION Y", "LA INFLACION Y", "LA POBREZA Y", "EL DESPLAZAMIENTO Y"]
PROMESA = ["TRABAJARE POR", "GARANTIZARE", "PROTEGERE", "VELARE POR", "PROMOVERE", "DEFENDERE"]
BENEFICIO_POPULISTA = ["LA EDUCACION", "EL EMPLEO", "LA SEGURIDAD", "LA PAZ", "LA IGUALDAD", "LA SALUD"]
DEPENDIENDO_DE_LA_CANTIDAD_DE_VOTOS = ["DEL PAIS", "DE LA CIUDAD", "DE LA COMUNIDAD", "DE LA POLACION", "PARA TODA LA GEGNTE", "DE CADA COLOMBIANO"]

#PRINT

print(random.choice(LAMBETAZO) + " " + random.choice(POTENCIALES_MARRANOS) + " " + random.choice(CONDICION) + " " + random.choice(COMPROMISO) + " " 
+ random.choice(ILUSION_GUERRERISTA) + " " + random.choice(PROMESA) + " " +random.choice(BENEFICIO_POPULISTA)+ " " + random.choice(DEPENDIENDO_DE_LA_CANTIDAD_DE_VOTOS))
