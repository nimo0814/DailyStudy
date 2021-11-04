//使用 Object.prototype.hasOwnProperty 来判断一个属性是否只处于其本身而不在原型上。
var me={height:180,weight:70};
var you=Object.create(me);
you.age=11;
var i;
for(i in you){
  if(you.hasOwnProperty(i)){
    console.log(i);
  }
}
