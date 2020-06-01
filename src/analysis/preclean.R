library(data.table)

preclean <- fread('../../gen/data-preparation/output/dataset.csv')

# tag retweets
#preclean[, retweet:=FALSE]
#preclean[grepl('^RT', text), retweet:=TRUE]
preclean <- preclean[positivity>0| negativity>0]
dir.create('../../gen/analysis/temp/', recursive = TRUE)
dir.create('../../gen/analysis/output/', recursive = TRUE)
fwrite(preclean, '../../gen/analysis/temp/preclean.csv')


 

