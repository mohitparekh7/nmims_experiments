ls()
lab1 <- read.table("D:\\college\\Data Mining\\lab1_01.txt", sep = "|", header = TRUE)
lab2 <- read.table("D:\\college\\Data Mining\\lab1_02.txt", sep = "|", header = TRUE)

head(lab1, n=10)
tail(lab2, n=10)

summary(lab1)

# and remove some extraneous variables (columns)
nlab1 <- lab1[,2:3]

# what did we get? 

hinc <- lab1$hinc 
rooms <- lab1$rooms 
nlab11 <- data.frame(hinc, rooms) 

dim(nlab1)
typeof(nlab1)
class(nlab1)
print(nlab1)

# what does summary() say now? 

summary(nlab1)

# same correlation values or different? 

cor(nlab1)

save(lab1, lab2, file="Labs.Rdata")

ls()      

ds <- lab1 
colnames(ds) <- c("income", "rooms")

summary(ds$income) 
range(ds$income) 
sd(ds$income) 
var(ds$income) 
plot(density(ds$income))

summary(ds$rooms) 
range(ds$rooms) 
sd(ds$rooms) 
plot(as.factor(ds$rooms))

(m <- mean(ds$income, trim=0.10) )

ds <- subset(ds, ds$income >= 10000 & ds$income < 1000000) 
summary(ds) 
quantile(ds$income, seq(from=0, to=1, length=11))

breaks <- c(0, 23000, 52000, 82000, 250000, 999999) 
labels <- c("Poverty", "LowerMid", "UpperMid", "Wealthy", "Rich") 
wealth <- cut(ds$income, breaks, labels) 

ds <- cbind(ds, wealth) 

head(ds)

wt <- table(wealth) 
percent <- wt/sum(wt)*100 
wt <- rbind(wt, percent) 
wt 
plot(wt)

nt <- table(wealth, ds$rooms)
print(nt) 
plot(nt)

rm(wealth,breaks,labels) 
save(ds, wt, nt, file="Census.Rdata")

library(MASS) 

with(ds, { 
  hist(income, main="Distribution of Household Income", freq=FALSE)
  lines(density(income), lty=2, lwd=2)
  xvals = seq(from=min(income), to=max(income), length=100) 
  param = fitdistr(income, "lognormal") 
  lines(xvals, dlnorm(xvals, meanlog = param$estimate[1], sdlog = param$estimate[2]),col= "blue") 
}) 

logincome = log10(ds$income) 
hist(logincome, main="Distribution of Household Income", freq=FALSE) 
lines(density(logincome), lty=2, lwd=2) 
xvals = seq(from=min(logincome), to=max(logincome), length=100) 
param = fitdistr(logincome, "normal") 
lines(xvals, dnorm(xvals, param$estimate[1], param$estimate[2]), lwd=2,col= "blue") 

with(ds, cor(income, rooms)) 
with(ds, cor(log(income), rooms))

boxplot(income ~ as.factor(rooms), data=ds, range=0, outline=F, log="y", xlab="# rooms", ylab="Income") 

boxplot(rooms ~ wealth, data = ds, main="Room by Wealth", Xlab="Category", ylab="# rooms") 






