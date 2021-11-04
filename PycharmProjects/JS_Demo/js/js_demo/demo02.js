var obj={
  name:'小明',
  age:12,
  say:function(){
    console.log('我叫'+this.name+',我的年龄是'+this.age+'岁');
  },
  'father-name':'小蓝',
};

console.log(obj.name);
console.log(obj['father-name'])
obj.say();

var obj=new Object();
obj.name ='小明';


