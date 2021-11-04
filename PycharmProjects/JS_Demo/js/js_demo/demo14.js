var gugugu={
  name:'?王',
  hobby:'放鸽子',
};
var desc=Object.create(null);
desc.enumerable=false;
desc.value='最强歌手';

Object.defineProperty(gugugu,'nickname',desc);
console.log(Object.keys(gugugu));
console.log(Object.getOwnPropertyNames(gugugu));
