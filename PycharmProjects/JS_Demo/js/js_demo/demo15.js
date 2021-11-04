var data={_id:'',createdAt:1635300722054,content:''};
var date=new Date(data.createdAt);
var YYYY=date.getFullYear();
var MM=date.getMonth()+1;
var DD=date.getDate();
var hh=date.getHours();
var mm=date.getMinutes();
var ss=date.getSeconds();

console.log([YYYY,'/',MM,'/',DD,' ',hh,':',mm,':',ss].join(''));
