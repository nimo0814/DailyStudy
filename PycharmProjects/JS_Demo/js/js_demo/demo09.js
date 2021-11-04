var person={
  'name':'小明',
  'age':17,
  'isAdult':false,
  sex:'man',
  hobby:['eat','sleep','play doudou'],
  parents:{
    mather:{
      name:'大红',
    },
    father:{
      name:'大明',
    },
  },
  say:function (){
    console.log('我叫'+this.name+',我今年'+this.age+'岁了。');
  },

};
console.log(person);
