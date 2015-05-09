README
======
Trivial, quick and dirty horizontal bar plot of top blast hits from BLAST 2.2.28+ and later. Takes four arguments: blastplus output in tabular format (-outfmt 6), the column no. for the taxonomy descriptions (staxids), the number of taxa to plot; a filename for the plot. Note this script relies on the "staxids" option in BLAST 2.2.28+ and later which gives the Subject Taxonomy ID. 

```bash
#e.g. blast invocation:
blastx -query query.fasta -db refseq_protein -max_target_seqs 1 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send stitle staxids sscinames evalue" -out blast_out
```

##Dependencies:
- pandas
- matplotlib

To include taxon names in the blast output you must download the taxdb from NCBI and place it in the same directory as your blastdb. The easiest option is to place it into your BLASTDB directory (e.g. wherever your `~/.ncbirc` file points to)
```bash
wget ftp://ftp.ncbi.nlm.nih.gov/blast/db/taxdb.tar.gz
tar xvf taxdb.tar.gz
```

##Usage

```bash
python blastplus_taxa_barh.py blast_output staxids_field no_taxa plot_filename.extension
```
for example plot the top 15 taxa from the blast output file `blast_out`:
```bash
python blastplus_taxa_barh.py blast_out 13 15 taxa_plot.png
```

![](https://github.com/Perugolate/blastplus-parsing/blob/master/taxa_plot.png)


Lepidopteran assembly heavily contmainated with yeast:

![](https://github.com/Perugolate/blastplus-parsing/blob/master/contam.png)

##More examples

Some more examples in jupyter [notebook](https://github.com/Perugolate/blastplus-parsing/blob/master/parse_blast_tax_names_eg.ipynb).
