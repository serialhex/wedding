#!/usr/bin/env ruby
require "cgi"
require "pstore"
require "digest"
# require "rubygems"
# require 'pry'

# http://www.ruby-doc.org/stdlib-1.9.3/libdoc/cgi/rdoc/CGI.html
# http://ruby-doc.org/stdlib-1.8.7/libdoc/pstore/rdoc/PStore.html

class Rsvp
  def initialize
    @pee = PStore.new("wedding.db")
    @cgi = CGI.new("html4")
  end
  attr_reader :cgi, :pee

  def save_data
    params = @cgi.params
    str =  params['first-name'].to_s.downcase + " "
    str += params['last-name'].to_s.downcase
    @pee.transaction do
      @pee[Digest::MD5.hexdigest(str)] = params
    end
    "data saved:<br>\n" + str
  end

  def out_html
    yay_nay=false
    @cgi.out() do
      @cgi.html() do
        @cgi.head() do
          head_str = "<meta http-equiv=\"refresh\" content=\"1; url=http://www.blue-ninja.com/wedding/"
          if @cgi["rsvp-code"].downcase.strip == "mushroom"
            head_str += "good-code.html\">"
            save_data
            yay_nay=true
          else
            head_str += "bad-code.html\">"
          end
          head_str
        end +
        @cgi.body() do
          res="stuff here<br>\n"
          res+=yay_nay.to_s
          # res+=dbinfo
          res
        end
      end
    end
  end

  def dbinfo
    str = ''
    @pee.transaction do
      @pee.roots.each do |data_name|
        str += data_name + "<br>\n"
        @pee[data_name].each do |k,v|
          str += k + ": " + v.join(' ') + "<br>\n"
        end
      end
    end
    str
  end

end

# first-name=moo
# last-name=poop
# rsvp-code=mushroom

rsvp = Rsvp.new
rsvp.out_html
# binding.pry
