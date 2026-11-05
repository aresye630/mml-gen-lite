// 页签平铺验证：模拟 renderTabBar，检查 7 个页签是否同级平铺
// 用法: node app_tabs_check.js <app_v2.html>
const fs = require('fs');
const src = fs.readFileSync(process.argv[2], 'utf8');

let fail = 0, ok = 0;
function chk(desc, cond, extra) {
  if (cond) { ok++; console.log(`  [OK]   ${desc}`); }
  else { fail++; console.log(`  [FAIL] ${desc}${extra ? '  → ' + extra : ''}`); }
}

// ── ① 结构断言：不再有层级 ──
console.log('─── 结构：层级已消除 ───');
chk('LV1_TABS 常量已删除', !/const\s+LV1_TABS/.test(src));
chk('setLv1 函数已删除', !/function\s+setLv1/.test(src));
chk('S.lv1 状态字段已删除', !/S\.lv1\b/.test(src));
chk('renderTabBar 不再输出 lv2bar', !/lv2bar/.test(src.replace(/\/\*[\s\S]*?\*\//g, '')));
chk('不再按 lv1 过滤页签', !/t\.lv1\s*===\s*S\.lv1/.test(src));
chk('生成后跳转改用 pickTab', /pickTab\('gen'\)/.test(src));

// ── ② 渲染断言：真跑一次 renderTabBar ──
console.log('─── 渲染：7 个页签平铺一行 ───');
// 抽取 renderTabBar 函数体，构造最小运行环境
const m = src.match(/function renderTabBar\(\)\{([\s\S]*?)\n\}/);
if (!m) { console.log('  [FAIL] 未找到 renderTabBar'); process.exit(1); }
const esc = s => String(s == null ? '' : s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const S = {
  artifacts: { tabs: [
    {tab_id: 'exp-raw', label: '1 exp 原文', lv1: 'exp-raw', available: true, updated_at: 'x'},
    {tab_id: 'cards', label: '2 特性判定卡', lv1: 'cards', available: true, updated_at: 'x'},
    {tab_id: 'cmd-list', label: '3 命令清单', lv1: 'cmd-list', available: true, updated_at: 'x'},
    {tab_id: 'gen', label: '4 配置方案', lv1: 'gen', available: true, updated_at: 'x'},
    {tab_id: 'csv', label: '5 参数收集表', lv1: 'csv', available: true, updated_at: 'x'},
    {tab_id: 'mml', label: '6 纯 MML', lv1: 'mml', available: true, updated_at: 'x'},
    {tab_id: 'jobs', label: '7 任务历史', lv1: 'jobs', available: true, updated_at: null},
  ]},
  genTabVisible: true, curTab: 'csv', curSid: 'S1', analyzing: false,
  guide: {actions: []},
};
const $ = () => null;
const go = () => {};
const doUploadExp = () => {};
const renderTabBar = new Function('S', 'esc', '$', 'go', 'doUploadExp',
  m[1].replace(/S\.genTabVisible/g, 'S.genTabVisible'));
const html = renderTabBar(S, esc, $, go, doUploadExp);

const btns = html.match(/<button[^>]*data-tab="[^"]+"[^>]*>[^<]*<\/button>/g) || [];
chk('渲染出 7 个页签', btns.length === 7, `实际 ${btns.length}`);
chk('无 lv2bar 输出', !html.includes('lv2bar'));
chk('单行容器 lv1bar', (html.match(/class="lv1bar"/g) || []).length === 1);
btns.forEach((b, i) => {
  const id = (b.match(/data-tab="([^"]+)"/) || [])[1];
  const lb = (b.match(/>([^<]*)</) || [])[1];
  console.log(`         ${i + 1}. ${id.padEnd(10)} ${lb}`);
});

// ── ③ 可用性：不可用=灰化可见（不是消失）──
console.log('─── 可用性：灰化但始终可见 ───');
const S2 = JSON.parse(JSON.stringify(S));
S2.artifacts.tabs.forEach(t => {
  if (t.tab_id !== 'jobs') t.available = false;
  t.updated_at = null;                 // ← 关键：gen 的可用性判据是「有产物」，
});                                    //   必须清掉 updated_at 才能真正置为不可用
S2.genTabVisible = false;
const html2 = renderTabBar(S2, esc, $, go, doUploadExp);
const btns2 = html2.match(/<button[^>]*data-tab="[^"]+"[^>]*>[^<]*<\/button>/g) || [];
chk('不可用时 7 个页签仍渲染（不消失）', btns2.length === 7, `实际 ${btns2.length}`);
// 6 个呈现页全部不可用（1/2/3/4/5/6），只有 7 任务历史可用
const offN = (html2.match(/class="tab off/g) || []).length;
chk('6 个呈现页全部灰化', offN === 6, `off 数 ${offN}（期望 6）`);
chk('灰化页签 disabled 不可点', btns2.filter(b => b.includes('disabled')).length === 6);
chk('任务历史始终可用', !btns2.find(b => b.includes('data-tab="jobs"')).includes('disabled'));
// ★ 判别力关键：灰化 ≠ 隐藏（旧实现会 filter 掉整个页签导致布局跳动）
chk('灰化页签**仍可见**（有 label 文本）',
  btns2.filter(b => b.includes('off') && />[^<]+</.test(b)).length === 6,
  '灰化页签必须仍带 label，不能是空壳');
// ★ 每页签 data-lv1 各自独立（证明无分组）
const lv1s = btns2.map(b => (b.match(/data-lv1="([^"]+)"/) || [])[1]);
chk('每个页签 data-lv1 互不相同（无分组）',
  new Set(lv1s).size === 7, `去重后 ${new Set(lv1s).size} 个`);

console.log(`\n结果: ${ok}/${ok + fail} 通过`);
process.exit(fail ? 1 : 0);
