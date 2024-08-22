# 1-user_limit.pp

exec { '1-user_limit.pp':
  command => '/bin/sed -i -e "s/hard nofile 5/hard nofile 4096" -e "s/soft nofile 4096/soft nofile 4096" /etc/security/limits.conf',
}
