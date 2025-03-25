import numpy as np
import matplotlib.pyplot as plt
import time

def plotar_automato(automato):
    plt.figure(figsize=(10, 10))
    plt.imshow(automato, cmap='binary', interpolation='nearest')
    plt.axis('off')
    plt.show()

def automato():
  CELLS = 32
  STEPS = 15

  cells = [0] * CELLS
  old= cells.copy()
  historico = [old]

  cells[CELLS // 2] = 1

  for t in range(STEPS):
    for i in range(CELLS): 
      old[i] = cells[i]

    for i in range(1, CELLS - 1):
        if old[i - 1] + old[i + 1] > 0:
            cells[i] = 1
        else:
            cells[i] = 0

    historico.append(cells.copy())
  return historico

if __name__ == "__main__":
    automato = automato()

    prin_aut = automato.copy()

    for i in range(len(automato)):
      new_line = automato[i].copy()
      # print(i)
      for cell in range(len(automato[i])):
        if automato[i][cell] == 1:
          new_line[cell] = "█"
        else:
          new_line[cell] = " "
      prin_aut[i] = new_line
    
    for i in range(len(prin_aut)):
      print(prin_aut[i])
 