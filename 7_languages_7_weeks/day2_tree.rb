#!/usr/bin/env ruby

class Tree
	attr_accessor :children, :node_name

	def initialize(name, children=[])
		@children = children
		@node_name = name
	end

	def initialize(name, children={})
		@node_name = name
		if children
			@children = children.each_key.collect {|parent| Tree.new(parent, children[parent]) }
		end
	end

	def visit_all(&block)
		visit &block
		children.each {|c| c.visit_all &block}
	end

	def visit(&block)
		block.call self
	end
end

#family_tree = Tree.new( "Dad", [Tree.new('Justin'), Tree.new('Sarah')] )
family_tree = Tree.new("Eve", {
		'grandpa' => {
		  'dad'   => {'child 1' => {}, 'child 2' => {} },
		  'uncle' => {'child 3' => {}, 'child 4' => {} }
		}
	}
)

puts "visiting a node"
family_tree.visit {|node| puts node.node_name}
puts

puts "visiting the whole tree"
family_tree.visit_all {|node| puts node.node_name}

