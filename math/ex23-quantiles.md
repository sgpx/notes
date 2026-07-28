# quantiles and torch.nanquantiles

qunatile is a statistical cutoff that divides a sorted dataset into equal sized adjacent subgroups

# types of quantiles

- median (2 quantile) : splits data into two equal groups, each representing 50% of the data
- quartiles (4 quantiles) : splits data in four equal groups, each representing 25% of the data
- quintiles (5 quantiles): splits the data into five equal groups, each representing 20% of the data
- deciles (10 quantiles) : splits the data into ten equal groups, each representing 10% of the data
- percentiles (100 quantiles): splits the data into 100 equal groups, each representing 1% of the data

# torch.nanquantiles

skips NaN values while trying to compute quantiles

>>> torch.nanquantile(torch.linspace(0,100,20), torch.tensor(0.5)) # represents 50th percentile
tensor(50.)

>>> torch.nanquantile(torch.linspace(0,100,100), torch.tensor(0.325)) # interpolates using formula q = N*i giving a value that doesn't exist in input tensor

tensor(32.5000)
>>> torch.nanquantile(torch.linspace(0,100,100), torch.tensor(0.325), interpolation='nearest')
tensor(32.3232)
