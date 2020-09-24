ls()

setwd("D:\\college\\Data Mining")
lab1 <- read.table("lab1_01.txt",sep = "|", header = TRUE)
lab2 <- read.table("lab1_02.txt",sep = "|", header = TRUE)

head(lab1,n=10)
tail(lab2,n=10)

summary(lab1)

nlab1 <- lab1[,2:3]

nlab11 <- data.frame(lab1$hinc, lab1$rooms) 
names(nlab11) = c("hinc","rooms") 

dim(nlab1) 
typeof(nlab1) 
class(nlab1) 

summary(nlab1) 
cor(nlab1) 

cor(lab1)

# 7 
rm(lab1)
lab1 <- nlab1
save(lab1,lab2,file="Labs.Rdata")
rm(lab1,lab2)

ls()

typeof(nlab1)
class(nlab1)
attributes(nlab1)

names(nlab1)
dim(nlab1)

tellme <- function(x){
  print(x)
}
tellme("MOHIT N029")