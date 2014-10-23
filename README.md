README
======
Quick and dirty horizontal bar plot of top blast hits from BLAST 2.2.28+ and later. Takes four arguments: blastplus output in tabular format (-outfmt 6), the column no. for the taxonomy descriptions (staxids), the number of taxa to plot; a filename for the plot. Note this script relies on the "staxids" option in BLAST 2.2.28+ and later which gives the Subject Taxonomy ID. 

```bash
#e.g. blast invocation:
blastx -query query.fasta -db refseq_protein -max_target_seqs 1 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send stitle staxids sscinames evalue" -out blast_out
```

Usage
-----
```bash
python blastplus_taxa_barh.py blast_out 13 10 plot.pdf
```
