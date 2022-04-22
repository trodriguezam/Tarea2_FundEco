class mercado:

    def __init__(self, DAPmax, COmin, d, s):
        """
        Configura los parámetros del mercado. DAPmax es la máxima disposición a 
        pagar de cualquier consumider-el intercepto con el eje y de la función 
        de demanda. COmin es el mínimo costo oportunidad de cualquier productor-el 
        intercepto con el eje y de la función de oferta. s es la pendiente de la f
        unción de oferta. d es la pendiente de la función de demanda...
        """
        
        self.DAPmax, self.COmin, self.d, self.s = DAPmax, COmin, d, s
        
        if DAPmax < COmin:
            raise ValueError('Demanda insuficiente.')

    def cantidad_equilibrio(self):
        "Cálculo cantidad de equilibrio"
        return  (self.DAPmax - self.COmin)/(self.d + self.s)

    def precio_equilibrio(self):
        "Cálculo cantidad de equilibrio"
        return  self.DAPmax - self.d * self.cantidad_equilibrio()

    def excedente_consumidor(self):
        "Cálculo excedente consumidor"
        return (self.DAPmax - self.precio_equilibrio())*self.cantidad_equilibrio()/2

    def excedente_productor(self):
        "Cálculo excedente productor"
        return (self.precio_equilibrio() - self.COmin) * self.cantidad_equilibrio() /2

    def excedente_total(self):
        "Cálculo excedente total"
        return self.excedente_productor() + self.excedente_consumidor()
    
    def demanda(self,x):
        "Función demanda"
        return self.DAPmax - self.d*x
        
    def oferta(self,x):
        "Función oferta"
        return self.COmin + self.s*x

import numpy as np
import matplotlib.pyplot as plt

# Parámetros iniciales DAPmax, COmin, d, s
params_ini = 10730,4740,24500000,5800000
m = mercado(*params_ini)

q_max = m.cantidad_equilibrio() * 2
q_grid = np.linspace(0.0, q_max, 100)
pd = m.demanda(q_grid)
ps = m.oferta(q_grid)

fig, ax = plt.subplots()
ax.plot(q_grid, pd, lw=2, alpha=0.6, label='demanda')
ax.plot(q_grid, ps, lw=2, alpha=0.6, label='oferta')
ax.set_xlabel('cantidad', fontsize=14)
ax.set_xlim(0, q_max)
ax.set_ylabel('precio', fontsize=14)
ax.legend(loc='lower right', frameon=False, fontsize=14)
ax.set(title='Oferta, Demanda y Equilibrio de mercados')
plt.show()

print("Excedente productor =",m.excedente_productor())
print("Excedente consumidor =",m.excedente_consumidor())
print("Excedente total =",m.excedente_total())
print("Cantidad de equilibrio =",m.cantidad_equilibrio())
print("Precio de equilibrio =",m.precio_equilibrio())