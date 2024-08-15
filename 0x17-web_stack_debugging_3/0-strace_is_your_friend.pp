# Using strace, find out why Apache is returning a 500 error. Once finding the issue, fixing it and then automating it using Puppet

# draft
file { '/etc/draft':
  ensure  => file,
  mode    => '0644'
  content => 'draft',
}
