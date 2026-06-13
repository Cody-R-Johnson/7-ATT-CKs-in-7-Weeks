const banner = "ACME local training target loaded";
window.ACME_BUILD = {
  environment: "warehouse-lab",
  internalHost: "intranet.acme.local",
  legacyConfigPath: "/internal/config",
  demoToken: "FAKE_ACME_DEMO_KEY_DO_NOT_USE"
};
console.debug(banner, window.ACME_BUILD);
