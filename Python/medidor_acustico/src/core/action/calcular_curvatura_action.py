class CalcularCurvaturaAction:

    def execute(self, t20, t30):
        return 100 * ((t30 / t20) - 1)
