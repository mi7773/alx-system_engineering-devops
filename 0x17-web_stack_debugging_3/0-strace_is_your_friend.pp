# Using strace, find out why Apache is returning a 500 error. Once finding the issue, fixing it and then automating it using Puppet

exec { 'draft':
  command => 'sed -i s/pp/py/g /var/a.py',
  path    => '/bin/',
}
