var request = require('request')
  , assert = require('assert')
  , server = require('../app');

describe('server', function () {
  it('should return a manifest file', function(done) {
    request('http://localhost:3000/manifest.webapp', function (err, resp, body){
      assert.ok(resp.statusCode == 200);
      done();
    });
  });

  it('should get the right content type for the manifest', function(done){
    request('http://localhost:3000/manifest.webapp', function (err, resp, body){
      assert.ok(resp.headers['content-type'] == 'application/x-web-app-manifest+json');
      done();
    });
  });
});
