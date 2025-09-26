const { chromium } = require('playwright');

async function testLinks() {
  const links = [
    'https://v0.dev',
    'https://bolt.new',
    'https://replit.com/',
    'https://v0.dev/docs',
    'https://bolt.new/guide',
    'https://docs.replit.com'
  ];

  console.log('リンクのテストを開始します...\n');

  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  const results = [];

  for (const link of links) {
    try {
      console.log(`テスト中: ${link}`);
      const response = await page.goto(link, {
        waitUntil: 'domcontentloaded',
        timeout: 30000
      });

      const status = response.status();
      const ok = status >= 200 && status < 400;

      results.push({
        url: link,
        status: status,
        ok: ok
      });

      console.log(`✅ ${link} - ステータス: ${status}\n`);
    } catch (error) {
      console.log(`❌ ${link} - エラー: ${error.message}\n`);
      results.push({
        url: link,
        status: 'ERROR',
        ok: false,
        error: error.message
      });
    }
  }

  await browser.close();

  console.log('\n=== テスト結果サマリー ===');
  console.log(`テストしたリンク数: ${links.length}`);
  console.log(`成功: ${results.filter(r => r.ok).length}`);
  console.log(`失敗: ${results.filter(r => !r.ok).length}`);

  if (results.filter(r => !r.ok).length > 0) {
    console.log('\n失敗したリンク:');
    results.filter(r => !r.ok).forEach(r => {
      console.log(`- ${r.url} (${r.error || 'Status: ' + r.status})`);
    });
  }
}

testLinks().catch(console.error);