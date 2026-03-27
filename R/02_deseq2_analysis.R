getwd()
list.files()
library(DESeq2)
install.packages("BiocManager")
BiocManager::install("DESeq2")
install.packages("tidyverse")
library(DESeq2)
install.packages("tidyverse")
install.packages("pheatmap")
install.packages("RColorBrewer")
BiocManager::install("EnhancedVolcano")
BiocManager::install("clusterProfiler")
BiocManager::install("org.Hs.eg.db")
library(DESeq2)
library(tidyverse)
library(pheatmap)
library(EnhancedVolcano)
library(RColorBrewer)
library(clusterProfiler)
library(org.Hs.eg.db)
print("All libraries loaded successfully!")
packages_needed <- c("DESeq2", "tidyverse", "pheatmap",
                     "EnhancedVolcano", "RColorBrewer",
                     "clusterProfiler", "org.Hs.eg.db")

for (pkg in packages_needed) {
  status <- pkg %in% (.packages())
  cat(pkg, "→", ifelse(status, "✓ Loaded", "✗ Not loaded"), "\n")
}
packages_needed <- c("DESeq2", "tidyverse", "pheatmap",
                     "EnhancedVolcano", "RColorBrewer",
                     "clusterProfiler", "org.Hs.eg.db")
for (pkg in packages_needed) {
  status <- pkg %in% (.packages())
  cat(pkg, "→", ifelse(status, "✓ Loaded", "✗ Not loaded"), "\n")
}
counts <- read.csv("counts_filtered.csv",
                   row.names   = 1,
                   check.names = FALSE)
metadata <- read.csv("metadata.csv",
                     row.names = 1)
cat("✓ Files loaded!\n")
cat("Counts matrix:  ", nrow(counts), "genes x", ncol(counts), "samples\n")
cat("Metadata rows:  ", nrow(metadata), "samples\n")
counts[1:5, 1:4]
head(metadata)
table(metadata$group)
cat("Missing values in counts:", sum(is.na(counts)), "\n")
cat("Missing values in metadata:", sum(is.na(metadata)), "\n")

