# Coalescent Simulation (CoSi) Analysis
The CoSi method is designed to evaluate the role of incomplete lineage sorting (ILS) in explaining conflicts between gene trees and species trees. This method has been successfully utilized in several recent studies, such as Wang et al. (2018), Yang et al. (2020), Morales-Briones et al. (2021), He et al. (2022), Liu et al. (2022), Jin et al. (2023), and Xu et al. (2023). Here, we adapted all scripts to accommodate the Single-Copy Nuclear genes (SCN genes) assembled from Deep Genome Skimming (DGS) data. 
Initially, we use a Multispecies coalescent (MSC) model to simulate multiple gene trees based on the species tree. Subsequently, we calculate the distribution of tree distances between these simulated gene trees and the species tree, as well as between the empirical gene trees and the species tree. If the simulated gene trees closely match the empirical gene trees, the height of the distribution bars will be similar, indicating a good fit for the MSC model. This similarity suggests that ILS adequately explains the discordance observed in the gene trees.
* Wang K, Lenstra JA, Liu L, Hu QJ, Ma T, Qiu Q, Liu JQ. 2018. Incomplete lineage sorting rather than hybridization explains the inconsistent phylogeny of the wisent. Communications Biology 1: 169.
* Yang YZ, Sun PC, Lv L, Wang DL, Ru DF, Li Y, Ma T, Zhang L, Shen XX, Meng FB, Jiao BB, Shan LX, Liu M, Wang QF, Qin ZJ, Xi ZX, Wang XY, Davis CC, Liu JQ. 2020. Prickly waterlily and rigid hornwort genomes shed light on early angiosperm evolution. Nature Plants 6: 215-222.
* Morales-Briones DF, Kadereit G, Tefarikis DT, Moore MJ, Smith SA, Brockington SF, Timoneda A, Yim WC, Cushman JC, Yang Y. 2021. Disentangling sources of gene tree discordance in phylogenomic data sets: testing ancient hybridizations in Amaranthaceae s.l. Systematic Biology 70: 219-235.
* He J, Lyu R, Luo YK, Xiao JM, Xie L, Wen J, Li WH, Pei LY, Cheng J. 2022. A phylotranscriptome study using silica gel-dried leaf tissues produces an updated robust phylogeny of Ranunculaceae. Molecular Phylogenetics and Evolution 174: 107545.
* Liu BB, Ren C, Kwak M, Hodel RGJ, Xu C, He J, Zhou WB, Huang CH, Ma H, Qian GZ, Hong DY, Wen J. 2022. Phylogenomic conflict analyses in the apple genus *Malus* s.l. reveal widespread hybridization and allopolyploidy driving diversification, with insights into the complex biogeographic history in the Northern Hemisphere. Journal of Integrative Plant Biology 64: 1020-1043.
* Jin ZT, Hodel RGJ, Ma DK, Wang H, Liu GN, Ren C, Ge BJ, Fan Q, Jin SH, Xu C, Wu J. Liu BB. 2023. Nightmare or delight: taxonomic circumscription meets reticulate evolution in the phylogenomic era. Molecular phylogenetics and evolution 189: 107914.
* Xu C, Jin ZT, Wang H, Xie SY, Lin XH, Hodel RGJ, Zhang Y, Ma DK, Liu B, Liu GN, Jin SH, Zhao L, Wu J, Ren C, Hong DY, Liu BB. 2023. Dense Sampling of Taxa and Genomes Untangles the Phylogenetic Backbone of a Non-model Plant Lineage Rife with Deep Hybridization and Allopolyploidy. https://dx.doi.org/10.1101/2023.10.21.563444


## Dependencies
python: ete3; dendropy; pandas; matplotlib; seaborn;  
R: phybase;  
ASTRAL-III
## Input and output
### Input
Gene trees, newick format, one line per gene tree;  
Species name list, text format, one line per species name.
### Ouput
output_subtree.trees: Subtrees generated in Step 1;  
astral.tre.regular.tre: Species tree constructed from subtrees in Step 2;  
astral.simulate.reroot.tree: Gene trees simulated by the species tree under MSC model in Step 3;  
result.tsv: Empirical and simulated gene-to-gene distance distributions;  
compare.png: Visualization of empirical and simulated gene-to-gene distance distribution results.
## Running the pipeline
### Step 1: Extracting subtrees
Two key considerations guide this step of our analysis. First, to ensure accurate comparisons of topological distances between gene trees and the species tree, the datasets must have consistent taxon sampling. Due to missing data in our empirical dataset, we extract subtrees to maintain uniform taxon sampling across all trees analyzed. Second, when our tree includes many species, the topological distance between the gene tree and the species tree can be highly variable. This variability requires generating a substantial number of gene trees to obtain statistically reliable results. To manage this, we select representative species from the major clades and extract subtrees for subsequent analysis.
The ‘extract_subtrees.py’ script will prune each gene tree according to the name list of the subsampled species and set the outgroup species.
```
python extract_subtrees.py -i <genes trees file> -n <species name list> -o <outgroup>
```
### Step 2: Inferring species tree using ASTRAL-III
In Step 1, we obtained the subtrees for each gene tree. In Step 2, we will use ASTRAL-III to infer the species tree, which will subsequently be converted into an "ultra-metric" tree.
```
python run.py
```
### Step 3: Simulating gene trees based on the MSC model
The "phybase" module will be employed to simulate gene trees based on the species tree using the MSC model. The “-n” parameter is used to specify the number of gene trees to be simulated, with a recommended minimum of 10,000.
```
python simulate.py -n <number of gene trees simulated> -o <outgroup>
```
### Step 4: Calculating and plotting the topological distance between the empirical and simulated gene trees
In Step 1, we extracted the subtrees. In Step 2, we inferred the species tree based on these subtrees. In Step 3, we simulated 10,000 gene trees. In Step 4, we calculated the distribution of tree distances between these simulated gene trees and the species tree, as well as between the empirical gene trees and the species tree. We then converted these calculated distances into distance distribution histograms for comparison. If the heights of the distribution bars are similar, this indicates a good fit for the MSC model.
```
python compare_trees_distance.py
```
