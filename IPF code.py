Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# These are your tools - run this cell first every time you open the notebook
import pandas as pd        # for data tables
import numpy as np         # for math/arrays
import matplotlib.pyplot as plt   # for plots
import seaborn as sns      # for nicer plots

print("All libraries loaded successfully!")
SyntaxError: multiple statements found while compiling a single statement
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("All libraries loaded successfully!")
All libraries loaded successfully!
df = pd.read_csv('GSE150910_gene-level_count_file_csv.gz', index_col=0)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    df = pd.read_csv('GSE150910_gene-level_count_file_csv.gz', index_col=0)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Python314\Lib\site-packages\pandas\io\common.py", line 809, in get_handle
    handle = gzip.GzipFile(  # type: ignore[assignment]
  File "C:\Python314\Lib\gzip.py", line 208, in __init__
    fileobj = self.myfileobj = builtins.open(filename, mode or 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'GSE150910_gene-level_count_file_csv.gz'
df = pd.read_csv(r"C:\Users\Acer\my_IPF_project\GSE150910_gene-level_count_file_csv.gz", index_col=0)
  
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    df = pd.read_csv(r"C:\Users\Acer\my_IPF_project\GSE150910_gene-level_count_file_csv.gz", index_col=0)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Python314\Lib\site-packages\pandas\io\common.py", line 809, in get_handle
    handle = gzip.GzipFile(  # type: ignore[assignment]
  File "C:\Python314\Lib\gzip.py", line 208, in __init__
    fileobj = self.myfileobj = builtins.open(filename, mode or 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Acer\\my_IPF_project\\GSE150910_gene-level_count_file_csv.gz'
df = pd.read_csv('GSE150910_gene-level_count_file_csv.gz', index_col=0)
  
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    df = pd.read_csv('GSE150910_gene-level_count_file_csv.gz', index_col=0)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Python314\Lib\site-packages\pandas\io\common.py", line 809, in get_handle
    handle = gzip.GzipFile(  # type: ignore[assignment]
  File "C:\Python314\Lib\gzip.py", line 208, in __init__
    fileobj = self.myfileobj = builtins.open(filename, mode or 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'GSE150910_gene-level_count_file_csv.gz'
import os
print(os.getcwd())
C:\Python314
df = pd.read_csv('GSE150910_gene-level_count_file_csv.gz', index_col=0)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    df = pd.read_csv('GSE150910_gene-level_count_file_csv.gz', index_col=0)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Python314\Lib\site-packages\pandas\io\common.py", line 809, in get_handle
    handle = gzip.GzipFile(  # type: ignore[assignment]
  File "C:\Python314\Lib\gzip.py", line 208, in __init__
    fileobj = self.myfileobj = builtins.open(filename, mode or 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'GSE150910_gene-level_count_file_csv.gz'
df = pd.read_csv('GSE150910_gene-level_count_file_csv', index_col=0)
  
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    df = pd.read_csv('GSE150910_gene-level_count_file_csv', index_col=0)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Python314\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'GSE150910_gene-level_count_file_csv'
df = pd.read_csv('GSE150910_gene-level_count_file_csv.gz', index_col=0)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    df = pd.read_csv('GSE150910_gene-level_count_file_csv.gz', index_col=0)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Python314\Lib\site-packages\pandas\io\common.py", line 809, in get_handle
    handle = gzip.GzipFile(  # type: ignore[assignment]
  File "C:\Python314\Lib\gzip.py", line 208, in __init__
    fileobj = self.myfileobj = builtins.open(filename, mode or 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'GSE150910_gene-level_count_file_csv.gz'
df = pd.read_csv(r"C:\Python314\GSE150910_gene-level_count_file_csv.gz", index_col=0)
  
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    df = pd.read_csv(r"C:\Python314\GSE150910_gene-level_count_file_csv.gz", index_col=0)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Python314\Lib\site-packages\pandas\io\common.py", line 809, in get_handle
    handle = gzip.GzipFile(  # type: ignore[assignment]
  File "C:\Python314\Lib\gzip.py", line 208, in __init__
    fileobj = self.myfileobj = builtins.open(filename, mode or 'rb')
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Python314\\GSE150910_gene-level_count_file_csv.gz'
import os
print(os.listdir())
['DLLs', 'Doc', 'etc', 'GSE150910_gene-level_count_file.csv.gz', 'include', 'IPF_project', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python.pdb', 'python3.14t.exe', 'python3.14t.pdb', 'python3.14t_d.exe', 'python3.14t_d.pdb', 'python3.dll', 'python314.dll', 'python314.pdb', 'python314t.dll', 'python314t.pdb', 'python314t_d.dll', 'python314t_d.pdb', 'python314_d.dll', 'python314_d.pdb', 'python3t.dll', 'python3t_d.dll', 'python3_d.dll', 'pythonw.exe', 'pythonw.pdb', 'pythonw3.14t.exe', 'pythonw3.14t.pdb', 'pythonw3.14t_d.exe', 'pythonw3.14t_d.pdb', 'pythonw_d.exe', 'pythonw_d.pdb', 'python_d.exe', 'python_d.pdb', 'Scripts', 'share', 'tcl', 'vcruntime140.dll', 'vcruntime140_1.dll']
df = pd.read_csv('GSE150910_gene-level_count_file.csv.gz', index_col=0)
print("Dataset loaded!")
Dataset loaded!
print(f"Genes (rows): {df.shape[0]}")
Genes (rows): 18838
print(f"Samples (columns): {df.shape[1]}")
Samples (columns): 288
df.iloc[:5, :6]
          chp_26  chp_31  chp_34  chp_38  chp_1  chp_3
symbol                                                
TSPAN6      1361     993     351     613    841    565
TNMD           5      13       0       0      0      6
DPM1        1929    2775    1894    2007   1436   1923
SCYL3        176     216     208     218    162    137
C1orf112      93     143      97     148     98    128
cols = list(df.columns)
ipf_samples     = [c for c in cols if c.startswith('ipf_')]
control_samples = [c for c in cols if c.startswith('control_')]
chp_samples     = [c for c in cols if c.startswith('chp_')]
print(f"IPF samples:     {len(ipf_samples)}")
IPF samples:     103
print(f"Control samples: {len(control_samples)}")
Control samples: 103
print(f"Healthy (CHP):   {len(chp_samples)}")
Healthy (CHP):   82
meta = pd.DataFrame({
    'sample': df.columns,
    'group': ['IPF'     if s.startswith('ipf_')     else
              'Healthy' if s.startswith('chp_')     else
              'Control'
              for s in df.columns]
}).set_index('sample')
  
meta['group'].value_counts()
  
group
IPF        103
Control    103
Healthy     82
Name: count, dtype: int64
lib_sizes = df.sum(axis=0)  # sum all gene counts per sample

plt.figure(figsize=(10, 4))
colors = meta['group'].map({'IPF': '#D94F3D', 'Healthy': '#4CAF7D', 'Control': '#5B8DB8'})
plt.bar(range(len(lib_sizes)), lib_sizes.values / 1e6, color=colors.values, alpha=0.7)
plt.xlabel('Sample Index')
plt.ylabel('Library Size (millions)')
plt.title('Library Size per Sample')
plt.tight_layout()
plt.show()
SyntaxError: multiple statements found while compiling a single statement
lib_sizes = df.sum(axis=0)
plt.figure(figsize=(10, 4))
<Figure size 1000x400 with 0 Axes>
colors = meta['group'].map({'IPF': '#D94F3D', 'Healthy': '#4CAF7D', 'Control': '#5B8DB8'})
plt.bar(range(len(lib_sizes)), lib_sizes.values / 1e6, color=colors.values, alpha=0.7)
<BarContainer object of 288 artists>
plt.xlabel('Sample Index')
Text(0.5, 0, 'Sample Index')
plt.ylabel('Library Size (millions)')
Text(0, 0.5, 'Library Size (millions)')
plt.title('Library Size per Sample')
Text(0.5, 1.0, 'Library Size per Sample')
plt.tight_layout()
plt.show()
print(lib_sizes.describe() / 1e6)
count     0.000288
mean     31.501262
std       5.980366
min       4.906588
25%      28.034598
50%      31.858365
75%      35.190852
max      51.762810
dtype: float64
counts = df.values.astype(float)
lib_sz = counts.sum(axis=0)
cpm    = counts / lib_sz[np.newaxis, :] * 1e6
log2cpm = np.log2(cpm + 1)
log2cpm_df = pd.DataFrame(log2cpm, index=df.index, columns=df.columns)
print("Normalization done!")
Normalization done!
print(log2cpm_df.iloc[:5, :4])
            chp_26    chp_31    chp_34    chp_38
symbol                                          
TSPAN6    5.789058  5.087610  3.825613  4.351884
TNMD      0.262391  0.518102  0.000000  0.000000
DPM1      6.284541  6.542726  6.172133  6.013038
SCYL3     3.003810  3.031925  3.139038  2.982977
C1orf112  2.235740  2.524256  2.214705  2.508070
min_samples = int(0.10 * df.shape[1])
keep_mask   = (cpm > 1).sum(axis=1) >= min_samples
df_filtered      = df.loc[keep_mask]
log2cpm_filtered = log2cpm_df.loc[keep_mask]
print(f"Genes before filtering: {df.shape[0]}")
Genes before filtering: 18838
print(f"Genes after filtering:  {df_filtered.shape[0]}")
Genes after filtering:  15058
print(f"Genes removed:          {df.shape[0] - df_filtered.shape[0]}")
Genes removed:          3780
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
groups = [('Healthy (CHP)', chp_samples, '#4CAF7D'),
          ('Control',       control_samples, '#5B8DB8'),
          ('IPF',           ipf_samples, '#D94F3D')]

for ax, (title, samples, color) in zip(axes, groups):
    mean_expr = log2cpm_filtered[samples].mean(axis=1)
    ax.hist(mean_expr[mean_expr > 0], bins=60, color=color, alpha=0.75, edgecolor='none')
    ax.set_title(title, fontsize=13, fontweight='bold')
    ax.set_xlabel('Mean log2(CPM + 1)')
    ax.set_ylabel('Number of Genes')
    
SyntaxError: multiple statements found while compiling a single statement
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
groups = [('Healthy (CHP)', chp_samples, '#4CAF7D'),
          ('Control',       control_samples, '#5B8DB8'),
          ('IPF',           ipf_samples, '#D94F3D')]
SyntaxError: multiple statements found while compiling a single statement
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
groups = [('Healthy (CHP)', chp_samples, '#4CAF7D'),
          ('Control',       control_samples, '#5B8DB8'),
          ('IPF',           ipf_samples, '#D94F3D')]
for ax, (title, samples, color) in zip(axes, groups):
    mean_expr = log2cpm_filtered[samples].mean(axis=1)
    ax.hist(mean_expr[mean_expr > 0], bins=60, color=color, alpha=0.75, edgecolor='none')
    ax.set_title(title, fontsize=13, fontweight='bold')
    ax.set_xlabel('Mean log2(CPM + 1)')
    ax.set_ylabel('Number of Genes')
    plt.suptitle('Gene Expression Distributions After Normalization', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

    
(array([ 83., 614., 756., 660., 635., 600., 588., 536., 585., 637., 621.,
       618., 639., 638., 656., 640., 603., 635., 535., 556., 492., 454.,
       392., 348., 278., 229., 173., 166., 130.,  87., 103.,  66.,  46.,
        43.,  32.,  20.,  17.,  24.,  11.,  13.,  16.,  10.,  15.,   9.,
         8.,  10.,   3.,   3.,   3.,   2.,   3.,   2.,   1.,   4.,   0.,
         3.,   4.,   0.,   1.,   2.]), array([ 0.05310451,  0.30340966,  0.55371482,  0.80401998,  1.05432514,
        1.3046303 ,  1.55493546,  1.80524062,  2.05554578,  2.30585093,
        2.55615609,  2.80646125,  3.05676641,  3.30707157,  3.55737673,
        3.80768189,  4.05798704,  4.3082922 ,  4.55859736,  4.80890252,
        5.05920768,  5.30951284,  5.559818  ,  5.81012316,  6.06042831,
        6.31073347,  6.56103863,  6.81134379,  7.06164895,  7.31195411,
        7.56225927,  7.81256442,  8.06286958,  8.31317474,  8.5634799 ,
        8.81378506,  9.06409022,  9.31439538,  9.56470054,  9.81500569,
       10.06531085, 10.31561601, 10.56592117, 10.81622633, 11.06653149,
       11.31683665, 11.5671418 , 11.81744696, 12.06775212, 12.31805728,
       12.56836244, 12.8186676 , 13.06897276, 13.31927792, 13.56958307,
       13.81988823, 14.07019339, 14.32049855, 14.57080371, 14.82110887,
       15.07141403]), <BarContainer object of 60 artists>)
Text(0.5, 1.0, 'Healthy (CHP)')
Text(0.5, 0, 'Mean log2(CPM + 1)')
Text(0, 0.5, 'Number of Genes')
Text(0.5, 0.98, 'Gene Expression Distributions After Normalization')
(array([ 90., 345., 601., 595., 528., 547., 520., 518., 487., 528., 533.,
       573., 550., 633., 628., 570., 626., 636., 638., 629., 597., 506.,
       512., 448., 395., 337., 289., 228., 183., 143., 102., 116.,  81.,
        76.,  44.,  31.,  22.,  19.,  23.,  18.,  14.,  16.,  13.,  16.,
         7.,   6.,  12.,   2.,   4.,   0.,   2.,   2.,   6.,   3.,   3.,
         2.,   1.,   3.,   0.,   1.]), array([ 0.0818453 ,  0.32585635,  0.56986741,  0.81387847,  1.05788953,
        1.30190058,  1.54591164,  1.7899227 ,  2.03393375,  2.27794481,
        2.52195587,  2.76596692,  3.00997798,  3.25398904,  3.4980001 ,
        3.74201115,  3.98602221,  4.23003327,  4.47404432,  4.71805538,
        4.96206644,  5.20607749,  5.45008855,  5.69409961,  5.93811067,
        6.18212172,  6.42613278,  6.67014384,  6.91415489,  7.15816595,
        7.40217701,  7.64618807,  7.89019912,  8.13421018,  8.37822124,
        8.62223229,  8.86624335,  9.11025441,  9.35426546,  9.59827652,
        9.84228758, 10.08629864, 10.33030969, 10.57432075, 10.81833181,
       11.06234286, 11.30635392, 11.55036498, 11.79437603, 12.03838709,
       12.28239815, 12.52640921, 12.77042026, 13.01443132, 13.25844238,
       13.50245343, 13.74646449, 13.99047555, 14.2344866 , 14.47849766,
       14.72250872]), <BarContainer object of 60 artists>)
Text(0.5, 1.0, 'Control')
Text(0.5, 44.49999999999998, 'Mean log2(CPM + 1)')
Text(690.8006975308641, 0.5, 'Number of Genes')
Text(0.5, 0.98, 'Gene Expression Distributions After Normalization')
(array([ 87., 361., 583., 573., 526., 476., 517., 513., 474., 485., 610.,
       579., 599., 636., 639., 636., 624., 668., 624., 614., 600., 515.,
       475., 441., 414., 337., 280., 239., 143., 123., 124., 114.,  85.,
        58.,  48.,  30.,  28.,  18.,  16.,  27.,  14.,  15.,  12.,  15.,
         6.,  11.,  10.,   7.,   3.,   4.,   2.,   2.,   5.,   2.,   1.,
         3.,   3.,   1.,   1.,   2.]), array([ 0.20051054,  0.43974315,  0.67897575,  0.91820835,  1.15744096,
        1.39667356,  1.63590616,  1.87513877,  2.11437137,  2.35360397,
        2.59283657,  2.83206918,  3.07130178,  3.31053438,  3.54976699,
        3.78899959,  4.02823219,  4.26746479,  4.5066974 ,  4.74593   ,
        4.9851626 ,  5.22439521,  5.46362781,  5.70286041,  5.94209301,
        6.18132562,  6.42055822,  6.65979082,  6.89902343,  7.13825603,
        7.37748863,  7.61672123,  7.85595384,  8.09518644,  8.33441904,
        8.57365165,  8.81288425,  9.05211685,  9.29134945,  9.53058206,
        9.76981466, 10.00904726, 10.24827987, 10.48751247, 10.72674507,
       10.96597768, 11.20521028, 11.44444288, 11.68367548, 11.92290809,
       12.16214069, 12.40137329, 12.6406059 , 12.8798385 , 13.1190711 ,
       13.3583037 , 13.59753631, 13.83676891, 14.07600151, 14.31523412,
       14.55446672]), <BarContainer object of 60 artists>)
Text(0.5, 1.0, 'IPF')
Text(0.5, 44.49999999999998, 'Mean log2(CPM + 1)')
Text(1306.6024320987653, 0.5, 'Number of Genes')
Text(0.5, 0.98, 'Gene Expression Distributions After Normalization')
for ax, (title, samples, color) in zip(axes, groups):
    mean_expr = log2cpm_filtered[samples].mean(axis=1)
    ax.hist(mean_expr[mean_expr > 0], bins=60, color=color, alpha=0.75, edgecolor='none')
    ax.set_title(title, fontsize=13, fontweight='bold')
    ax.set_xlabel('Mean log2(CPM + 1)')
    ax.set_ylabel('Number of Genes')

    
(array([ 83., 614., 756., 660., 635., 600., 588., 536., 585., 637., 621.,
       618., 639., 638., 656., 640., 603., 635., 535., 556., 492., 454.,
       392., 348., 278., 229., 173., 166., 130.,  87., 103.,  66.,  46.,
        43.,  32.,  20.,  17.,  24.,  11.,  13.,  16.,  10.,  15.,   9.,
         8.,  10.,   3.,   3.,   3.,   2.,   3.,   2.,   1.,   4.,   0.,
         3.,   4.,   0.,   1.,   2.]), array([ 0.05310451,  0.30340966,  0.55371482,  0.80401998,  1.05432514,
        1.3046303 ,  1.55493546,  1.80524062,  2.05554578,  2.30585093,
        2.55615609,  2.80646125,  3.05676641,  3.30707157,  3.55737673,
        3.80768189,  4.05798704,  4.3082922 ,  4.55859736,  4.80890252,
        5.05920768,  5.30951284,  5.559818  ,  5.81012316,  6.06042831,
        6.31073347,  6.56103863,  6.81134379,  7.06164895,  7.31195411,
        7.56225927,  7.81256442,  8.06286958,  8.31317474,  8.5634799 ,
        8.81378506,  9.06409022,  9.31439538,  9.56470054,  9.81500569,
       10.06531085, 10.31561601, 10.56592117, 10.81622633, 11.06653149,
       11.31683665, 11.5671418 , 11.81744696, 12.06775212, 12.31805728,
       12.56836244, 12.8186676 , 13.06897276, 13.31927792, 13.56958307,
       13.81988823, 14.07019339, 14.32049855, 14.57080371, 14.82110887,
       15.07141403]), <BarContainer object of 60 artists>)
Text(0.5, 1.0, 'Healthy (CHP)')
Text(0.5, 44.49999999999998, 'Mean log2(CPM + 1)')
Text(27.832296296296285, 0.5, 'Number of Genes')
(array([ 90., 345., 601., 595., 528., 547., 520., 518., 487., 528., 533.,
       573., 550., 633., 628., 570., 626., 636., 638., 629., 597., 506.,
       512., 448., 395., 337., 289., 228., 183., 143., 102., 116.,  81.,
        76.,  44.,  31.,  22.,  19.,  23.,  18.,  14.,  16.,  13.,  16.,
         7.,   6.,  12.,   2.,   4.,   0.,   2.,   2.,   6.,   3.,   3.,
         2.,   1.,   3.,   0.,   1.]), array([ 0.0818453 ,  0.32585635,  0.56986741,  0.81387847,  1.05788953,
        1.30190058,  1.54591164,  1.7899227 ,  2.03393375,  2.27794481,
        2.52195587,  2.76596692,  3.00997798,  3.25398904,  3.4980001 ,
        3.74201115,  3.98602221,  4.23003327,  4.47404432,  4.71805538,
        4.96206644,  5.20607749,  5.45008855,  5.69409961,  5.93811067,
        6.18212172,  6.42613278,  6.67014384,  6.91415489,  7.15816595,
        7.40217701,  7.64618807,  7.89019912,  8.13421018,  8.37822124,
        8.62223229,  8.86624335,  9.11025441,  9.35426546,  9.59827652,
        9.84228758, 10.08629864, 10.33030969, 10.57432075, 10.81833181,
       11.06234286, 11.30635392, 11.55036498, 11.79437603, 12.03838709,
       12.28239815, 12.52640921, 12.77042026, 13.01443132, 13.25844238,
       13.50245343, 13.74646449, 13.99047555, 14.2344866 , 14.47849766,
       14.72250872]), <BarContainer object of 60 artists>)
Text(0.5, 1.0, 'Control')
Text(0.5, 44.49999999999998, 'Mean log2(CPM + 1)')
Text(690.8006975308641, 0.5, 'Number of Genes')
(array([ 87., 361., 583., 573., 526., 476., 517., 513., 474., 485., 610.,
       579., 599., 636., 639., 636., 624., 668., 624., 614., 600., 515.,
       475., 441., 414., 337., 280., 239., 143., 123., 124., 114.,  85.,
        58.,  48.,  30.,  28.,  18.,  16.,  27.,  14.,  15.,  12.,  15.,
         6.,  11.,  10.,   7.,   3.,   4.,   2.,   2.,   5.,   2.,   1.,
         3.,   3.,   1.,   1.,   2.]), array([ 0.20051054,  0.43974315,  0.67897575,  0.91820835,  1.15744096,
        1.39667356,  1.63590616,  1.87513877,  2.11437137,  2.35360397,
        2.59283657,  2.83206918,  3.07130178,  3.31053438,  3.54976699,
        3.78899959,  4.02823219,  4.26746479,  4.5066974 ,  4.74593   ,
        4.9851626 ,  5.22439521,  5.46362781,  5.70286041,  5.94209301,
        6.18132562,  6.42055822,  6.65979082,  6.89902343,  7.13825603,
        7.37748863,  7.61672123,  7.85595384,  8.09518644,  8.33441904,
        8.57365165,  8.81288425,  9.05211685,  9.29134945,  9.53058206,
        9.76981466, 10.00904726, 10.24827987, 10.48751247, 10.72674507,
       10.96597768, 11.20521028, 11.44444288, 11.68367548, 11.92290809,
       12.16214069, 12.40137329, 12.6406059 , 12.8798385 , 13.1190711 ,
       13.3583037 , 13.59753631, 13.83676891, 14.07600151, 14.31523412,
       14.55446672]), <BarContainer object of 60 artists>)
Text(0.5, 1.0, 'IPF')
Text(0.5, 44.49999999999998, 'Mean log2(CPM + 1)')
Text(1306.6024320987653, 0.5, 'Number of Genes')
>>> plt.suptitle('Gene Expression Distributions After Normalization', fontsize=14, fontweight='bold')
Text(0.5, 0.98, 'Gene Expression Distributions After Normalization')
>>> plt.tight_layout()
>>> plt.show()
>>> 
>>> df_filtered.to_csv('counts_filtered.csv')
>>> meta_de = pd.DataFrame({
...     'sample': ipf_samples + control_samples,
...     'group': ['IPF'] * len(ipf_samples) + ['Control'] * len(control_samples)
... }).set_index('sample')
>>> meta_de.to_csv('metadata.csv')
>>> print("Exported files:")
Exported files:
>>> print(f"  counts_filtered.csv  → {df_filtered.shape[0]} genes x {df_filtered.shape[1]} samples")
  counts_filtered.csv  → 15058 genes x 288 samples
>>> print(f"  metadata.csv         → {len(meta_de)} samples")
  metadata.csv         → 206 samples
