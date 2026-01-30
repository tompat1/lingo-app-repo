const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const appPath = path.join(projectRoot, "App.tsx");

function fail(message) {
  console.error(message);
  process.exit(1);
}

if (!fs.existsSync(appPath)) {
  fail(`Missing App.tsx at ${appPath}`);
}

const appSource = fs.readFileSync(appPath, "utf8");

const defaultApiPattern =
  /Platform\.OS === "android"\s*\?\s*"http:\/\/10\.0\.2\.2:8000"\s*:\s*"http:\/\/localhost:8000"/;

if (!defaultApiPattern.test(appSource)) {
  fail(
    "Expected DEFAULT_API_BASE to use 10.0.2.2 for Android and localhost otherwise."
  );
}

if (!appSource.includes("EXPO_PUBLIC_API_BASE")) {
  fail("Expected API_BASE to reference EXPO_PUBLIC_API_BASE override.");
}

console.log("API base defaults verified.");
