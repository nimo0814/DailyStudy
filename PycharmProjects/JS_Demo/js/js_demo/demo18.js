var obj={prop:'value'};
var newObj=JSON.parse(JSON.stringify(obj));
newObj.prop='new value';
console.log(obj);
console.log(newObj);
