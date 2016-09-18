a = []
16.times do
	a.push(rand(100))
end

a.each {|item| puts item if i % 4 == 0; print "#{item}, " if i % 4 != 0; i += 1}

a.each_slice(4) {|item| p item}


