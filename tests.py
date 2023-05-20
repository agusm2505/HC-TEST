import unittest
import os
import checkpoint as ch

class HenryChallenge(unittest.TestCase):
    def test_OrdenarDiccionario_01(self):
      dicc = {'clave1':['c','a','b'], 'clave2':['casa','auto','barco'], 'clave3':[3,1,2]}
      valor_test = ch.ordenarDiccionario(dicc, 'clave1')
      valor_esperado = {'clave1':['c','b','a'], 'clave2':['casa','barco','auto'], 'clave3':[3,2,1]}
      self.assertEqual(valor_test, valor_esperado)

    def test_OrdenarDiccionario_02(self):
      dicc = ['c','a','b']
      valor_test = ch.ordenarDiccionario(dicc, 'clave1', True)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_OrdenarDiccionario_03(self):
      dicc = {'clave1':['c','a','b'], 'clave2':['casa','auto','barco'], 'clave3':[3,1,2]}
      valor_test = ch.ordenarDiccionario(dicc, 'clave1', False)
      valor_esperado = {'clave1':['a','b','c'], 'clave2':['auto','barco','casa'], 'clave3':[1,2,3]}
      self.assertEqual(valor_test, valor_esperado)
    
    def test_ListaEnteros_01(self):
      lista_test = ch.listaEnteros(1, 10)
      lista_esperada = [1,2,3,4,5,6,7,8,9,10]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaEnteros_02(self):
      lista_test = ch.listaEnteros(3, 8)
      lista_esperada = [3,4,5,6,7,8,9,10]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaEnteros_03(self):
      lista_test = ch.listaEnteros(-2, 4)
      lista_esperada = [-2,-1,0,1]
      self.assertEqual(lista_test, lista_esperada)
    
    def test_DividirDosNumeros_01(self):
      parte_entera, resto = ch.dividirDosNumeros(10, 5)
      lista_test = [parte_entera, resto]
      lista_esperada = [2,0]
      self.assertEqual(lista_test, lista_esperada)

    def test_DividirDosNumeros_02(self):
      parte_entera, resto = ch.dividirDosNumeros(17, 3)
      lista_test = [parte_entera, resto]
      lista_esperada = [5,2]
      self.assertEqual(lista_test, lista_esperada)

    def test_DividirDosNumeros_03(self):
      parte_entera, resto = ch.dividirDosNumeros(13, 3)
      lista_test = [parte_entera, resto]
      lista_esperada = [4,1]
      self.assertEqual(lista_test, lista_esperada)
    
    def test_ClaseAnimal_01(self):
      a = ch.claseAnimal('perro','negro')
      valor_test = a.CumplirAnios()
      valor_test = a.CumplirAnios()
      valor_test = a.CumplirAnios()
      valor_esperado = 3
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseAnimal_02(self):
      a = ch.claseAnimal('ballena','azul')
      for i in range(0,10):
        valor_test = a.CumplirAnios()
      valor_esperado = 10
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseAnimal_03(self):
      a = ch.claseAnimal('tortuga','verde')
      for i in range(0,100):
        valor_test = a.CumplirAnios()
      valor_esperado = 100
      self.assertEqual(valor_test, valor_esperado)
    
    def test_Exponente_01(self):
      valor_test = ch.exponente(10, 2)
      valor_esperado = 100
      self.assertEqual(valor_test, valor_esperado)

    def test_Exponente_02(self):
      valor_test = ch.exponente(49, 0.5)
      valor_esperado = 7
      self.assertEqual(valor_test, valor_esperado)

    def test_Exponente_03(self):
      valor_test = ch.exponente(3, 0)
      valor_esperado = 1
      self.assertEqual(valor_test, valor_esperado)
    
    def test_ListaPrimos_01(self):
      lista_test = ch.listaPrimos(1,11)
      lista_esperada = [1,2,3,5,7,11]
      self.assertEqual(lista_test, lista_esperada)
      
    def test_ListaPrimos_02(self):
      lista_test = ch.listaPrimos('0',0)
      lista_esperada = None
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaPrimos_03(self):
      lista_test = ch.listaPrimos(66,77)
      lista_esperada = [67, 71, 73]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaPrimos_04(self):
      lista_test = ch.listaPrimos(0,'66')
      lista_esperada = None
      self.assertEqual(lista_test, lista_esperada)
    
    def test_ListaRepetidos_01(self):
      lista_test = ch.listaRepetidos(['hola', 'mundo', 'hola']) 
      lista_esperada = [('hola',2),('mundo',1)]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaRepetidos_02(self):
      lista_test = ch.listaRepetidos([10,11,11,12,15,17,20,20])
      lista_esperada = [(10,1),(11,2),(12,1),(15,1),(17,1),(20,2)]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaRepetidos_03(self):
      lista_test = ch.listaRepetidos((1,2,3,3))
      lista_esperada = None
      self.assertEqual(lista_test, lista_esperada)
    
resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

hc_tests = resultado_test.result.testsRun
hc_fallas = len(resultado_test.result.failures)
hc_errores = len(resultado_test.result.errors)
hc_ok = hc_tests - hc_fallas - hc_errores

archivo_test = open('resultado_test.csv', 'w')
archivo_test.write('Total_Tests,Total_Fallas,Total_Errores,Total_Correctos\n')
archivo_test.write(str(hc_tests)+','+str(hc_fallas)+','+str(hc_errores)+','+str(hc_ok)+'\n')
archivo_test.close()

print('Resumen')
print('Total Tests:', str(hc_tests))
print('Total Fallas:', str(hc_fallas))
print('Total Errores:', str(hc_errores))
print('Total Correctos:', str(hc_ok))
