import pdb

unlock = """
  let setlock = window.wrappedJSObject.SettingsListener.getSettingsLock();
  let obj = {'screen.timeout': 0};
  setlock.set(obj);
         
  waitFor(
    function() {
      window.wrappedJSObject.LockScreen.unlock();
      waitFor(
        function() {
          finish(window.wrappedJSObject.LockScreen.locked);
        },
        function() {
          return !window.wrappedJSObject.LockScreen.locked;
        }
      );
    },
    function() {
      return !!window.wrappedJSObject.LockScreen;
    }
  );
"""

from marionette import Marionette 

marionette = Marionette('localhost', 2828)
marionette.start_session()
marionette.import_script('gaia_apps.js')
marionette.set_script_timeout(60000)

marionette.execute_script(unlock)
result = marionette.execute_async_script("GaiaApps.launchWithName('%s')" % "NxtGenUG-QualityApps")

marionette.switch_to_frame(result.get("frame"))
pdb.set_trace()
