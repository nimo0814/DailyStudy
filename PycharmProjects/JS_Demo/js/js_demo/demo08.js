//构造函数：当一个函数与new关键字一起被调用的时候就会作为一个构造函数
function Person(name,age){
  this.name=name;
  this.age=age;
}

Person.prototype.say=function (){
  console.log('我是'+this.name);
}
var person=new Person('阿梅',12);
person.say();
console.log(person);
