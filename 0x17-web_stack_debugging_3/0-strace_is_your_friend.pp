# Using strace, find out why Apache is returning a 500 error. Once finding the issue, fixing it and then automating it using Puppet

exec { 'php':
  command  => 'sed -i "/s/pph/php/g" /var/test.php',
  provider => shell,
}
