# Using strace, find out why Apache is returning a 500 error. Once finding the issue, fixing it and then automating it using Puppet

exec { 'install_apache2':
  command  => 'apt install apache2',
  unless   => 'dpkg -l | grep apache2',
  provider => shell,
}
