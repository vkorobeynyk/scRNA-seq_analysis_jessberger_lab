## Aim

Transcriptional comparison between Gli1- and Ascl1- targeted neuronal stem cells (NSCs) isolated from the adult mouse hippocampus.

## Repository structure

Tasks (`01`, `02`, etc) subfolders contain both source code in R (`Rmd` files) and the rendered HTML reports.

- `01_data_processing_integration`, scater's QC; Seurat's integration, dimensionality reduction and clustering.
- `02_differential_analysis`, differential expression analysis (Seurat-based).
- `03_velocity_steady-state_model`, Inference of steady state model RNA velocity (velocyto.R)
- `04_velocity_dynamical_model`, Inference of RNA velocity (scVelo)
- `05_prediction_RF_KNN_GLM`, `velocyto.R`, Machine learning approaches for prediction Gli vs Ascl cells
- `06_prediction_SVM`, Application of SVM for prediction Gli vs Ascl cells

## Requirements

Data analysis was carried out in R v3.6.1. A shortlist of the package versions include:


R packages

```
 package                version   date        source        
 biomaRt                2.40.0    2019-05-02  Bioconductor  
 edgeR                  3.28.0    2019-06-21  Bioconductor  
 ggplot2                3.2.0     2019-06-16  CRAN (R >3.6.0)
 limma                  3.41.6    2019-05-17  Bioconductor  
 Rtsne                  0.15      2018-11-10  CRAN
 scater                 1.13.9    2019-05-24  Bioconductor  
 Seurat                 3.1.2     2019-12-13  CRAN (R ≥3.6.0)
 purrr                  0.3.2	  2019-03-15  CRAN (R ≥3.6.1)
 dplyr			        0.8.3	  2019-07-04  cran (R ≥3.6.1)
 caret                  6.0.85    2020-01-07  cran (R ≥3.2.0)
 cowplot                0.9.4     2019-07-11  CRAN (R ≥3.5.0)
 velocyto.R             0.6                   devtools::install_github("velocyto-team/velocyto.R")
 bmrm                   4.1.0     2019-04-03  CRAN (R ≥ 3.0.2)
 e1071                  1.7.2     2019-11-26  CRAN
 fastICA                1.2.2     2019-07-08  CRAN (R ≥ 3.0.0)
 CellMixS               1.1.0                 Bioconductor(R ≥ 3.6.0
```

Python packages

```
 package              version  
 scvelo               0.1.24
 scanpy               1.4.5
 loompy               3.0.6
 numpy                1.18.1
 pandas               0.25.3
```
