#! /usr/bin/python
"""
Usage: blastplus_taxa_barh.py blast_output staxids_field no_taxa plot_filename

Arguments:
	blast_ouput
 		output from BLAST 2.2.28+ and later in outfmt 6 containing staxids 
	staxids_field
		field in blast output containing staxids (Genus species)
	no_taxa
		number of taxa to include in the horizontal bar plot
	plot_filename
		filename for plot .png

example blast invocation which places staxids in field 13:
blastx -query query.fasta -db refseq_protein -max_target_seqs 1 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send stitle staxids sscinames evalue" -out blast_out

Paul Johnston (Paul.Johnston@fu-berlin.de)
"""

import sys
import pandas
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


__author__ = "Paul Johnston"
__contact__ = "paul.johnston@fu-berlin.de"


def blast_in(in_file):
    blast_data = pandas.read_table(in_file,header = None)
    blast_data = pandas.DataFrame(blast_data)
    return blast_data

def genus(blast_data, tax_field, num_tophits):
    desc = blast_data[tax_field]
    desc = desc.str.split(' ').str.get(0)
    desc = desc.str.split(';').str.get(0)
    desc = desc.value_counts()
    topfreq_desc = desc[:num_tophits]
    return topfreq_desc

def plot_out(topfreq_desc, out_file):
    fig = plt.figure() 
    topfreq_desc.plot(kind='barh')
    plt.title("Top blast hits")
    plt.xlabel("Number of best hits")
    plt.ylabel("Taxa")
    fig.tight_layout()
    fig.savefig(out_file, dpi=fig.dpi)
    
def plot_in(topfreq_desc):
    fig = plt.figure()
    topfreq_desc.plot(kind='barh')
    plt.title("Top blast hits")
    plt.xlabel("Number of best hits")
    plt.ylabel("Taxa")
    fig.tight_layout()

def main():

    if len(sys.argv) < 5:
        print __doc__
        sys.exit(0)

    in_file = sys.argv[1]
    tax_field = int(sys.argv[2])-1
    num_tophits = int(sys.argv[3])
    out_file = sys.argv[4]

    blast_data = blast_in(in_file)
    topfreq_desc = genus(blast_data, tax_field, num_tophits)
    plot_out(topfreq_desc, out_file)

if __name__ == '__main__':
    main()
