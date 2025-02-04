# datach("package:ggplot2", unload=TRUE)
# remove.packages(("ggplot2"))
# install.packages("ggplot2")

if (!requireNamespace("ggplot2", quietly=TRUE)) {
    install.packages("ggplot2")
}

library(ggplot2)

data(ChickWeight)
head(ChickWeight)