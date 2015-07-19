library(tm)
library(ggplot2)

corpus <- Corpus(DirSource("dat/", encoding = "UTF-8"),readerControl = list(language = "en"))

corpus <- tm_map(corpus, stripWhitespace)
corpus <- tm_map(corpus, tolower)
corpus <- tm_map(corpus, removeWords, stopwords("english"))
corpus <- tm_map(corpus, stemDocument)

dtm <- DocumentTermMatrix(corpus)

findFreqTerms(dtm, 50)

termFrequency <- rowSums(as.matrix(dtm))
termFrequency <- subset(termFrequency, termFrequency>=10)
qplot(names(termFrequency), termFrequency, geom="bar", stat="identity") + coord_flip()

findAssocs(dtm, "coli", 0.99)
findAssocs(dtm, "bacteria", 0.90)

inspect(DocumentTermMatrix(corpus,
list(dictionary = c("bacteria", "metabolism", "aerob"))))

