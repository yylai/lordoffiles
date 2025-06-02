const rows = document.querySelectorAll('div.flex.flex-wrap.z-1.rounded-xl');
const results = Array.from(rows).map(row => {
  const children = row.children;
  return {
    rank: children[0]?.textContent.trim(),
    name: children[1]?.textContent.trim(),
    score: children[4]?.querySelector('div').textContent.trim()
  };
});
console.log(results);