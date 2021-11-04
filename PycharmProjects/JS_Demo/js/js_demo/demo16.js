var user = {
  name: '小明',
  age: 14,
  skill: ['HTML', 'Java'],
};

var json = JSON.stringify(user, function(key, value) {
  if (key === '') {
    return value;
  }

  return '我是处理过的值';
});

console.log(json);
