##
##  membershipAttack.r
##
##  demonstrate membership attacks of Homer et al. (2008) and of Dwork, Smith, Steinke, Ullman, Vadhan (2015).
##
##  jH 2019.2.11
##

rm(list=ls())		# Remove any objects in memory
par(mfrow=c(1,1))   # Rebuild fresh plot window, if previously divided


#### Parameters ####
set.seed(123)
k.attributes <- 100
n.sims<- 10000
n.samples <- 10
null.sims <- 1000

## Generate underlying population attributes
population.prob <- runif(n=k.attributes, min=0, max=1)
population.mean <- 2*(population.prob-0.5)              # Because we are recoding to {-1,1} in next function

## A utility function to create data from the population
rmvbernoulli <- function(n=1, prob){
  history <- matrix(NA, nrow=n, ncol=length(prob))
  for(i in 1:n){
    x<- rbinom(n=length(prob), size=1, prob=prob)
    x[x==0] <- -1      								# Transform from {0,1} to {-1,1}
    history[i,] <- x
  }
  return(history)
}

## Some potential test statistics
test.Homer <- function(alice, sample.mean, population.mean, referent){
  test.statistic <- sum(abs(alice - population.mean) - abs(alice - sample.mean))
  return(test.statistic)
}

# This is the Dwork et al. test using the population means
test.Dwork <- function(alice, sample.mean, population.mean, referent){
  test.statistic <- sum(alice * sample.mean) - sum(population.mean * sample.mean)
  return(test.statistic)
}

### This is the Dwork et al. test using only a single individual from the population as a referent
# test.Dwork <- function(alice, sample.mean, population.mean, referent){
# 	test.statistic <- sum(alice * sample.mean) - sum(referent * sample.mean)
# 	return(test.statistic)
# }


## A null distribution and critical value generator
nullDistribution <- function(null.sims=1000, alpha=0.05, fun, population.prob){
  population.mean <- 2*(population.prob-0.5)
  hold <- rep(NA,null.sims)
  for(i in 1:null.sims){
    sample <- rmvbernoulli(n=n.samples, prob=population.prob)
    nullAlice <- rmvbernoulli(n=1, prob=population.prob)
    referent <- rmvbernoulli(n=1, prob=population.prob)
    sample.mean <- apply(sample, MARGIN=2, FUN=mean)
    hold[i] <- eval(fun(alice=nullAlice, sample.mean=sample.mean, population.mean=population.mean, referent=referent))
  }
  nullDistribution <- sort(hold, decreasing=TRUE)
  criticalValue <- nullDistribution[round(alpha*null.sims)]
  return(list(nullDist=nullDistribution, criticalVal=criticalValue))
}


## Visualize the null distribution

showdist <- function(x,criticalvalue, main="", bw="nrd0"){
  testdens <- density(x, bw=bw)
  plot(testdens, main=main, xlab="Test Statistic")
  semi.blue <- rgb(0,90,239,180,maxColorValue=255)          # Slightly transparent colors
  semi.red  <- rgb(239,90,0,180,maxColorValue=255)
  flag <- testdens$x < criticalvalue
  polygon( c(min(testdens$x), testdens$x[flag], criticalvalue), y=c(0, testdens$y[flag], 0), col=semi.blue)
  polygon( c(criticalvalue, testdens$x[!flag], max(testdens$x)), y=c(0, testdens$y[!flag], 0), col=semi.red)
  abline(v=criticalvalue, lwd=1.5)
  accept.frac <- round(100*mean(x>criticalvalue))/100
  text(x=criticalvalue, y=0.8*max(testdens$y), labels=paste("OUT "), pos=2)
  text(x=criticalvalue, y=0.8*max(testdens$y), labels=paste(" IN"), pos=4)
  text(x=criticalvalue, y=0.7*max(testdens$y), labels=paste(accept.frac), pos=4)
}


## Find the null distribution for test1
output <- nullDistribution(fun=test.Homer, population.prob=population.prob)
testdist <- output$nullDist
criticalValue <- output$criticalVal
showdist(testdist, criticalValue, main="Null Distribution with Critical Value")

#### Export graph to .pdf ####
dev.copy2pdf(file="./figs/nullDistribution.pdf")




## Simulate

history <- matrix(NA, nrow=n.sims, ncol=9)														# Matrix to store results

myalpha <-0.01
nullDist.Homer<-nullDistribution(fun=test.Homer, population.prob=population.prob, alpha=myalpha)	# Find null distributions
nullDist.Dwork<-nullDistribution(fun=test.Dwork, population.prob=population.prob, alpha=myalpha)

for(i in 1:n.sims){
  # Simulate data
  sample <- rmvbernoulli(n=n.samples, prob=population.prob)
  sample.mean <- apply(sample, MARGIN=2, FUN=mean)
  alice <- sample[1,]
  nullAlice <- rmvbernoulli(n=1, prob=population.prob)
  referent <- rmvbernoulli(n=1, prob=population.prob)

  # Conduct tests
  test.alice.Homer <- test.Homer(alice=alice, sample.mean=sample.mean, population.mean=population.mean, referent=referent)
  test.alice.Dwork <- test.Dwork(alice=alice, sample.mean=sample.mean, population.mean=population.mean, referent=referent)
  test.nullAlice.Homer <- test.Homer(alice=nullAlice, sample.mean=sample.mean, population.mean=population.mean, referent=referent)
  test.nullAlice.Dwork <- test.Dwork(alice=nullAlice, sample.mean=sample.mean, population.mean=population.mean, referent=referent)

  # Store simulated values
  history[i,1]<-i
  history[i,2]<-test.alice.Homer
  history[i,3]<-test.alice.Homer>nullDist.Homer$criticalVal
  history[i,4]<-test.nullAlice.Homer
  history[i,5]<-test.nullAlice.Homer>nullDist.Homer$criticalVal
  history[i,6]<-test.alice.Dwork
  history[i,7]<-test.alice.Dwork>nullDist.Dwork$criticalVal
  history[i,8]<-test.nullAlice.Dwork
  history[i,9]<-test.nullAlice.Dwork>nullDist.Dwork$criticalVal

}


#### Export graph to .pdf ####

par(mfrow=c(2,2))
showdist(history[,2], criticalvalue=nullDist.Homer$criticalVal, main="Homer Alice", bw=0.5)
showdist(history[,4], criticalvalue=nullDist.Homer$criticalVal, main="Homer Null", bw=0.5)
Tvalue <- sqrt(8*k.attributes * log(1/myalpha))
showdist(history[,6], criticalvalue=nullDist.Dwork$criticalVal, main="Dwork Alice", bw=0.5)
abline(v=Tvalue, col="red", lty=2)
showdist(history[,8], criticalvalue=nullDist.Dwork$criticalVal, main="Dwork Null", bw=0.5)
abline(v=Tvalue, col="red", lty=2)

dev.copy2pdf(file="./figs/membershipAttack.pdf")





