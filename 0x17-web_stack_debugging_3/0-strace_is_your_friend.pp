# Using strace, find out why Apache is returning a 500 error. Once finding the issue, fixing it and then automating it using Puppet

file { '/etc/draft':
  ensure  => file,
  content => 'draft',
}
