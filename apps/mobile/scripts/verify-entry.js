const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const pkgPath = path.join(projectRoot, "package.json");
const entryPath = path.join(projectRoot, "index.ts");

function fail(message) {
  console.error(message);
  process.exit(1);
}

if (!fs.existsSync(pkgPath)) {
  fail(`Missing package.json at ${pkgPath}`);
}

const pkg = JSON.parse(fs.readFileSync(pkgPath, "utf8"));

if (pkg.main !== "index.ts") {
  fail(`Expected package.json main to be index.ts, got ${pkg.main}`);
}

if (!fs.existsSync(entryPath)) {
  fail(`Missing Expo entry file at ${entryPath}`);
}

const entry = fs.readFileSync(entryPath, "utf8");

if (!entry.includes("registerRootComponent")) {
  fail("Expo entry file does not register root component.");
}

console.log("Expo entry file present and registers root component.");
