# SomaGene 
  
  some explanation and logo ans stuffs //TODO

  
  
## Installation 
  
### Requirements
  * [S4Vectors](https://bioconductor.org/packages/release/bioc/html/S4Vectors.html)
  * [GenomicRanges](https://bioconductor.org/packages/release/bioc/html/GenomicRanges.html)
  
  
```r
# Install SomaGene from source
install.packages("THE_SOURCE_DIR", repos = NULL, type = "source")

# Or the development version from GitHub:
devtools::install_github("r-lib/devtools")
```

## Usage

* `annotateBinary(input_id, input_chr, input_start, input_end,
                annot_id = NULL, annot_chr, annot_start, annot_end)` 
                
  __inputs__:
  * *input_id*: Character vector defining the name of input genomic regions (e.g. gene id)
  * *input_chr*: 	Character vector defining the name of the chromosome for input genomic regions (one of chr1, chr2, ..., chrX, chrY or chrM).
  * *input_start*: Numeric vector specifying the starting position of input genomic regions.
  * *input_end*: Numeric vector specifying the ending position of input genomic regions.
  * *annot_id*: Optional (NULL by default): Character vector defining the name or ID of each annotation entry. If NULL, the row numbers (indexes) are used as IDs.
  * *annot_chr*: Character vector defining the name of the chromosome for annotation entries (one of chr1, chr2, ..., chrX, chrY or chrM).
  * *annot_start*: Numeric vector specifying the starting position of annotation entries.
  * *annot_end*: Numeric vector specifying the ending position of annotation entries.
  
  
  
