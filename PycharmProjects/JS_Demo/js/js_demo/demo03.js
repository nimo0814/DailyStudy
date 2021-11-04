var num=17;
var flag=false;
var len;
var i;

for (i=2,len=17-1;i<=len;i++){
  if (num%i===0){
    flag=true;
    break;
  }
}

if (flag){
  console.log(num+'不是质数');
}else {
  console.log(num+'是质数');
}
