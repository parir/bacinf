library(tm)
library(ggplot2)

corpus <- Corpus(DirSource("dat/", encoding = "UTF-8"),readerControl = list(language = "en"))

corpus <- tm_map(corpus, stripWhitespace)
corpus <- tm_map(corpus, tolower)
corpus <- tm_map(corpus, removeWords, stopwords("english"))
corpus <- tm_map(corpus, stemDocument)

dtm <- DocumentTermMatrix(corpus)

findFreqTerms(dtm, 50)

termFrequency <- colSums(as.matrix(dtm))
term_most <- tail(sort(termFrequency), 30)
qplot(names(term_most), term_most, geom="bar", stat="identity") + coord_flip()

findAssocs(dtm, "coli", 0.99)
findAssocs(dtm, "bacteria", 0.90)
findAssocs(dtm, names(term_most), rep(0.99, length(term_most)))

keywords <- readLines("db/keywords.txt")
key_hits <- inspect(DocumentTermMatrix(corpus, list(dictionary = keywords)))
key_hits[,which(colSums(key_hits)>1)]


