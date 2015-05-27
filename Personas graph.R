library(ggplot2)
library(grid)
library(gridExtra)

target_car = '长安CS75'

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

### 补充百分比，需要给出具体数值，以便生成合理的策略 ###
testData8 <- read.table('data/Media_6.txt', header=T, sep='\t')
### Rebuild Data for Barplot ###
testData8$CHsubUser <- testData8$UV_channel - testData8$UV_target
testData8$UT <- c('目标用户')
colnames(testData8)[2] <- 'UV'
tmp <- as.data.frame(cbind(testData8$SC, c('其他用户'), testData8$CHsubUser))
colnames(tmp) <- c('SC', 'UT', 'UV')
levels(tmp$SC) <- levels(testData8$SC)
testData8 <- testData8[,c(-3, -4)]
testData8 <- rbind(testData8, tmp)
testData8$UV <- as.integer(testData8$UV)/10000
################################
p <- ggplot(testData8, aes(x=SC, y=UV, fill=UT))
p + geom_bar(stat='identity')

## Competitive Addict ##
## Background Default Pic ##
basedata <- read.table('data/competitive.txt', header=T)
basedata$Cluster <- factor(basedata$Cluster, levels=c('低端车','经济型车','中端车','中高端车','豪车'))
basedata$competitive <- basedata$Car/basedata$User
legendLab <- paste(levels(basedata$Cluster), "\n", basedata$Car, '%')
## To Write the Exactly Position of text, we have to add a cumulative percent ##
Cumulative_1 <- function(x) {
  tmpa = 0
  tmpb = rep(0, length(x))
  for (ele in 1:length(x)) {
  tmpb[ele] = x[ele] + tmpa
  tmpa = tmpa + x[ele]
  }
  tmpb
}
zo_trans <- function(x) {
  return((x-min(x))/(max(x)-min(x)))
}
basedata$cumulative <- Cumulative_1(basedata$Car)
p <- ggplot(data=basedata, aes(x=factor(1), y=Car, fill=zo_trans(competitive))) + scale_fill_continuous(low='white', high='red', guide=guide_legend(title="竞争程度")) + ggtitle('车型竞争环境')
p + geom_bar(stat='identity', width=1) + geom_text(data=basedata, aes(y=cumulative-10,label=legendLab)) + coord_polar(theta="y") + ylab('') + xlab('') 

## Board of audition ##
testdata7 <- read.table('data/user_4.txt', header=T)
p <- ggplot(testdata7, aes(x=Car, y=User))
fillcolor <- rep('grey', 6)
fillcolor[levels(testdata7$Car) == '长安cs75'] <- 'red'
p + geom_bar(stat='identity', fill=fillcolor, width=.6)

## The First Pic of Media ##
testData9 <- read.table('data/Media_01.txt', header=T, sep='\t')
### Transform to fit ###
tmpdata <- data.frame(t(c(0,0,0)))
colnames(tmpdata) <- c('Car', 'Mon', 'URL')
for (ele in 2:length(testData9)) {
  tmpvec <- rep(colnames(testData9)[ele], 6)
  tmpdata <- rbind(tmpdata, cbind(Car=tmpvec, Mon = testData9[, 1], URL= testData9[, ele]))
  rm(tmpvec)
}
tmpdata <- tmpdata[-1,]
tmpdata$URL <- as.numeric(tmpdata$URL)
tmpdata$Car <- factor(tmpdata$Car, levels=c("传祺GS4", "哈佛H6", "奔腾X80", "瑞虎5", "长安CS75", "陆风X5"))
fillcolor <- rep('black', length(levels(tmpdata$Car)))
fillcolor[levels(tmpdata$Car) == target_car] <- 'red'
p <- ggplot(tmpdata[tmpdata$Mon==6,], aes(x=Car, y=URL)) + ylab('') + xlab('') + theme_bw() +  scale_colour_identity()  + theme(axis.text.x = element_blank(), axis.ticks.x = element_blank())
p + geom_text(aes(y=URL+1, color=fillcolor), label=levels(tmpdata$Car)) + geom_point(color=fillcolor, size=3,pch=20)

p <- ggplot(tmpdata[tmpdata$Car=='长安CS75',][-1:-3,], aes(x=Mon, y=URL, group=Car))
p <- p + geom_line()
ggsave(p, file='a.png', width=20, height=11, unit='mm')
### every pic for brief trends ###
dpic <- function(n) {
  p <- ggplot(n, aes(x=Mon, y=URL, group=Car)) + theme(panel.background=element_blank(), axis.title=element_blank(), axis.text=element_blank(), axis.ticks=element_blank(), axis.line=element_line(color='white'), line=element_line(color='white'))
#  p <- p + geom_line(color='blue') + geom_point(fill='black', color='blue', pch=20, cex=0.2)
  p <- p + geom_smooth(color='blue', method='loess')
}
m = dpic(tmpdata[tmpdata$Car=='长安CS75',][-1:-3,])
m
for (nam in levels(tmpdata$Car)) {
  fname = paste(nam, '.png', sep='')
  print(fname)
  p <- dpic(tmpdata[tmpdata$Car==nam,][-1:-3,])
  p
  ggsave(p, file=fname, width=60, height=36, unit='mm')
}

