import { access, copyFile, readFile, writeFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const projectRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const sourcePath = resolve(projectRoot, 'gewitterradar-card-v4_05.js');
const distPath = resolve(projectRoot, 'dist', 'gewitterradar.js');
const packageSourcePath = resolve(projectRoot, 'home-assistant', 'app_gewitterradar_pkg.yaml');
const packageDistPath = resolve(projectRoot, 'dist', 'app_gewitterradar_pkg.yaml');

let card = await readFile(sourcePath, 'utf8');
const assets = new Set();

card = card.replace(/'\/local\/gewitterradar\/assets\/([^']+)'/g, (_, assetWithQuery) => {
  assets.add(assetWithQuery.split('?')[0]);
  return `new URL('./assets/${assetWithQuery}', import.meta.url).href`;
});

if (assets.size !== 15) {
  throw new Error(`Expected exactly 15 V4.05 assets, found ${assets.size}.`);
}

for (const asset of assets) {
  await access(resolve(projectRoot, 'dist', 'assets', asset));
}

await writeFile(distPath, card, 'utf8');
await copyFile(packageSourcePath, packageDistPath);
console.log(`Built ${distPath} from V4.05 with ${assets.size} verified asset references and staged app_gewitterradar_pkg.yaml.`);
