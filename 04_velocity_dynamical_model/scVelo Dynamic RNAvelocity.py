#!/usr/bin/env python
# coding: utf-8
# %%


import scvelo as scv
import scanpy as sc
import pandas as pd
import numpy as np
import os
import loompy


# # scVelo

# %%


# Load rawcounts already processed
adata = sc.read("../data/data_RNAvelocity/processed_counts.txt",sep=' ')

# Since python like cells as rows -> transpose matrix
adata = adata.T

# Insert umap coordinates from SO
umap_cord = pd.read_csv("../data/data_RNAvelocity/coordinates_umap_scvelo.txt", sep=",") 
adata.obsm["X_umap"] = umap_cord.iloc[:,0:2].values

# Read metadata
metadata = pd.read_csv("../data/data_RNAvelocity/metadata_GEO.txt", sep= ",")


# %%


# Add metadata file (OBS)
metadata = pd.DataFrame(metadata)
adata.obs["batch_group"] = metadata["batch_group"].values
adata.obs["cluster"] = umap_cord.iloc[:,2].values

# Add features (VAR)
feat = pd.read_csv("../data/data_RNAvelocity/processed_counts.txt", sep= " ")
feat = feat.index
feat = pd.DataFrame(feat)
feat = pd.DataFrame({"feature" : feat.iloc[:,0]})
adata.var["features"] = feat.values


# %%


# Read LOOM file
ldata = scv.read("../data/data_RNAvelocity/s_un_am_allgenes.loom", cache=True)
# Merge adata with loom file
adata = scv.utils.merge(adata, ldata)


# %%


#we compute the first- and second-order moments (basically means and variances) for velocity estimation:
scv.pp.moments(adata)


# %%


# Estimates of velocity
#For steady state model
#scv.tl.velocity(adata, mode='steady_state')

#For dynamic model run 
scv.tl.recover_dynamics(adata)
scv.tl.velocity(adata, mode='dynamical')

#The velocities are stored in adata.layers just like the count matrices.
scv.tl.velocity_graph(adata)


# %%


# Computes confidence of velocities
scv.tl.velocity_confidence(adata)

scv.pl.scatter(adata, color='velocity_length', perc=[10,98], size= 100)
scv.pl.scatter(adata, color='velocity_confidence', perc=[2,98], size= 100)


# %%


# Extract highly variable genes
scv.pp.filter_genes_dispersion(adata)
HVG = adata.var[adata.var["velocity_genes"] == True].index


# %%


len(HVG)


# %%


scv.pl.velocity_embedding_stream(adata, basis='umap', color = "cluster",                                 
                                 size = 80.0, alpha = 0.8,
                                 palette= ['#A1DAB4','#FEE391','#41B6C4','#1D91C0'], legend_loc = "none")


# %%


get_ipython().run_line_magic('pinfo', 'scv.tl.terminal_states')


# %%


# Compute pseudotime
scv.tl.terminal_states(adata)
scv.tl.velocity_pseudotime(adata)

scv.pl.scatter(adata, color='velocity_pseudotime', color_map='bwr')


# %%


# graoh with root and end cells

scv.pl.scatter(adata, color=['root_cells', 'end_points'])


# %%


scv.logging.print_versions()


# # Plot expression of a gene

# %%


# Visualization
#scv.pl.velocity(adata, var_names=['Stmn1'])
#scv.pl.velocity_graph(adata)

