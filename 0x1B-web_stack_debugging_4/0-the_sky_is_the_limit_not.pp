# 0-the_sky_is_the_limit_not.pp

exec { '0-the_sky_is_the_limit_not.pp':
  command => '/bin/bash sed -i s/15/4096/g /etc/default/nginx'
}
