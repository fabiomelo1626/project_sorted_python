from PyQt5 import uic, QtWidgets
import random


def primeira_tela():#função pra criar a lista.
    n = formulario.lineEdit.text()
    n1 = formulario.lineEdit_2.text()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    sequence = range(int(n), int(n1))
    lista = list(sequence)
    print('retorna a lista: ', lista)
    pag.show()
    return lista

def sorteio(lista):#printar a lista na segunda tela, mas não vai
    pag.textBrowser(lista)

app = QtWidgets.QApplication([])
formulario = uic.loadUi("untitled.ui")
pag = uic.loadUi("sorted.ui")
formulario.pushButton.clicked.connect(primeira_tela)
#formulario.pushButton_2.clicked.connect(segunda_tela)
pag.pushButton.clicked.connect(sorteio)

formulario.show()
app.exec()
