function isPrimeNumber(num){
  var flag=false;
  var i;
  var len;
  for (i=2,len=num-1;i<=len;i++){
    if(num%i===0){
      flag=true;
      break;
    }
  }
  return flag;
}
var num=10;
var result=isPrimeNumber(num);
console.log(result);
