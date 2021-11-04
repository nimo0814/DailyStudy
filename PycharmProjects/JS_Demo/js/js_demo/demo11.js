//Object.create 会根据传递过去的对象生成一个新的对象，作为参数传递的对象会作为新对象的原型。
var parent={
  walk:function(){
    console.log('走路');
  },
};
var son=Object.create(parent);
console.log(parent===son);
son.walk();
