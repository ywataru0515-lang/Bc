const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:670},deviceScaleFactor:1.5});
await p.goto('file://'+process.cwd()+'/src/cover_overlay.html');await p.waitForTimeout(300);await p.screenshot({path:'cover_overlay.png',omitBackground:true});
await b.close();})();
