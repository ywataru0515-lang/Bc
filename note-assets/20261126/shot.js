const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:670},deviceScaleFactor:1.5});
for(const n of ['02_ratio','03_cases','04_compare','06_check']){await p.goto('file://'+process.cwd()+'/src/'+n+'.html');await p.waitForTimeout(300);await p.screenshot({path:n+'.png',fullPage:true});}
await b.close();})();
