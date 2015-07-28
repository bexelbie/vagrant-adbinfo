Gem::Specification.new do |spec|
  spec.name          = 'vagrant-dockerinfo'
  spec.version       = '0.0.1'
  spec.homepage      = 'https://github.com/bexelbie/vagrant-dockerinfo'
  spec.summary       = 'Vagrant plugin that provides the IP address:port and tls certificate file location for a docker daemon'

  spec.authors       = ['Brian Exelbierd']
  spec.email         = ['bex@pobox.com']

  spec.files         = `git ls-files -z`.split("\x0")
  spec.require_paths = ['lib']

  spec.add_development_dependency 'bundler', '~> 1.6'
  spec.add_development_dependency 'rake'
end
