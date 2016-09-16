#!/usr/bin/env ruby

search   = ARGV[0]
filename = ARGV[1]

File.open(filename, 'r') do |file|
	file.each do |line|
		puts line if line.include? search
	end
end