samples_match <- all(colnames(counts) == rownames(metadata))
length(colnames(counts)
       length(rownames(metadata))       
       length(colnames(counts))
       length(rownames(metadata))       
setdiff(colnames(counts), rownames(metadata))       
setdiff(rownames(metadata), colnames(counts))
samples_match <- all(colnames(counts) == rownames(metadata))
if (samples_match) {
  cat("✓ Sample names match perfectly - safe to continue!\n")
} else {
  cat("✗ Sample names do NOT match - fixing now...\n")
metadata <- metadata[colnames(counts), , drop = FALSE]  
if (all(colnames(counts) == rownames(metadata))) {
  cat("✓ Fixed! Sample names now match.\n")
}
}
metadata <- metadata[colnames(counts), ]
all(colnames(counts) == rownames(metadata))
metadata <- metadata[colnames(counts), ]
stopifnot(all(colnames(counts) == rownames(metadata)))
colnames(counts) <- tolower(colnames(counts))
rownames(metadata) <- tolower(rownames(metadata))
if (all(colnames(counts) == rownames(metadata))) {
  cat("✓ Fixed! Sample names now match.\n")
}}
samples_match <- all(colnames(counts) == rownames(metadata))
if (samples_match) {
  cat("✓ Sample names match perfectly - safe to continue!\n")
} else {
  cat("✗ Sample names do NOT match - fixing now...\n")
  metadata <- metadata[colnames(counts), , drop = FALSE]  
  class(metadata)
  dim(metadata)  
  str(metadata)  
  print(metadata)  
raw_check <- read.csv("metadata.csv", header = TRUE)  
cat("Dimensions:", dim(raw_check), "\n")
cat("Columns:   ", colnames(raw_check), "\n")
head(raw_check)
metadata <- read.csv("metadata.csv",
                     header           = TRUE,
                     row.names        = 1,
                     stringsAsFactors = FALSE)
metadata <- as.data.frame(metadata)
colnames(metadata) <- "group"
cat("Class:      ", class(metadata), "\n")
cat("Dimensions: ", dim(metadata), "\n")
cat("Column name:", colnames(metadata), "\n")
cat("First few rows:\n")
head(metadata)
samples_match <- all(colnames(counts) == rownames(metadata))
if (samples_match) {
  cat("✓ Sample names match perfectly - safe to continue!\n")
} else {
  cat("✗ Sample names do NOT match - fixing now...\n")
  metadata <- metadata[colnames(counts), , drop = FALSE]
  
  if (all(colnames(counts) == rownames(metadata))) {
    cat("✓ Fixed! Sample names now match.\n")
  }
}
cat("First 6 counts columns:\n")
print(head(colnames(counts)))
cat("\nFirst 6 metadata rows:\n")
print(head(rownames(metadata)))
cat("\nLast 6 counts columns:\n")
print(tail(colnames(counts)))
cat("\nLast 6 metadata rows:\n")
print(tail(rownames(metadata)))
matching <- sum(colnames(counts) == rownames(metadata))
cat("\nMatching sample names:", matching, "out of", ncol(counts), "\n")
raw <- read.csv("metadata.csv", header = TRUE)
cat("Dimensions:", dim(raw), "\n")
cat("Column names:", colnames(raw), "\n")
head(raw)
all_samples     <- colnames(counts)
ipf_samples     <- all_samples[startsWith(all_samples, "ipf_")]
control_samples <- all_samples[startsWith(all_samples, "control_")]
selected        <- c(ipf_samples, control_samples)
cat("IPF samples:     ", length(ipf_samples), "\n")
cat("Control samples: ", length(control_samples), "\n")
cat("Total selected:  ", length(selected), "\n")
counts_de <- counts[, selected]
cat("Counts matrix:   ", nrow(counts_de), "genes x",
    ncol(counts_de), "samples\n")
metadata <- data.frame(
  group     = ifelse(startsWith(selected, "ipf_"),
                     "IPF",
                     "Control"),
  row.names = selected,
  stringsAsFactors = FALSE
)
metadata$group <- factor(metadata$group,
                         levels = c("Control", "IPF"))
cat("Metadata dimensions:", dim(metadata), "\n")
cat("\nSamples per group:\n")
print(table(metadata$group))
cat("\nFirst 6 rows:\n")
head(metadata)
cat("\nLast 6 rows:\n")
tail(metadata)
if (all(colnames(counts_de) == rownames(metadata))) {
  cat("✓ Sample names match perfectly - ready for DESeq2!\n")
} else {
  cat("✗ Still mismatching\n")
  mismatches <- which(colnames(counts_de) != rownames(metadata))
  cat("Mismatches at positions:", mismatches, "\n")
}  
dds <- DESeqDataSetFromMatrix(
  countData = round(counts_de),
  colData   = metadata,
  design    = ~ group
)
cat("✓ DESeq2 object created!\n")
cat("Genes:  ", nrow(dds), "\n")
cat("Samples:", ncol(dds), "\n")
keep <- rowSums(counts(dds) >= 10) >= 20
dds  <- dds[keep, ]
cat("Genes after filtering:", nrow(dds), "\n")
cat("Running DESeq2 - please wait 3-5 minutes...\n")
dds <- DESeq(dds)
cat("✓ DESeq2 complete!\n")
size_factors <- sizeFactors(dds)
cat("Size factor summary:\n")
print(summary(size_factors))
extreme <- size_factors[size_factors < 0.5 | size_factors > 2.0]
if (length(extreme) == 0) {
  cat("✓ All size factors look healthy!\n")
} else {
  cat("⚠ Warning:", length(extreme), "samples with extreme size factors\n")
  print(extreme)
}
res <- results(dds,
               contrast = c("group", "IPF", "Control"),
               alpha    = 0.05)
cat("=== DESeq2 Results Summary ===\n")
summary(res)
res_df <- as.data.frame(res) %>%
  rownames_to_column("gene") %>%
  arrange(padj) %>%
  filter(!is.na(padj))
cat("Total genes tested:", nrow(res_df), "\n")
cat("\nTop 10 most significant genes:\n")
head(res_df, 10)
sig_genes  <- res_df %>%
  filter(padj < 0.05,
         abs(log2FoldChange) > 1)
up_genes   <- sig_genes %>% filter(log2FoldChange > 1)
down_genes <- sig_genes %>% filter(log2FoldChange < -1)
cat("─────────────────────────────────────\n")
cat("Total significant DEGs:", nrow(sig_genes), "\n")
cat("Upregulated in IPF:    ", nrow(up_genes),  "\n")
cat("Downregulated in IPF:  ", nrow(down_genes),"\n")
cat("─────────────────────────────────────\n")
cat("\nTop 10 upregulated genes in IPF:\n")
up_genes %>%
  arrange(desc(log2FoldChange)) %>%
  select(gene, log2FoldChange, padj) %>%
  head(10)
up_genes %>%
  arrange(desc(log2FoldChange)) %>%
  select(gene, log2FoldChange, padj) %>%
  head(10)
cat("\nTop 10 upregulated genes in IPF:\n")
up_genes %>%
  arrange(desc(log2FoldChange)) %>%
  dplyr::select(gene, log2FoldChange, padj) %>%
  head(10)
cat("\nTop 10 downregulated genes in IPF:\n")
down_genes %>%
  arrange(log2FoldChange) %>%
  dplyr::select(gene, log2FoldChange, padj) %>%
  head(10)
write.csv(res_df,
          "DESeq2_all_results.csv",
          row.names = FALSE)
write.csv(sig_genes,
          "DESeq2_significant_genes.csv",
          row.names = FALSE)
write.csv(up_genes,
          "DESeq2_upregulated.csv",
          row.names = FALSE)
write.csv(down_genes,
          "DESeq2_downregulated.csv",
          row.names = FALSE)
cat("✓ All result files saved!\n")
EnhancedVolcano(res_df,
                lab             = res_df$gene,
                x               = "log2FoldChange",
                y               = "padj",
                pCutoff         = 0.05,
                FCcutoff        = 1.0,
                pointSize       = 1.8,
                labSize         = 3.5,
                title           = "IPF vs Control",
                subtitle        = "DESeq2  |  padj < 0.05  |  |log2FC| > 1",
                caption         = paste("Total genes:", nrow(res_df)),
                col             = c("grey70", "grey70", "#5B8DB8", "#D94F3D"),
                colAlpha        = 0.6,
                legendPosition  = "right",
                drawConnectors  = TRUE,
                max.overlaps    = 25
)
vsd <- vst(dds, blind = FALSE)
top50 <- sig_genes %>%
  slice_min(padj, n = 50) %>%
  pull(gene)
heatmap_mat <- assay(vsd)[top50, ]
annotation_col <- data.frame(
  Group     = metadata$group,
  row.names = rownames(metadata)
)
ann_colors <- list(
  Group = c(Control = "#5B8DB8", IPF = "#D94F3D")
)
pheatmap(heatmap_mat,
         annotation_col    = annotation_col,
         annotation_colors = ann_colors,
         scale             = "row",
         show_colnames     = FALSE,
         fontsize_row      = 7,
         color             = colorRampPalette(
           rev(brewer.pal(9, "RdBu")))(100),
         main              = "Top 50 DE Genes: IPF vs Control",
         border_color      = NA,
         cutree_cols       = 2
)
vsd <- vst(dds, blind = FALSE)

pca_plot <- plotPCA(vsd, intgroup = "group") +
  scale_color_manual(
    values = c(Control = "#2471A3",
               IPF     = "#C0392B"),
    labels = c(paste0("Control (n = ", sum(metadata$group == "Control"), ")"),
               paste0("IPF     (n = ", sum(metadata$group == "IPF"), ")"))
  ) +
  labs(
    title    = "PCA: Global Gene Expression Patterns",
    subtitle = "IPF vs Control  |  Variance Stabilized Counts",
    x        = "PC1 — explains most variation between samples",
    y        = "PC2 — explains second most variation",
    color    = "Sample Group",
    caption  = "Each dot represents one sample"
  ) +
  geom_point(size = 3, alpha = 0.8) +
  theme_bw(base_size = 13) +
  theme(
    plot.title       = element_text(face = "bold", size = 15,
                                    hjust = 0),
    plot.subtitle    = element_text(size = 11, color = "grey40",
                                    hjust = 0),
    plot.caption     = element_text(size = 9, color = "grey50",
                                    hjust = 1),
    legend.position  = "right",
    legend.title     = element_text(face = "bold", size = 11),
    legend.text      = element_text(size = 10),
    axis.title       = element_text(size = 11, face = "bold"),
    axis.text        = element_text(size = 10, color = "grey20"),
    panel.grid.major = element_line(color = "grey92", linewidth = 0.4),
    panel.grid.minor = element_blank(),
    panel.border     = element_rect(color = "grey70", linewidth = 0.8),
    plot.background  = element_rect(fill = "white", color = NA),
    plot.margin      = margin(20, 20, 20, 20)
  )
print(pca_plot)
ggsave("pca_plot_final.png",
       plot   = pca_plot,
       width  = 10,
       height = 8,
       dpi    = 300,
       bg     = "white")
cat("✓ PCA plot saved!\n")
cat("Converting gene symbols to Entrez IDs...\n")
up_entrez <- bitr(up_genes$gene,
                  fromType = "SYMBOL",
                  toType   = "ENTREZID",
                  OrgDb    = org.Hs.eg.db)
down_entrez <- bitr(down_genes$gene,
                    fromType = "SYMBOL",
                    toType   = "ENTREZID",
                    OrgDb    = org.Hs.eg.db)
cat("Genes available for enrichment:\n")
cat("Upregulated:  ", nrow(up_entrez),   "genes\n")
cat("Downregulated:", nrow(down_entrez), "genes\n")
head(up_entrez)
cat("Running GO enrichment on upregulated genes...\n")
go_up <- enrichGO(
  gene          = up_entrez$ENTREZID,
  OrgDb         = org.Hs.eg.db,
  ont           = "BP",
  pAdjustMethod = "BH",
  pvalueCutoff  = 0.05,
  qvalueCutoff  = 0.05,
  readable      = TRUE
)
cat("✓ Done!\n")
cat("Enriched pathways found:", nrow(go_up@result), "\n")
go_up@result %>%
  dplyr::select(Description, Count, GeneRatio, p.adjust) %>%
  head(10)
fibrosis_pathways <- go_up@result %>%
  dplyr::filter(
    grepl("fibros|collagen|matrix|fibroblast|wound|scar",
          Description,
          ignore.case = TRUE)
  ) %>%
  dplyr::select(Description, Count, GeneRatio, p.adjust) %>%
  head(20)
cat("=== FIBROSIS RELATED PATHWAYS ===\n")
print(fibrosis_pathways)
immune_pathways <- go_up@result %>%
  dplyr::filter(
    grepl("immune|inflamm|cytokine|lymphocyte|macrophage",
          Description,
          ignore.case = TRUE)
  ) %>%
  dplyr::select(Description, Count, GeneRatio, p.adjust) %>%
  head(20)
cat("\n=== IMMUNE RELATED PATHWAYS ===\n")
print(immune_pathways)
epithelial_pathways <- go_up@result %>%
  dplyr::filter(
    grepl("epithelial|keratiniz|differentiat",
          Description,
          ignore.case = TRUE)
  ) %>%
  dplyr::select(Description, Count, GeneRatio, p.adjust) %>%
  head(20)
cat("\n=== EPITHELIAL RELATED PATHWAYS ===\n")
print(epithelial_pathways)
cat("Running GO enrichment on downregulated genes...\n")
go_down <- enrichGO(
  gene          = down_entrez$ENTREZID,
  OrgDb         = org.Hs.eg.db,
  ont           = "BP",
  pAdjustMethod = "BH",
  pvalueCutoff  = 0.05,
  qvalueCutoff  = 0.05,
  readable      = TRUE
)
cat("✓ Done!\n")
cat("Enriched pathways found:", nrow(go_down@result), "\n")
go_down@result %>%
  dplyr::select(Description, Count, GeneRatio, p.adjust) %>%
  head(10)
up_plot <- dotplot(go_up,
                   showCategory = 20,
                   title        = "GO Biological Processes — Upregulated in IPF",
                   color        = "p.adjust",
                   font.size    = 10) +
  scale_color_gradient(low  = "#C0392B",
                       high = "#F1948A") +
  theme_bw() +
  theme(
    plot.title  = element_text(face = "bold", size = 13),
    axis.text.y = element_text(size = 9)
  )
print(up_plot)
down_plot <- dotplot(go_down,
                     showCategory = 20,
                     title        = "GO Biological Processes — Downregulated in IPF",
                     color        = "p.adjust",
                     font.size    = 10) +
  scale_color_gradient(low  = "#2471A3",
                       high = "#7FB3D3") +
  theme_bw() +
  theme(
    plot.title  = element_text(face = "bold", size = 13),
    axis.text.y = element_text(size = 9)
  )
print(down_plot)
ggsave("GO_upregulated_dotplot.png",
       plot   = up_plot,
       width  = 12,
       height = 9,
       dpi    = 300,
       bg     = "white")
ggsave("GO_downregulated_dotplot.png",
       plot   = down_plot,
       width  = 12,
       height = 9,
       dpi    = 300,
       bg     = "white")
write.csv(go_up@result,
          "GO_upregulated_pathways.csv",
          row.names = FALSE)
write.csv(go_down@result,
          "GO_downregulated_pathways.csv",
          row.names = FALSE)
cat("✓ All pathway outputs saved!\n")
cat("  GO_upregulated_dotplot.png\n")
cat("  GO_downregulated_dotplot.png\n")
cat("  GO_upregulated_pathways.csv\n")
cat("  GO_downregulated_pathways.csv\n")
