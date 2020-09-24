setwd("D:\\college\\Data Mining\\Data Mining exp 6")
getwd()

nb <-read.table("D:\\college\\Data Mining\\Data Mining exp 6\\Naive_Bayes.csv",sep = ",",header = TRUE)
nb
nb1<-nb[!(nb$Age =='<=30' &  nb$Income=='Medium' & nb$Jobsatisfaction=='Yes' & nb$Desire=='Fair'),]
nb1

n_age = nb1$Age
n_in = nb1$Income
n_js = nb1$Jobsatisfaction
n_des = nb1$Desire
n_enroll = nb1$Enrolls

yes_age=0
yes_in=0
yes_js=0
yes_desire = 0
yes_enrol=0

no_age=0
no_in=0
no_js=0
no_desire = 0
no_enrol=0

for (i in 1:14) {
  if(n_age[i] == '<=30' & n_enroll[i] == 'Yes'){
    yes_age = yes_age +1
  }
  if(n_in[i] == 'Medium' & n_enroll[i] == 'Yes'){
    yes_in = yes_in+1
  }
  if(n_js[i] == 'Yes' & n_enroll[i] == 'Yes'){
    yes_js = yes_js +1
  }
  if(n_des[i] == 'Fair' & n_enroll[i] == 'Yes'){
    yes_desire = yes_desire +1
  }
  if(n_enroll[i] == 'Yes'){
    yes_enrol = yes_enrol +1
  }
  
}
for (i in 1:14) {
  if(n_age[i] == '<=30' & n_enroll[i] == 'No'){
    no_age = no_age +1
  }
  if(n_in[i] == 'Medium' & n_enroll[i] == 'No'){
    no_in = no_in+1
  }
  if(n_js[i] == 'Yes' & n_enroll[i] == 'No'){
    no_js = no_js +1
  }
  if(n_des[i] == 'Fair' & n_enroll[i] == 'No'){
    no_desire = no_desire +1
  }
  if(n_enroll[i] == 'No'){
    no_enrol = no_enrol +1
  }
  
}

ans_yesAge = yes_age/yes_enrol
ans_yesInc = yes_in/yes_enrol
ans_yesJs = yes_js/yes_enrol
ans_yesDesire = yes_desire/yes_enrol

ans_noAge = no_age/no_enrol
ans_noInc = no_in/no_enrol
ans_noJs = no_js/no_enrol
ans_noDesire = no_desire/no_enrol

ans_yes = (ans_yesAge*ans_yesInc*ans_yesJs*ans_yesDesire)*(yes_enrol/14)
ans_no = (ans_noAge*ans_noDesire*ans_noJs*ans_noInc)*(no_enrol/14)

print(ans_yes)
print(ans_no)

if(ans_yes>ans_no){
  print("Yes")
}else{
  print("No")
}

install.packages("naivebayes")
library(naivebayes)

trainingData = nb[1:14,]
testData = nb[15,]

nb2 <- naive_bayes(Enrolls ~ ., trainingData , laplace = 1)
summary(nb2)

predict(nb2 , testData , type = "prob")


