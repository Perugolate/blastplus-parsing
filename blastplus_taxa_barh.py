#! /usr/bin/python
# takes 4 arguments: blast output in format 6; field no. for taxa descriptions; no. of taxa to plot; filename for plot
# requires pandas and matplotlib

import sys
from pandas import DataFrame
import pandas
import matplotlib.pyplot as plt

in_file = sys.argv[1]
tax_field = int(sys.argv[2])
num_tophits = int(sys.argv[3])
out_file = sys.argv[4]

def blast_in(in_file):
  blast_data = pandas.read_table(in_file,header = None)
  blast_data = DataFrame(blast_data)
  return blast_data

def genus(blast_data):
  desc = blast_data[tax_field]
  desc = desc.str.split(' ').str.get(0)
  desc = desc.str.split(';').str.get(0)
  desc = desc.value_counts()
  topfreq_desc = desc[:num_tophits]
  return topfreq_desc

def plot_out(topfreq_desc):
  fig = plt.figure()
  topfreq_desc.plot(kind='barh')
  plt.title("Top blast hits")
  plt.xlabel("Number of best hits")
  plt.ylabel("Taxa")
  fig.tight_layout()
  fig.savefig(out_file, dpi=fig.dpi)
  
blast_data = blast_in(in_file)
topfreq_desc = genus(blast_data)
plot_out(topfreq_desc)
