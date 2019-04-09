import tkinter
from tkinter import ttk

from matplotlib import pyplot


class Estilista:

    def definir_estilos_ttk(self):

            style_medidor = ttk.Style()
            if not style_medidor.theme_names().__contains__('medidor_acustico'):

                settings = {"TNotebook.Tab": {"configure": {"padding": [5, 2],
                                                            "background": "#fdd57e"
                                                            },
                                              "map": {"background": [("selected", "#bb3939"),
                                                                     ("active", "#fdadc7"),
                                                                     ("!disabled", "#5e0606")],
                                                      "foreground": [("selected", "#ffffff"),
                                                                     ("active", "#000000"),
                                                                     ("!disabled", "#ffffff")]

                                                      }
                                              },
                            "TNotebook": {"configure": {"background": "#831212"}
                                          },
                            "TProgressbar": {"configure": {"background": "#5893d4",
                                                           "troughcolor": "#5e0606",
                                                           }
                                             }
                            }
                style_medidor.theme_create("medidor_acustico", parent="alt", settings=settings)

            style_medidor.theme_use("medidor_acustico")

    def definir_estilos_graficas(self):
        pyplot.style.use('seaborn-darkgrid')

    def definir_fuentes(self, root):
        root.option_add("*font", "Helvetica 9")