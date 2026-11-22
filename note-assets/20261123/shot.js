const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:670},deviceScaleFactor:1.5});
for(const n of ['00_cover','01_seat','02_compare','03_rules','04_cards','05_flow']){await p.goto('file://'+process.cwd()+'/src/'+n+'.html');await p.waitForTimeout(300);
await p.screenshot({path:n+'.png',fullPage:n!=='00_cover'});}
await b.close();})();
