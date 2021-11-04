var obj = [
  {
    path: '/',
    component: 'function() {}',
    children: [
      {
        path: 'note',
        component: 'function() {}',
      },
      {
        path: 'friends',
        component: 'function() {}',
      }
    ]
  },
  {
    path: '*',
    component: 'function() {}',
  }
];

var json1 = JSON.stringify(obj, null);
var json2 = JSON.stringify(obj, null, 2);
var json3 = JSON.stringify(obj, null, '*-*');

console.log(json1); // 没有格式
console.log(json2); // 使用两个空格控制的缩进
console.log(json3); // 使用 *-* 控制的缩进
