README
======
Trivial, quick and dirty horizontal bar plot of top blast hits from BLAST 2.2.28+ and later. Takes four arguments: blastplus output in tabular format (-outfmt 6), the column no. for the taxonomy descriptions (sscinames), the number of taxa to plot, and a filename.extension for the plot. Note this depends on the "sscinames" option in BLAST 2.2.28+ and later which gives the scientific name taxon name of the blast hits. 

```bash
#e.g. blast invocation placing scientific names (sscinames) in the 13th column:
blastx -query query.fasta -db refseq_protein -max_target_seqs 1 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send stitle staxids sscinames evalue" -out blast_out
```

##Dependencies:
- pandas
- matplotlib

###Note
To include taxon scientific names in the blast output you must download the taxdb from NCBI and place it visible to blast e.g. by placing it in the BLASTDB path of you `~/.ncbirc` file:
```bash
mkdir /path/to/your_taxdb_dir/ && cd /path/to/your_taxdb_dir/
wget ftp://ftp.ncbi.nlm.nih.gov/blast/db/taxdb.tar.gz
tar xvf taxdb.tar.gz
```
Then add the directory to BLASTDB in `~/.ncbirc` so that it looks like:
```
[BLAST]
BLASTDB=/path/to/your_taxdb_dir/:/path/to/your_blastdb_dir1/:/path/to/your_blastdb_dir2/
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
