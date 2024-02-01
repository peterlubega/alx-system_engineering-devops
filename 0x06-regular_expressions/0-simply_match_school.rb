#!/usr/bin/env ruby

# Print the result of scanning the first command-line argument for the pattern "School"
puts ARGV[0].scan(/School/).join
