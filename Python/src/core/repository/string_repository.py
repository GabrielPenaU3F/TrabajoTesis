class StringRepository:

    def __init__(self):

        self.string_instrucciones = "INSTRUCCIONES DE USO:\n\n\n" \
                                    "La aplicación medirá la respuesta impulsional " \
                                    "de la sala y a partir de ella calculará la " \
                                    "curva de decaimiento del sonido y los tiempos " \
                                    "de reverberación EDT, T20 y T30 tal como están, " \
                                    "definidos en las normas ISO 3382-1 y 3382-2.\n\n" \
                                    "MEDICIÓN:\n" \
                                    "La respuesta impulsional puede medirse utilizando dos métodos: " \
                                    "el MLS (secuencia pseudoaleatoria) y el ESS (senoide con frecuencia" \
                                    "modulada exponencialmente). Se recomienda para la mayoría de las " \
                                    "aplicaciones el método ESS, por ser más resistente al ruido.\n" \
                                    "Asegúrese de no causar ruidos espurios que contaminen la medición " \
                                    "mientras ésta se esté efectuando.\n" \
                                    "Se recomienda que el micrófono se encuentre a al menos dos metros de " \
                                    "la fuente de sonido y a al menos un metro del suelo, " \
                                    "preferentemente en la localización usual de los oyentes.\n\n"\
                                    "Mejorar la calidad de la medición en términos de linealidad " \
                                    "requiere mejorar el hardware utilizado (altavoces, tarjetas " \
                                    "de audio, micrófonos).\n\n" \
                                    "BANDAS DE FRECUENCIA:\n" \
                                    "También pueden visualizarse los resultados por banda " \
                                    "de frecuencia, tanto de octava como de tercio de octava, en la " \
                                    "Vista Detallada."


        self.string_parametros_linealidad = "PARÁMETROS DE LINEALIDAD:\n" \
                                            "Los tres valores adicionales son parámetros representativos " \
                                            "del carácter lineal de la curva de decaimiento, definidos " \
                                            "en la norma ISO 3382-2.\n" \
                                            "El valor r es el coeficiente de correlación lineal. Si " \
                                            "difiere mucho de -1, la medición no se considera buena.\n" \
                                            "El valor ξ es el parámetro de no-linealidad de la curva. " \
                                            "Indica cuanto se aleja la curva, en pormilaje, " \
                                            "de la linealidad perfecta. Se consideran buenos valores " \
                                            "de 0 a 5‰.\n" \
                                            "El valor C es el parámetro de curvatura. Mide, en porcentaje, " \
                                            "cuan diferentes son los tiempos T20 y T30. Valores típicos son " \
                                            "de 0 a 5%.\n" \

        self.string_error_lundeby = "Lo sentimos, se ha producido un error\n" \
                                    " durante la estimación de la curva de\n" \
                                    " decaimiento. Por favor, intente repetir \n" \
                                    "la medición nuevamente."


    def get_string_instrucciones(self):
        return self.string_instrucciones

    def get_mensaje_error_lundeby(self):
        return self.string_error_lundeby
