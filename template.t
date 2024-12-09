#
#  Author: KhulnaSoft, Ltd
#  Date: [% DATE # 2013-01-06 01:06:57 +0000 (Sun, 06 Jan 2013) %]
#
#  [% VIM_TAGS %]
#
#  [% URL %]
#
#  [% LICENSE %]
#
#  [% MESSAGE %]
#
#  [% LINKEDIN %]
#

use diagnostics;
use warnings;
use strict;
use Test::More;
use File::Basename;
BEGIN {
    use lib dirname(__FILE__) . "/..";
    use_ok('BuildScale::NAME');
}
require_ok('BuildScale::NAME');


done_testing();
