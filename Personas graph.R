library(ggplot2)
### Setting Raw Protype ###
testData <- read.table('data/car_setting.txt', stringsAsFactors = F)
colnames(testData) <- testData[1,]
testData <- testData[-1,]
testData <- testData[order(testData$Series),]
testData$Price <- as.numeric(testData$Price)
testData$Series <- factor(testData$Series, levels=c('长安CS75', '哈佛H6', '奔腾x80'))
p <- ggplot(testData, aes(x=Series, y=Price)) + xlab('') + ylab('')
p + geom_point(pch=1, cex=3) + geom_jitter(position=position_jitter(w=0.2, h=0.01), pch=20, cex=0.5, color='red') + facet_grid(.~Series, scale='free', space='free')

### V bar plot ###
library(grid)
library(gridExtra)
testData2 <- read.table('data/user_2.txt', stringsAsFactors =F, header=T)
testData2 <- as.data.frame(testData2)
testData2$City <- factor(testData2$City, levels=c('一线城市', '二线城市', '三线城市'))
testData2$Focus <- factor(testData2$Focus)
testData2[,3:5] <- testData2[,3:5] - 50
p.mid <- ggplot(testData2, aes(x=1, y=Focus)) + geom_text(aes(label=Focus)) + geom_segment(x=0.94, xend=0.96, yend=testData2$Focus) + geom_segment(x=1.04, xend=1.605, yend=testData2$Focus) + ggtitle('') + ylab(NULL) + scale_x_continuous(expand=c(0, 0), limits=c(0.94, 1.065)) + 
  theme(axis.title = element_blank(),
        panel.grid = element_blank(),
        axis.text.y = element_blank(),
        axis.ticks.y = element_blank(),
        panel.background = element_blank(),
        axis.text.x = element_text(color=NA),
        axis.ticks.x = element_line(color=NA),
        plot.margin = unit(c(1, -1, 1, -1), 'mm'))
p1 <- ggplot(testData2, aes(x=Focus, y=testData2[,3], fill=City)) + geom_bar(stat='identity', position='dodge') + ggtitle('长安CS75') +
  theme(axis.title.x=element_blank(),
        axis.title.y=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank(),
        panel.background = element_rect(colour = NA),
        legend.position = 'none',
        plot.margin = unit(c(1, -1, 1, 0), 'mm')) +
  scale_y_reverse() + coord_flip()
gg1 <- ggplot_gtable(ggplot_build(p1))
p2 <- ggplot(testData2, aes(x=Focus, y=testData2[,4], fill=City)) + geom_bar(stat='identity', position='dodge') + xlab(NULL) +
  ggtitle('哈佛H6') +
  theme(axis.title.x=element_blank(),
        axis.title.y=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank(),
        #legend.key.size = unit(0.3, 'cm'),
        legend.position = 'none',
        plot.margin = unit(c(1, 0, 1, -1), 'mm')) + coord_flip()
gg2 <- ggplot_gtable(ggplot_build(p2))
gg.mid <- ggplot_gtable(ggplot_build(p.mid))
grid.arrange(gg.mid, gg1, gg2, ncol=3, widths=c(1/9, 4/9, 4/9))
## User Right Plot ##
testData3 <- read.table('data/user_3.txt',header=T)
levels(testData3$City) <- c("一线城市", "二线城市", "三线城市")
testData3$Car <- factor(testData3$Car, levels=c('长安CS75', '哈佛H6', '奔腾X80'))
p1 <- ggplot(testData3, aes(x=Car, y=User, fill=City))
p1 + geom_bar(stat='identity', width=.5, position='dodge') + xlab('') + ylab('')

## Media Fisrt Plot ##
testData4 <- read.table('data/Media_1.txt', header=T)
testData4$US <- factor(testData4$US, levels=c('浏览用户','关注用户','预购用户')) 
p <- ggplot(testData4, aes(x=SC, y=User, fill=US)) + xlab('') + ylab('用户站比')
p + geom_bar(stat='identity', width=.5)

testData5 <- read.table('data/Media_2.txt', header=T)
testData5$US <- factor(testData5$US, levels=c('浏览用户','关注用户','预购用户'))
p <- ggplot(testData5, aes(x=CC, y=User, fill=US)) + xlab('') + ylab('用户站比')
p + geom_bar(stat='identity', width=.5, position='dodge')

testData6 <- read.table('data/Media_3.txt', header=T)
p <- ggplot(testData6, aes(x=CC, y=User)) + xlab('') + ylab('')
p + geom_bar(stat='identity', width=.5, colour='grey', fill='grey')

testData7 <- read.table('data/Media_4.txt', header=T, sep='\t')
testData7$UT <- factor(testData7$UT, levels=c('浏览用户', '关注用户','预购用户'))
p <- ggplot(testData7, aes(x=Focus, y=User.Percent, fill=UT)) + xlab('') + ylab('')
p + geom_bar(stat='identity', width=.5)

