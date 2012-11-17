
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { title: 'MozCamp Asia 2012' });
};
