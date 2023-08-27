silumawig = function(X,Y){

  
  # Initialize
  X = X[order(-X)]
  Y = Y[order(-Y)]  
  d = 0
  N = min(length(X),length(Y))
  X = X[1:N]
  Y = Y[1:N]
  Z = abs(X-Y)
  l = which(Z==max(Z))[1]
  d=0
  

  if(N==1){
    d = abs(X[1]-Y[1])/2
    return(d)
  }
  
  if(Y[l]>X[l]){
    S=Y
    Y=X
    X=S
  }
  
  if(length(which(X>=Y))==N){
    d = abs(X[l]-Y[l])/2
    return(d)
  }
  else{
    m=which((X-Y)==min(X-Y))[1]
   if(Y[m]-X[m] > Y[l] & m<l){
     return(silumawig(X[1:l],Y[1:l]))
   }
    else if(X[l]-Y[l] > X[m] & m>l){
      return(silumawig(X[1:m],Y[1:m]))
    }
    else{
      d = (X[l]-Y[l]-X[m]+Y[m])/2
      return(d)
    }
  }
}
  