const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:670},deviceScaleFactor:1.5});
await p.goto('file://'+process.cwd()+'/src/cover.html');await p.waitForTimeout(500);await p.screenshot({path:'00_cover.jpg',type:'jpeg',quality:88});
await b.close();})();
