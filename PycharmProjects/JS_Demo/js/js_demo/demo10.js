function Car(color,maxSpeed){
  this.color=color;
  this.maxSpeed=maxSpeed;
}
Car.prototype.bibi=function (){
  console.log('哔哔！');
};
var car=new Car('red',9999999)
console.log(car);
