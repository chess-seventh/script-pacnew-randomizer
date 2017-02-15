import random, sys, os
from shutil import copyfile



#PATH = '/home/seventh/work_progress/randomizer/GitKiff/'
#FILE_OG = 'mirrorlist.pacnew.orig'
#ALL_OG = PATH + FILE_OG

PATH = "/etc/pacman.d/"
FILE = 'mirrorlist.pacnew'

ALL = PATH + FILE
ME = PATH + 'mirrorlist'

MAX = 10


"""
Class that handles all my server changes
no need of inputs for init() the class

"""

class Bloc(object):
  def __init__(self):
    self.my_servers = []
    self.all_servers = []
    self.qty = []
    self.swiss = []
    self.country = ""


"""
Function that runs all the function needed for an output
"""
  def run_all(self):
    self.remove_header()
    self.run_file()
    self.run_rand()
    self.write_mirrorlist()


"""
Function that fills my servers after getting the random values.
"""
  def run_rand(self):
    tot = MAX + len(self.swiss)
    num_ser = []
    i = 0
    for a in range(tot+1):
      num_ser.append(self.rdm())
    num_ser.sort()
    num_ser =  list(set(num_ser))
    for s in range(len(self.all_servers)):
      if s == num_ser[i]:
        self.my_servers.append((self.all_servers[s]))
        i = i+1


"""
Function that ends the process
"""
  def write_mirrorlist(self):
    open(ME, 'w').close()
    with open(ME, 'w') as f:
      for i in self.my_servers:
        f.write("%s" % i)
      for i in self.swiss:
        f.write("%s" % i)
      f.close()


"""
Function that opens the new mirrorlist and appends all servers
"""
  def run_file(self):
    with open(FILE, 'r') as f:
      for l in f:
        if (self.is_country(l)):
          self.do_country(l)
        if (self.is_swiss() and (self.is_server(l))):
          self.swiss.append(self.modifier(l))
        if (self.is_server(l) and not (self.is_swiss())):
          self.all_servers.append(self.modifier(l))
      f.close()


"""
Function that stores the current country in Bloc
Returns False if the line is empty
"""
  def do_country(self, l):
    if l.strip():
      self.country = ' ' + l[1:]
      return True
    return False
    
  def is_server(self, n):
    if n[1:7] == 'Server':
      return True
    return False

  def is_country(self, l):
    if l[:2] == '##':
      return True
    return False

  def remove_header(self):
    if not FILE == "":
      with open(FILE, 'r') as fin:
        data = fin.read().splitlines(True)
      with open(FILE, 'w') as fout:
        fout.writelines(data[5:])
      return True

  def is_swiss(self):
    if ("".join(self.country.split())[1:] == 'Switzerland'):
      return True
    if ("".join(self.country.split())[1:] == 'Worldwide'):
      return True
    return False

  def rdm(self):
    return (random.randint(0, len(self.all_servers)))

  def modifier(self, line):
    l = line.split('\n')
    l[1] += self.country + '\n'
    line = "".join(l)
    return (line[1:])

def main():
  myBloc = Bloc()
  myBloc.run_all()

  #This line below can be removed
  #copyfile(FILE_OG, FILE)

if __name__ == '__main__':
  main()
