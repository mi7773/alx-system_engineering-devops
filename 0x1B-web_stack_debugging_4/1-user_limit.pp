# 1-user_limit.pp

exec { '1-user_limit.pp':
  command => '/bin/sed -i -e "s/hard nofile 5/hard nofile 2500" -e "s/soft nofile 4/soft nofile 2000" /etc/security/limits.conf',
}
