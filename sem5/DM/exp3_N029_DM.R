
setwd("D:\\college\\Data Mining\\Data_Mining_Experiment 3")
df<- read.csv("customer.csv", stringsAsFactors = FALSE)



str(df)
summary(df)

install.packages("Hmisc")
require(Hmisc)

describe(df)

df$MonthlyCharges

# to check if there are any missing values
is.na(df$MonthlyCharges)

# to check how many missing values are present
sum(is.na(df$MonthlyCharges))

install.packages("tidyverse")
library(tidyverse)
install.packages("tidyr") #for pipe operator
library(tidyr)
install.packages("dplyr") #for distinct function
library(dplyr)

install.packages("magrittr")
library(magrittr)

#find unique values in MonthlyCharges column
df %>% distinct(MonthlyCharges)

#summarise distinct values
df %>% summarise(n= n_distinct(MonthlyCharges))

#doing multiple things in summarise
df%>% summarise(n=n_distinct(MonthlyCharges),count = sum(is.na(MonthlyCharges)),M = mean(MonthlyCharges, na.rm=TRUE))

# replace missing values with median
df <- df %>% mutate(MonthlyCharges =replace(MonthlyCharges,is.na(MonthlyCharges),median(MonthlyCharges,na.rm = TRUE)))

# checking for nonstandard missing values:
is.na(df$TotalCharges) 
df%>% summarise(n=sum(is.na(TotalCharges)))

# change the 'na' and 'N/A' values to NA in TotalCharges column. Then count and display null values in totalcharges column
df <- df %>%
  mutate(TotalCharges =replace(TotalCharges,TotalCharges=='na',NA)) %>%
  mutate(TotalCharges =replace(TotalCharges,TotalCharges=='N/A',NA))
df%>% summarise(n=sum(is.na(TotalCharges)))
#	Display all values in totalcharges column
df$TotalCharges

#convert Totalcharges to Numeric using as.numeric command
df$TotalCharges<-as.numeric(df$TotalCharges)

#Describe structure of dataframe 
str(df)

#replace the missing values with mean value in Totalcharges column and display totalcharges column. Ignore null values while calculating mean value.
df <- df %>% 
  mutate(TotalCharges
         = replace(TotalCharges,is.na(TotalCharges),mean(TotalCharges,na.rm = TRUE)))
df$TotalCharges

#check 'paymentmethod' column for null values and comment on the result.
is.na(df$PaymentMethod)

#Replace '- -' by 'NA' and null value by 'unavailable'
df<- df%>%
  mutate(PaymentMethod = replace(PaymentMethod , PaymentMethod == '--',NA)) %>%
  mutate(PaymentMethod = replace(PaymentMethod , is.na(PaymentMethod),"Unavailable"))

df$PaymentMethod

df %>% mutate(PecentageCharges=TotalCharges/100)

df

