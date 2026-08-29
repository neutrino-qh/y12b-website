const fs = require('fs');
const { JSDOM } = require('jsdom');

const html = fs.readFileSync('index.html', 'utf8');

// mock layout APIs jsdom lacks
const dom = new JSDOM(html, {
  runScripts: 'dangerously',
  pretendToBeVisual: true,
  beforeParse(window) {
    window.scrollTo = (...args) => {
      window.__scrollCalls = window.__scrollCalls || [];
      window.__scrollCalls.push(args);
    };
    window.HTMLElement.prototype.scrollIntoView = function(){ window.__scrollIntoView = true; };
    window.Element.prototype.getBoundingClientRect = function(){
      // give each prow a distinct fake top so we can verify target math
      const id = this.id || '';
      const tops = {'01-thi-thi':1500,'00-bat-trang':3000,'02-quoc-anh':4500,'03-phu-tho':6000,'04-hado':7500,'05-mimosa':9000};
      const top = tops[id] !== undefined ? tops[id] : 0;
      return { top, left:0, right:0, bottom:0, width:0, height:0 };
    };
  }
});

const { window } = dom;
const { document } = window;

function fire(el, type){
  const ev = new window.MouseEvent(type, { bubbles:true, cancelable:true });
  el.dispatchEvent(ev);
}

// 1) open menu
const btn = document.getElementById('menuBtn');
fire(btn, 'click');
const drop = document.getElementById('menuDrop');
console.log('menu opened:', drop.classList.contains('open'));

// 2) click a project name in the menu
const link = drop.querySelector('a[href="#02-quoc-anh"]');
console.log('link found:', !!link, link && link.getAttribute('href'));
fire(link, 'click');

// 3) inspect scroll call
const calls = window.__scrollCalls || [];
console.log('scrollTo calls:', JSON.stringify(calls));
if (calls.length) {
  const arg = calls[0][0];
  // expected y = target top (4500) + scrollY(0) - 80 = 4420
  console.log('expected y ~4420, got:', arg.top, 'behavior:', arg.behavior);
  console.log('SCROLL TEST:', (arg.top === 4420 && arg.behavior === 'smooth') ? 'PASS' : 'FAIL');
} else {
  console.log('SCROLL TEST: FAIL (no scrollTo call)');
}

// 4) menu still open right after click (closes after 450ms) — check immediately
console.log('menu open immediately after click (should be true):', drop.classList.contains('open'));

// 5) hover effect class/style - just confirm link exists & is <a>
console.log('project link tag:', link && link.tagName);

// cleanup jsdom
dom.window.close();
