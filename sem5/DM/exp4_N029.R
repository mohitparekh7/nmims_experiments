
x=runif(100,0,10)
x

y <- 5 + 6*x + rnorm(100)
y

plot(x,y)

d <- lm(y ~ x) 
str(d) 
print(d)

par(mfrow=c(1,1))

ypred <- predict(d) 
par(mfrow=c(1,1))
plot(y,y, type="l", xlab="true y", ylab="predicted y") 
points(y, ypred)

d1 <- summary(d) 
print(d1) 

cat("OLS gave slope of ", d1$coefficients[2,1],
    "and an R-sqr of ", d1$r.squared, "\n")

#training data
x1 <- runif(100) 
y1 = 5 + 6*x1 + 0.1*x1*x1 + rnorm(100) 

#generate model
m <- lm(y1 ~ x1)  # linear model y1=a+bx1;

#test data
x2 <- runif(100) 
y2 = 5 + 6*x2 + 0.1*x2*x2 + rnorm(100) 


plot(x1,y1)  #same as  plot(y1~x1) 
plot(x2,y2)
print(m)
str(m)


m1 <- summary(m) 
print(m1) 

#prediction
test_data=data.frame(x2)

y2pred <- predict(m,test_data)

par(mfrow=c(1,1)) #fill in rowise, like subplot of matlab

plot(y2,y2, type="l", xlab="true y", ylab="predicted y",sub="Test data") 
points(y2, y2pred, col='blue')


