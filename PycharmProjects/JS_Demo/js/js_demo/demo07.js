function sum(){
  var total=0;
  var i;
  var len;
  for(i=0,len=arguments.length;i<len;i++){
    total+=arguments[i];
  }
  return total;
}
var  total=sum(1,2,3,4,15);
console.log(total);
