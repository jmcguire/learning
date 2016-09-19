#!/usr/bin/env ruby

module ActsAsCsv
  def self.included(base)
    base.extend ClassMethods
  end

  module ClassMethods
    def acts_as_csv
      include InstanceMethods
    end
  end

  module InstanceMethods   
    attr_accessor :headers, :csv_contents

    def initialize
      read 
    end

    def read
      @csv_contents = []
      filename = self.class.to_s.downcase + '.txt'
      file = File.new(filename)
      @headers = file.gets.chomp.split(', ')

      file.each do |row|
        @csv_contents << row.chomp.split(', ')
      end
    end

    def each &block
      csv_rows = @csv_contents.collect {|r| CsvRow.new(@headers, r)}
      csv_rows.each(&block)
    end
  end
end


class CsvRow
  attr_accessor :headers, :row

  def initialize headers, row
    @headers = headers
    @row = row
  end

  def method_missing name, *args
    header = name.to_s
    index = @headers.index(header)
    @row[index]
  end
end


class RubyCsv  # no inheritance! You can mix it in
  include ActsAsCsv
  acts_as_csv
end


m = RubyCsv.new
puts m.headers.inspect
puts m.csv_contents.inspect

csv = RubyCsv.new
csv.each {|row| puts row.one}

