
/*
 * GET the Web Apps Manifest.
 */

exports.manifest = function(req, res){
  res.set('Content-Type', 'application/x-web-app-manifest+json');
  res.send({
    "name": "MozCampAsia-QualityApps",
    "description": "How To Build Quality Apps",
    "launch_path": "/",
    "icons": {
        "128": "/images/dragon-thumb.jpg",
        "16": "/images/dragon-thumb-16.jpg",
        "60": "/images/dragon-thumb-32.jpg"
      },
    "developer": {
        "name": "David Burns",
        "url": "http://www.theautomatedtester.co.uk"
      },
    "default_locale": "en"
  });
};

