library('ggplot2')
RawData <- read.csv('Demo_competitive.txt', header=F, sep=',')
rownames(RawData) <- RawData[,1]
RawData <- RawData[,2:20]

## Generate Range of Auto Price ##
PriceRange <- apply(RawData, 1, range, na.rm=T)
rownames(PriceRange) <- c('min', 'max')
PriceRange <- t(PriceRange)
