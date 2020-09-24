setwd("D:\\college\\Data Mining\\Data Mining Experiment 5")

install.packages("rpart.plot") 
library("rpart") 
library("rpart.plot")

#Read the data 
play_decision <- read.table("D:\\college\\Data Mining\\Data Mining Experiment 5\\Decision_Tree.csv",header=TRUE,sep=",")
play_decision
summary(play_decision)


fit <- rpart(Play ~ Outlook + Temperature + Humidity + Wind, method="class", data=play_decision,control=rpart.control(minsplit=1) )
summary(fit)

rpart.plot(fit, type=4, extra=1)

Newdata <-data.frame (Outlook="rainy", Temperature="mild", Humidity="high", Wind=FALSE)
Newdata

predict(fit,newdata = newdata,type = c("prob"))
predict(fit,newdata = newdata,type = c("class"))