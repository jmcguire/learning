#!/usr/bin/end ruby

number = rand(11)

pick = nil

while pick != number
	puts "what number am i thinking of?"
	pick = gets().to_i

	if pick > number
		puts "too high"
	elsif pick < number
		puts "too low"
	end

end

puts "correct!"

