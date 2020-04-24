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

* `annotateBinary(input_id, input_chr, input_start, input_end, annot_id = NULL, annot_chr, annot_start, annot_end)` 
                
  __inputs__:
  * **input_id**: Character vector defining the name of input genomic regions (e.g. gene id)
  * **input_chr**: 	Character vector defining the name of the chromosome for input genomic regions (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **input_start**: Numeric vector specifying the starting position of input genomic regions.
  * **input_end**: Numeric vector specifying the ending position of input genomic regions.
  * **annot_id**: Optional (NULL by default): Character vector defining the name or ID of each annotation entry. If NULL, the row numbers (indexes) are used as IDs.
  * **annot_chr**: Character vector defining the name of the chromosome for annotation entries (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **annot_start**: Numeric vector specifying the starting position of annotation entries.
  * **annot_end**: Numeric vector specifying the ending position of annotation entries.
  
   __outputs__:
   * **input_ID**: Character vector defining the name of input genomic regions (e.g. gene id)
   * **input_chr**: Character vector defining the name of the chromosome for input genomic regions (one of chr1, chr2, ..., chrX, chrY or chrM).
   * **input_start**: Numeric vector specifying the starting position of input genomic regions.
   * **input_end**: Numeric vector specifying the ending position of input genomic regions.
   * **overlap_count**: Numeric vector specifying the count of overlapped annotations with that geneID.
   * **overlapping_annot_IDs**: Character vector specifying the IDs of overlapped annotations with that geneID (separated by comma).

  
* `annotateMultiScore(input_id, input_chr, input_start, input_end, annot_chr, annot_start, annot_end, annot_sub_id, annot_sub_score)` 
                
  __inputs__:
  * **input_id**: Character vector defining the name of input genomic regions (e.g. gene id)
  * **input_chr**: Character vector defining the name of the chromosome for input genomic regions (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **input_start**: Numeric vector specifying the starting position of input genomic regions.
  * **input_end**: Numeric vector specifying the ending position of input genomic regions.
  * **annot_chr**: Character vector defining the name of the chromosome for annotation entries (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **annot_start**: Numeric vector specifying the starting position of annotation entries.
  * **annot_end**: Numeric vector specifying the ending position of annotation entries.
  * **annot_sub_ids**: Character vector defining sets of sub-IDs for annotation entries (separated by comma).
  * **annot_sub_score**: Character vector defining sets of sub-scores for annotation entries (separated by comma). 
  
   __outputs__:
   * **input_ID**: Character vector specifying the operlapping annotation ids of output (separated by comma).
    * **input_chr**: Character vector defining the name of the chromosome for input genomic regions (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **input_start**: Numeric vector specifying the starting position of input genomic regions.
  * **input_end**: Numeric vector specifying the ending position of input genomic regions.
   * **overlap_sub_ids**: The sub-IDs of annotation entries that overlap with each input region (separated by comma).
   * **overlap_sub_scores**: CThe average score of annotation for each overlapping sub-ID over each input region (separated by comma).
   * **overlap_sub_percentages**: The percentage of overlap between each input region and its overlapping sub-IDs (separated by comma).


* `annotateSingleScore(input_id, input_chr, input_start, input_end, annot_chr, annot_start, annot_end, annot_score)` 
                
  __inputs__:
  * **input_id**: Character vector defining the name of input genomic regions (e.g. gene id)
  * **input_chr**: Character vector defining the name of the chromosome for input genomic regions (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **input_start**: Numeric vector specifying the starting position of input genomic regions.
  * **input_end**: Numeric vector specifying the ending position of input genomic regions.
  * **annot_chr**: Character vector defining the name of the chromosome for annotation entries (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **annot_start**: Numeric vector specifying the starting position of annotation entries.
  * **annot_end**: Numeric vector specifying the ending position of annotation entries.
  * **annot_score**: Numeric vector specifying scores for annotation entries (separated by comma). 
  
   __outputs__:
   * **input_ID**: Character vector specifying the operlapping annotation ids of output (separated by comma).
    * **input_chr**: Character vector defining the name of the chromosome for input genomic regions (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **input_start**: Numeric vector specifying the starting position of input genomic regions.
  * **input_end**: Numeric vector specifying the ending position of input genomic regions.
   * **overlap_score**: The average score of annotation over each input region.
   * **overlap_percentage**: The percentage of overlap between each input region and annotation entries.

  
* `annotateCategorical(input_id, input_chr, input_start, input_end, annot_chr, annot_start, annot_end, annot_category)` 
                
  __inputs__:
  * **input_id**: Character vector defining the name of input genomic regions (e.g. gene id)
  * **input_chr**: Character vector defining the name of the chromosome for input genomic regions (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **input_start**: Numeric vector specifying the starting position of input genomic regions.
  * **input_end**: Numeric vector specifying the ending position of input genomic regions.
  * **annot_chr**: Character vector defining the name of the chromosome for annotation entries (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **annot_start**: Numeric vector specifying the starting position of annotation entries.
  * **annot_end**: Numeric vector specifying the ending position of annotation entries.
  * **annot_category**: Character vector specifying categories for annotation entries.
  
   __outputs__:
   * **input_ID**: Character vector specifying the operlapping annotation ids of output (separated by comma).
    * **input_chr**: Character vector defining the name of the chromosome for input genomic regions (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **input_start**: Numeric vector specifying the starting position of input genomic regions.
  * **input_end**: Numeric vector specifying the ending position of input genomic regions.
   * **overlapping_categories**: The categories that overlap with each input region (separated by comma).
   * **overlapping_percentage**: The percentages of overlaps between each input region and its overlapping categories (separated by comma).
   

* `findHiCinteractions(input_id, input_chr, input_start, input_end, hic_f1_id, hic_f1_chr, hic_f1_start, hic_f1_end, hic_f2_id, hic_f2_chr, hic_f2_start, hic_f2_end, target_id, target_chr, target_start, target_end)` 
                
  __inputs__:
  * **input_id**: Character vector defining the name of input genomic regions (e.g. gene id)
  * **input_chr**: Character vector defining the name of the chromosome for input genomic regions (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **input_start**: Numeric vector specifying the starting position of input genomic regions.
  * **input_end**: Numeric vector specifying the ending position of input genomic regions.
  * **hic_f1_id**: Character defining the ID for left fragments of Hi-C interactions.
  * **hic_f1_chr**: Character vector defining the name of the chromosome for left fragments of Hi-C interactions (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **hic_f1_start**: Numeric vector specifying the starting position of left fragments of Hi-C interactions.
  * **hic_f1_end**: Numeric vector specifying the ending position of left fragments of Hi-C interactions.
  * **hic_f2_id**: Character defining the ID for left fragments of Hi-C interactions.
  * **hic_f2_chr**: Character vector defining the name of the chromosome for left fragments of Hi-C interactions (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **hic_f2_start**: Numeric vector specifying the starting position of left fragments of Hi-C interactions.
  * **hic_f2_end**: Numeric vector specifying the ending position of left fragments of Hi-C interactions.
  * **target_id**: Character vector defining the name of target genomic regions (e.g. gene id)
  * **target_chr**: Character vector defining the name of the chromosome for target genomic regions (one of chr1, chr2, ..., chrX, chrY or chrM).
  * **target_start**: Numeric vector specifying the starting position of target genomic regions.
  * **target_end**: Numeric vector specifying the ending position of target genomic regions.
  
   __outputs__:
   A list of two data.frames:

  The first data.frame contains the input genomic regions and 3 extra columns which specify:

  1. The number of target genomic regions that interact with each input genomic region through Hi-C interactions.

  2. The IDs of target genomic regions that interact with each input genomic region through Hi-C interactions (separated by comma).

  3. The IDs of Hi-C interactions that connect each input genomic region with target genomic regions (separated by comma).

  The second data.frame provides further information about each Hi-C interaction. It specifies the genomic regions of the left and right Hi-C fragments. Furthermore, the IDs of input genomic regions and target genomic regions that interact through these Hi-C interactions are listed in each row (separated by comma).
