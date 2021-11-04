var count=function fn(num){
  if(num<0){
    return num;
  }
  return  fn(num-1)+num;
}
count(5);
